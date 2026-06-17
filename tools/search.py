from langchain.tools import tool

from services.search_service import search_web

# ============================================================
# Tool
# ============================================================
@tool
def get_web_search(query: str) -> str:
    """
    Retrieve up-to-date, external, and real-time information from the web when local knowledge is insufficient or when information is time-sensitive, dynamic, or frequently changing.

    This tool is used for ANY request that requires external verification, current data, or information beyond the local knowledge base.

    Use this tool when the user requests information involving ANY combination of:

    - health OR fitness OR nutrition OR wellness OR medical OR scientific OR research
    AND
    - news OR updates OR trends OR latest OR recent OR current OR new OR today OR now
    OR
    - comparison OR statistics OR guidelines OR recommendations requiring up-to-date data

    Examples include (but are not limited to):
    - latest health news
    - recent medical research
    - new fitness trends
    - updated nutrition guidelines
    - current wellness recommendations
    - what is happening in health or fitness right now
    - today's health or fitness updates
    - recent scientific findings
    - new treatment guidelines (non-diagnostic informational context only)
    - comparison of diets, workouts, or supplements with current data

    Also use this tool for any general knowledge request when:
    - the answer may change over time
    - or the user explicitly or implicitly requests recent, real-time, or evolving information

    If the request involves time-sensitive or externally changing information → use this tool.
    """

    try:
        return search_web(query)

    except Exception as exc:
        return (
            f"Unable to retrieve web search results: {str(exc)}"
        )