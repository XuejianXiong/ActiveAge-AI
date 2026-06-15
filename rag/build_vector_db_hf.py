from pathlib import Path

from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


# ============================================================
# Configuration
# ============================================================
DATA_FILE = Path("data/mental.csv")
PERSIST_DIRECTORY = Path("data/chroma_db_hf")

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


# ============================================================
# Validation
# ============================================================
def validate_inputs() -> None:
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Input file does not exist: {DATA_FILE}"
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
def get_embedding_model() -> HuggingFaceEmbeddings:
    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
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
    validate_inputs()
    build_vector_database()


if __name__ == "__main__":
    main()