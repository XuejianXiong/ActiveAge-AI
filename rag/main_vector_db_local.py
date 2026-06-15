import os
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.vectorstores import Chroma
# Switch to local HuggingFace embeddings
from langchain_huggingface import HuggingFaceEmbeddings

# 1. Load the docs
loader = CSVLoader(
    file_path="data/mental.csv",
    metadata_columns=["Exercise Name"]
)
data = loader.load()

# 2. Initialize the local embedding model
# This runs directly on your machine, no API key required
embeddings_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# 3. Create the Vector Store
persist_directory = "data/chroma_db_local"

# IMPORTANT: Delete your old ./chroma_db folder before running this
# because you are changing the embedding model.
vector_db = Chroma.from_documents(
    documents=data,
    embedding=embeddings_model,
    persist_directory=persist_directory
)

print(f"Database saved locally to {persist_directory}")