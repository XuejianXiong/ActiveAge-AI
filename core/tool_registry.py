"""
Central registry for all tools used by the ActiveAge agent.
This ensures a single source of truth for tool definitions.
"""

from tools.exercise import get_body_exercise
from tools.search import get_web_search
from tools.mental import create_mental_tool

from core.config import EMBEDDING_PROVIDER


# ============================================================
# Tool Initialization
# ============================================================
def _init_mental_tool():
    """
    Creates the mental activity tool with selected embedding backend.
    """
    return create_mental_tool(EMBEDDING_PROVIDER)


# ============================================================
# Tool Registry
# ============================================================
def get_tools():
    """
    Returns all available tools for the agent.
    """
    mental_tool = _init_mental_tool()

    return [
        get_body_exercise,
        mental_tool,
        get_web_search
    ]


# ============================================================
# Global export (used by agent + model)
# ============================================================
TOOLS = get_tools()