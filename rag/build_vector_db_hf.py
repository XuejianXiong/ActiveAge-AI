from pathlib import Path

from core.config import DATA_FILE, CHROMA_DB_HF
from core.embeddings import get_embedding_model
from rag.vector_db_builder import load_documents, build_vector_database


# ============================================================
# Validation
# ============================================================
def validate_inputs() -> None:
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Input file does not exist: {DATA_FILE}"
        )


# ============================================================
# Main
# ============================================================
def main() -> None:
    validate_inputs()

    documents = load_documents(DATA_FILE)

    embedding_model = get_embedding_model("hf")

    build_vector_database(
        documents,
        embedding_model,
        CHROMA_DB_HF
    )


if __name__ == "__main__":
    main()