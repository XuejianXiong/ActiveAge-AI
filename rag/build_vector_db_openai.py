from pathlib import Path
import os

from dotenv import load_dotenv

from core.config import DATA_FILE, CHROMA_DB_OPENAI
from core.embeddings import get_embedding_model
from rag.vector_db_builder import load_documents, build_vector_database


# ============================================================
# Environment
# ============================================================
def validate_environment() -> None:
    load_dotenv(".secrets")

    required_vars = [
        "OPENAI_API_KEY",
        "API_GATEWAY_KEY",
    ]

    missing = [var for var in required_vars if not os.getenv(var)]

    if missing:
        raise ValueError(
            f"Missing required environment variables: {', '.join(missing)}"
        )


# ============================================================
# Main
# ============================================================
def main() -> None:
    validate_environment()

    documents = load_documents(DATA_FILE)

    embedding_model = get_embedding_model("openai")

    build_vector_database(
        documents,
        embedding_model,
        CHROMA_DB_OPENAI
    )


if __name__ == "__main__":
    main()