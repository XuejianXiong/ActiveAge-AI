from typing import Optional


# ============================================================
# Safety Policy (Configuration Layer)
# ============================================================
RESTRICTED_TERMS = {
    "medical_risk": [
        "diagnose me",
        "diagnosis",
        "cure for",
        "treatment plan",
        "prescription",
        "medication dosage",
        "drug interaction",
        "self-medication",
        "stop taking medication"
    ],

    "emergency": [
        "chest pain treatment",
        "heart attack treatment at home",
        "stroke treatment at home",
        "emergency bypass",
        "suicide",
        "self harm",
        "overdose"
    ],

    "misinformation": [
        "miracle cure",
        "guaranteed cure",
        "replace doctor",
        "no side effects",
        "detox cleanse cure disease",
        "anti vaccine",
        "vaccines cause"
    ],

    "out_of_scope": [
        "horoscope",
        "astrology",
        "zodiac",
        "fortune telling",
        "psychic reading",
        "lottery prediction"
    ],

    "sensitive": [
        "what is my illness",
        "am I sick",
        "life expectancy"
    ]
}


# ============================================================
# Policy Response Map (what system returns on violation)
# ============================================================
RESPONSE_MAP = {
    "emergency": (
        "If this is an emergency, please contact local emergency services immediately. "
        "I can help with safe fitness or wellness guidance."
    ),

    "medical_risk": (
        "I cannot provide medical advice, but I can suggest safe wellness exercises."
    ),

    "misinformation": (
        "I focus on safe, evidence-based wellness activities rather than unverified claims."
    ),

    "out_of_scope": (
        "I focus on physical and mental wellness activities like exercise and brain training."
    ),

    "sensitive": (
        "I’m not able to assess personal medical conditions, but I can help with safe wellness routines."
    ),

    "default": (
        "I focus on safe physical and mental wellness activities."
    )
}


# ============================================================
# Guardrail Engine (Logic Layer)
# ============================================================
def check_guardrails(user_message: str) -> Optional[str]:
    """
    Pre-LLM safety filter.

    Detects unsafe or out-of-scope queries and returns a
    safe response if a violation is detected.

    Returns:
        str: safe fallback response if blocked
        None: if request is allowed
    """

    message = user_message.lower()

    for category, terms in RESTRICTED_TERMS.items():
        for term in terms:
            if term in message:
                return RESPONSE_MAP.get(
                    category,
                    RESPONSE_MAP["default"]
                )

    return None