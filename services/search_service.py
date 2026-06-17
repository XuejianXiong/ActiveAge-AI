from functools import lru_cache

from langchain.tools import tool
from langchain_community.tools.tavily_search import TavilySearchResults

from core.config import WEB_TOP_K


# ============================================================
# Search Service
# ============================================================
@lru_cache(maxsize=1)
def get_search_client() -> TavilySearchResults:
    """
    Lazily initialize the Tavily search client.
    """
    return TavilySearchResults(k=WEB_TOP_K)


def search_web(query: str) -> str:
    """
    Execute a web search and format the retrieved results.
    """

    search_client = get_search_client()

    results = search_client.run(query)

    if not results:
        return "No relevant web search results were found."

    content_list = []

    for result in results:
        content_list.append(
            f"Source: {result.get('url')}\n"
            f"Content: {result.get('content')}"
        )

    return "\n\n".join(content_list)

