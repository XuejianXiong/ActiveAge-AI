import os
from functools import lru_cache

from langchain.tools import tool
from langchain_community.vectorstores import Chroma

from core.embeddings import get_embedding_model
from core.config import RAG_TOP_K


def create_mental_tool(embedding_provider: str = "hf"):
    """
    Factory function that returns a configured tool.
    This allows HF or OpenAI embeddings to be injected.
    """

    vector_db_path = f"data/chroma_db_{embedding_provider}"

    embeddings = get_embedding_model(embedding_provider)

    @lru_cache(maxsize=1)
    def get_vector_db():
        return Chroma(
            persist_directory=vector_db_path,
            embedding_function=embeddings
        )

    @tool
    def get_mental_activity(query: str) -> str:
        """
        Retrieve mental fitness, brain exercises, or cognitive training activities designed to improve brain performance.

        This tool covers ANY request related to improving mental health, including memory, attention, focus, and problem-solving.

        Use this tool when the user requests activities involving ANY combination of:

        - brain OR mental OR cognitive OR memory OR thinking OR focus
        AND
        - exercise OR exercises OR training OR workout OR activity OR practice OR fitness OR movement

        Examples include (but are not limited to):
        - brain exercises
        - mental exercise
        - cognitive training
        - memory training
        - brain fitness
        - mental fitness
        - brain workout
        - mental workout
        - cognitive exercises
        - attention training activities
        - focus improvement exercises

        If the request is about improving brain function in any structured or activity-based way → use this tool.
        """

        try:
            vector_db = get_vector_db()

            docs = vector_db.similarity_search(query, k=RAG_TOP_K)

            if not docs:
                return "I couldn't find a matching mental exercise."

            best = docs[0]

            return (
                f"Exercise: {best.metadata.get('Exercise Name', 'Unknown')}\n"
                f"Instructions: {best.page_content}"
            )

        except Exception as e:
            return f"Error retrieving mental activity: {str(e)}"

    return get_mental_activity