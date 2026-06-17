from typing_extensions import TypedDict, Annotated
from typing import Any
import operator

from langchain_core.messages import AnyMessage


class MessagesState(TypedDict):
    """
    LangGraph state definition for ActiveAge agent.
    """

    messages: Annotated[list[AnyMessage], operator.add]
    llm_calls: int
    active_tool: str | None
    blocked: bool
    final_output: str | None