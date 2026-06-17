import os

from langchain_openai import OpenAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings

from core.config import (
    EMBEDDING_MODEL_HF,
    EMBEDDING_MODEL_OPENAI,
    OPENAI_BASE_URL
)


# ============================================================
# Embedding
# ============================================================
def get_embedding_model(provider: str = "hf"):

    if provider == "hf":
        return HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL_HF
        )

    if provider == "openai":
        return OpenAIEmbeddings(
            model=EMBEDDING_MODEL_OPENAI,
            openai_api_base=OPENAI_BASE_URL,
            openai_api_key="any value",
            default_headers={"x-api-key": os.getenv("API_GATEWAY_KEY")}
          )

    raise ValueError(
        f"Unsupported embedding provider: {provider}"
    )

