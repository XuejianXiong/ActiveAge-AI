from typing import Literal

from langchain_core.messages import SystemMessage, ToolMessage, AIMessage
from langgraph.graph import StateGraph, START, END

from agents.state import MessagesState
from core.prompt_builder import build_full_system_prompt
from core.models import get_model_with_tools
from core.tool_registry import TOOLS
from core.guardrails import check_guardrails


# ============================================================
# Guardrail Node
# ============================================================
def guardrail_node(state: MessagesState):
    """
    Pre-LLM safety validation.
    Stops unsafe or out-of-scope queries early.
    """

    user_message = state["messages"][-1].content
    blocked_response = check_guardrails(user_message)

    if blocked_response:
        return {
            "blocked": True,
            "final_output": blocked_response,
            "messages": [AIMessage(content=blocked_response)]            
        }

    return {
        "blocked": False,
        "final_output": None
    }


# ============================================================
# LLM Node
# ============================================================
def llm_call(state: MessagesState):
    """
    Executes LLM with dynamic prompt builder + tool awareness.
    """

    model = get_model_with_tools()
    call_count = state.get("llm_calls", 0)

    # Dynamic prompt builder
    active_tool = state.get("active_tool")
    system_prompt = build_full_system_prompt(active_tool)

    if call_count == 0:
        status_update = "\n[SYSTEM NOTE: First interaction. Include a friendly greeting.]"
    else:
        status_update = "\n[SYSTEM NOTE: Continue conversation. Do not repeat greeting.]"

    response = model.invoke(
        [SystemMessage(content=system_prompt + status_update)]
        + state["messages"]
    )

    return {
        "messages": [response],
        "llm_calls": call_count + 1
    }


# ============================================================
# Tool Node
# ============================================================
def tool_node(state: MessagesState):
    """
    Executes tool calls and records active tool for prompt context.
    """

    tools_by_name = {tool.name: tool for tool in TOOLS}

    tool_outputs = []
    last_tool = None

    for tool_call in state["messages"][-1].tool_calls:
        tool_name = tool_call["name"]
        last_tool = tool_name

        tool = tools_by_name[tool_name]
        observation = tool.invoke(tool_call["args"])

        tool_outputs.append(
            ToolMessage(
                content=observation,
                tool_call_id=tool_call["id"]
            )
        )

    return {
        "messages": tool_outputs,
        "active_tool": last_tool
    }


# ============================================================
# Routing Logic
# ============================================================
def route_after_guardrails(state: MessagesState) -> Literal["llm_call", END]:
    if state.get("blocked", False):
        return END
    return "llm_call"


def should_continue(state: MessagesState) -> Literal["tool_node", END]:
    """
    Determines whether to execute tools or finish response.
    """

    last_message = state["messages"][-1]

    if last_message.tool_calls:
        return "tool_node"

    return END


# ============================================================
# Agent Factory
# ============================================================
def get_exercise_chat_agent():
    """
    Builds LangGraph agent with modular prompt + guardrails + tool routing.
    """

    graph = StateGraph(MessagesState)

    # Nodes
    graph.add_node("guardrails", guardrail_node)
    graph.add_node("llm_call", llm_call)
    graph.add_node("tool_node", tool_node)

    # Entry
    graph.add_edge(START, "guardrails")

    # Guardrail decides whether we continue or stop
    graph.add_conditional_edges(
        "guardrails",
        route_after_guardrails,
        ["llm_call", END]
    )

    # LLM routing
    graph.add_conditional_edges(
        "llm_call",
        should_continue,
        ["tool_node", END]
    )

    # Tool loop
    graph.add_edge("tool_node", "llm_call")

    return graph.compile()