from functools import lru_cache

from langchain.chat_models import init_chat_model
from langchain_openai import ChatOpenAI

from core.config import (
    LLM_PROVIDER,
    LOCAL_LLM_MODEL,
    LOCAL_LLM_BASE_URL,
    LOCAL_LLM_API_KEY,
    OPENAI_MODEL,
    API_GATEWAY_KEY,
    OPENAI_BASE_URL,
    LLM_TEMPERATURE
)
from core.tool_registry import TOOLS


# ============================================================
# Model Factory
# ============================================================
@lru_cache(maxsize=1)
def get_model_with_tools():

    print(f"LLM_PROVIDER is : {LLM_PROVIDER}")

    # --------------------------------------------------------
    # OpenAI / Cloud Mode
    # --------------------------------------------------------
    if LLM_PROVIDER == "openai":

        model = init_chat_model(
            OPENAI_MODEL,
            temperature=LLM_TEMPERATURE,
            base_url=OPENAI_BASE_URL,
            api_key="any value",
            default_headers={
                "x-api-key": API_GATEWAY_KEY
            }
        )

    # --------------------------------------------------------
    # Local Mode
    # --------------------------------------------------------
    elif LLM_PROVIDER == "local":

        model = ChatOpenAI(
            model=LOCAL_LLM_MODEL,
            temperature=LLM_TEMPERATURE,
            base_url=LOCAL_LLM_BASE_URL,
            api_key=LOCAL_LLM_API_KEY
        )

    else:
        raise ValueError(f"Invalid LLM_PROVIDER: {LLM_PROVIDER}")

    return model.bind_tools(TOOLS)