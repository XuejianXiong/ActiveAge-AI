from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.vectorstores import Chroma


# ============================================================
# Document Loading
# ============================================================
def load_documents(data_file):
    loader = CSVLoader(
        file_path=str(data_file),
        metadata_columns=["Exercise Name"]
    )

    documents = loader.load()
    print(f"Loaded {len(documents)} documents")

    return documents


# ============================================================
# Vector Database Creation
# ============================================================
def build_vector_database(documents, embedding_model, persist_directory):
    Chroma.from_documents(
        documents=documents,
        embedding=embedding_model,
        persist_directory=str(persist_directory)
    )

    print(f"Vector DB created at: {persist_directory}")