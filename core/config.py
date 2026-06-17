import os
from pathlib import Path
from dotenv import load_dotenv

from core.output_schema import (
    EXERCISE_OUTPUT_SCHEMA,
    WEB_OUTPUT_SCHEMA,
)


# ============================================================
# Load environment
# ============================================================
load_dotenv(".secrets")


# ============================================================
# API Keys
# ============================================================
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
API_GATEWAY_KEY = os.getenv("API_GATEWAY_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")


# ============================================================
# Database
# ============================================================
SQL_URL = os.getenv("SQL_URL")


# ============================================================
# LangSmith / LangChain
# ============================================================
LANGSMITH_TRACING = os.getenv(
    "LANGSMITH_TRACING",
    "false"
).lower() == "true"

LANGCHAIN_PROJECT = os.getenv(
    "LANGCHAIN_PROJECT",
    "activeage-ai"
)


# ============================================================
# Optional Validation (lightweight)
# ============================================================
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is required")
if not API_GATEWAY_KEY:
    raise ValueError("API_GATEWAY_KEY is required")


# ============================================================
# Data Paths
# ============================================================
PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"
DATA_FILE = DATA_DIR / "mental.csv"


# ============================================================
# Vector DB Paths
# ============================================================
CHROMA_DB_HF = DATA_DIR / "chroma_db_hf"
CHROMA_DB_OPENAI = DATA_DIR / "chroma_db_openai"


# ============================================================
# Embedding Configuration
# ============================================================
EMBEDDING_PROVIDER = os.getenv("EMBEDDING_PROVIDER", "hf")
# options: "hf", "openai"

EMBEDDING_MODEL_HF = "sentence-transformers/all-MiniLM-L6-v2"

EMBEDDING_MODEL_OPENAI = "text-embedding-3-small"

OPENAI_BASE_URL = (
    "https://k7uffyg03f.execute-api.us-east-1.amazonaws.com"
    "/prod/openai/v1"
)


# ============================================================
# WGER API Configuration
# ============================================================
WGER_API_URL = "https://wger.de/api/v2/exerciseinfo/"

DEFAULT_LANGUAGE = 2  # English
DEFAULT_LIMIT = 20


# ============================================================
# WEB SEARCH Configuration
# ============================================================
WEB_TOP_K = 3


# ============================================================
# MENTAL RAG Configuration
# ============================================================
RAG_TOP_K = 3


# ============================================================
# LLM Configuration
# ============================================================
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "local")
# options: "local", "openai"

LOCAL_LLM_MODEL = "google/gemma-4-e4b"
LOCAL_LLM_BASE_URL = "http://localhost:1234/v1"
LOCAL_LLM_API_KEY = "lm-studio"

OPENAI_MODEL = "openai:gpt-4o-mini"

LLM_TEMPERATURE = 0.7


# ============================================================
# CHAT HISTORY Configuration
# ============================================================
MAX_CHAT_HISTORY = 20


# ============================================================
# Tool → Output Schema Mapping
# ============================================================
OUTPUT_SCHEMA_MAP = {
    "get_body_exercise": EXERCISE_OUTPUT_SCHEMA,
    "get_mental_activity": EXERCISE_OUTPUT_SCHEMA,
    "get_web_search": WEB_OUTPUT_SCHEMA,
}
