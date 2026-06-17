from uuid import uuid4

import gradio as gr

from utils.logger import get_logger

from agents.activeage_agent import get_exercise_chat_agent

from core.chat import build_langchain_messages, extract_final_output


# ============================================================
# Logging
# ============================================================
logger = get_logger(__name__)


# ============================================================
# Agent Initialization
# ============================================================
agent = get_exercise_chat_agent()


# ============================================================
# Chat Handler
# ============================================================
def exercise_chat(
    message: str,
    history: list[dict]
) -> str:
    """
    Handle user interaction and invoke the ActiveAge agent.
    """

    messages, llm_calls = build_langchain_messages(
        history=history,
        user_message=message
    )

    state = {
        "messages": messages,
        "llm_calls": llm_calls
    }

    response = agent.invoke(
        state,
        config={
            "tags": [
                "activeage",
                "production"
            ],
            "metadata": {
                "session_id": str(uuid4())
            }
        }
    )

    if response.get("blocked"):
        return response["final_output"] 

    return extract_final_output(response["messages"])


# ============================================================
# Gradio Interface
# ============================================================
chat = gr.ChatInterface(
    fn=exercise_chat,
    type="messages",
    title="ActiveAge AI",
    description=(
        "AI assistant built with LangGraph, LangChain, vector databases, "
        "semantic retrieval, and tool orchestration to deliver personalized "
        "physical wellness activities, cognitive training exercises, and "
        "evidence-informed health information."
    )
)


# ============================================================
# Application Entry Point
# ============================================================
if __name__ == "__main__":

    logger.info(
        "Starting ActiveAge AI application..."
    )

    chat.launch()