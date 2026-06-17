from typing import Any

import requests

from langchain.tools import tool

from services.exercise_service import (
    fetch_exercises,
    select_random_exercise
)


# ============================================================
# Tool
# ============================================================
@tool
def get_body_exercise() -> str:
    """
    Retrieve physical fitness and movement-based activities designed to improve strength, mobility, flexibility, balance, endurance, and overall physical wellness.

    This tool covers ANY request related to improving physical condition, including structured movement, workouts, and training programs.

    Use this tool when the user requests activities involving ANY combination of:

    - body OR physical OR physical fitness OR muscular OR strength OR mobility OR flexibility OR cardio OR endurance
    AND
    - exercise OR exercises OR workout OR workouts OR training OR activity OR activities OR practice OR fitness OR movement

    Examples include (but are not limited to):
    - body exercises
    - physical exercises
    - workout routines
    - body workout
    - strength training
    - mobility training
    - fitness training
    - cardio workouts
    - endurance training
    - stretching exercises
    - balance training activities
    - full-body workout routines

    If the request is about improving physical health, movement ability, or fitness through structured activities → use this tool.
    """
    try:
        response_data = fetch_exercises()

        return select_random_exercise(response_data)

    except requests.RequestException as exc:
        return (
            f"Unable to retrieve exercise data "
            f"from the exercise service: {str(exc)}"
        )

    except Exception as exc:
        return (
            f"Unexpected error retrieving exercise: "
            f"{str(exc)}"
        )