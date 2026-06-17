from core.prompts import get_system_prompt
from core.config import OUTPUT_SCHEMA_MAP


# ============================================================
# System Prompt Builder
# ============================================================
def build_system_prompt() -> str:
    """
    Builds the full system prompt by combining:
    - base system behavior prompt
    - global output formatting rules (if needed)
    
    This keeps prompt construction modular and production-ready.
    """
    base_prompt = get_system_prompt()

    return base_prompt.strip()


# ============================================================
# Output Schema Builder (Tool-specific)
# ============================================================
def build_output_schema(tool_name: str | None) -> str:
    """
    Returns the output formatting schema for a given tool.

    Each tool can enforce its own response structure to ensure
    consistent and predictable LLM outputs.
    """
    return OUTPUT_SCHEMA_MAP.get(tool_name, "")


# ============================================================
# Full Prompt Composer (optional but recommended)
# ============================================================
def build_full_system_prompt(active_tool: str | None = None) -> str:
    """
    Combines system prompt + tool-specific output schema.

    This is useful when you want stricter control over formatting
    depending on which tool is being used.
    """
    system_prompt = build_system_prompt()

    schema = ""
    if active_tool:
        schema = build_output_schema(active_tool)

    if schema:
        return f"{system_prompt}\n\nOUTPUT FORMAT RULES:\n{schema}"

    return system_prompt