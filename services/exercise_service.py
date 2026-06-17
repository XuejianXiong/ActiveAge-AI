import json
import random
from typing import Any

import requests

from core.config import WGER_API_URL, DEFAULT_LANGUAGE, DEFAULT_LIMIT


# ============================================================
# Service Layer
# ============================================================
def fetch_exercises(
    language: int = DEFAULT_LANGUAGE,
    limit: int = DEFAULT_LIMIT
) -> dict[str, Any]:
    """
    Retrieve exercise data from the Wger API.
    """

    response = requests.get(
        WGER_API_URL,
        params={
            "language": language,
            "limit": limit
        },
        timeout=5
    )

    response.raise_for_status()

    return response.json()


def select_random_exercise(
    response_data: dict[str, Any]
) -> str:
    """
    Select a random exercise from the API response.
    """

    exercises = response_data.get("results", [])

    if not exercises:
        return "No exercises found."

    exercise = random.choice(exercises)

    return json.dumps(
        exercise,
        indent=2,
        ensure_ascii=False
    )

