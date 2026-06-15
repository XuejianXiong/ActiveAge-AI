from pathlib import Path
import os

from dotenv import load_dotenv

from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings


# ============================================================
# Configuration
# ============================================================
DATA_FILE = Path("data/mental.csv")
PERSIST_DIRECTORY = Path("data/chroma_db")

EMBEDDING_MODEL = "text-embedding-3-small"

OPENAI_BASE_URL = (
    "https://k7uffyg03f.execute-api.us-east-1.amazonaws.com/prod/openai/v1"
)


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
# Document Loading
# ============================================================
def load_documents():
    loader = CSVLoader(
        file_path=str(DATA_FILE),
        metadata_columns=["Exercise Name"]
    )

    documents = loader.load()

    print(f"Loaded {len(documents)} documents")

    return documents


# ============================================================
# Embedding Model
# ============================================================
def get_embedding_model() -> OpenAIEmbeddings:
    return OpenAIEmbeddings(
        model=EMBEDDING_MODEL,
        openai_api_base=OPENAI_BASE_URL,
        openai_api_key="any value",
        default_headers={
            "x-api-key": os.getenv("API_GATEWAY_KEY")
        }
    )


# ============================================================
# Vector Database Creation
# ============================================================
def build_vector_database() -> None:
    documents = load_documents()

    embedding_model = get_embedding_model()

    Chroma.from_documents(
        documents=documents,
        embedding=embedding_model,
        persist_directory=str(PERSIST_DIRECTORY)
    )

    print(f"Vector database created at: {PERSIST_DIRECTORY}")


# ============================================================
# Main
# ============================================================
def main() -> None:
    validate_environment()
    build_vector_database()


if __name__ == "__main__":
    main()