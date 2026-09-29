"""
EduGenie - Personalized Learning Path Module

Uses Gemini 3.5 Flash-Lite to generate
structured and personalized learning recommendations.
"""

import json
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from model_config import GEMINI_MODEL


# ============================================================
# ENVIRONMENT AND GEMINI CLIENT
# ============================================================

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY is not configured in the .env file."
    )

client = genai.Client(api_key=api_key)


# ============================================================
# PERSONALIZED LEARNING PATH
# ============================================================

def generate_learning_path(
    subject: str,
    current_level: str,
    learning_goal: str,
    available_time: str = "1 hour per day",
    duration_weeks: int = 4,
) -> dict:
    """
    Generate a personalized learning path using
    Gemini 3.5 Flash-Lite.
    """

    if not subject or not subject.strip():
        raise ValueError("Subject cannot be empty.")

    subject = subject.strip()

    if len(subject) > 200:
        raise ValueError(
            "Subject is too long. Maximum length is 200 characters."
        )

    if not current_level or not current_level.strip():
        raise ValueError("Current level cannot be empty.")

    current_level = current_level.strip()

    if len(current_level) > 100:
        raise ValueError(
            "Current level is too long. Maximum length is 100 characters."
        )

    if not learning_goal or not learning_goal.strip():
        raise ValueError("Learning goal cannot be empty.")

    learning_goal = learning_goal.strip()

    if len(learning_goal) > 500:
        raise ValueError(
            "Learning goal is too long. Maximum length is 500 characters."
        )

    if not available_time or not available_time.strip():
        raise ValueError("Available time cannot be empty.")

    available_time = available_time.strip()

    if len(available_time) > 100:
        raise ValueError(
            "Available time is too long. Maximum length is 100 characters."
        )

    if not 1 <= duration_weeks <= 52:
        raise ValueError(
            "Duration must be between 1 and 52 weeks."
        )

    prompt = f"""
You are EduGenie, an AI learning assistant for college students.

Create a personalized learning path for the student.

Subject:
{subject}

Current Level:
{current_level}

Learning Goal:
{learning_goal}

Available Study Time:
{available_time}

Duration:
{duration_weeks} weeks

Requirements:
- Create a practical and realistic learning plan.
- Start from the student's current level.
- Progress from basic concepts toward more advanced concepts.
- Divide the plan week by week.
- Include topics to study each week.
- Include practical activities or exercises.
- Include useful learning suggestions.
- Keep the plan suitable for a college student.
- Respect the available study time.
- Make the learning goal the main focus.
- Do not invent certifications, courses, or external resources.
- Keep the recommendations clear and actionable.

Return ONLY valid JSON in exactly this structure:

{{
    "subject": "{subject}",
    "current_level": "{current_level}",
    "learning_goal": "{learning_goal}",
    "duration_weeks": {duration_weeks},
    "weekly_plan": [
        {{
            "week": 1,
            "focus": "Main focus for this week",
            "topics": [
                "Topic 1",
                "Topic 2"
            ],
            "activities": [
                "Practical activity 1",
                "Practical activity 2"
            ],
            "suggestion": "Useful suggestion for this week"
        }}
    ],
    "final_recommendation": "Overall recommendation for achieving the learning goal."
}}
"""

    try:
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                max_output_tokens=4096,
            ),
        )

        if not response.text:
            raise RuntimeError(
                "Gemini returned an empty learning path response."
            )

        learning_path = json.loads(response.text)

    except json.JSONDecodeError as exc:
        raise RuntimeError(
            "Gemini returned invalid JSON for the learning path."
        ) from exc

    except Exception as exc:
        raise RuntimeError(
            f"Gemini learning path generation failed: {exc}"
        ) from exc

    if not isinstance(learning_path, dict):
        raise RuntimeError(
            "Learning path response must be a JSON object."
        )

    required_fields = {
        "subject",
        "current_level",
        "learning_goal",
        "duration_weeks",
        "weekly_plan",
        "final_recommendation",
    }

    if not required_fields.issubset(learning_path.keys()):
        raise RuntimeError(
            "Learning path response is missing required fields."
        )

    weekly_plan = learning_path.get("weekly_plan")

    if not isinstance(weekly_plan, list):
        raise RuntimeError(
            "Learning path weekly_plan must be a list."
        )

    if len(weekly_plan) != duration_weeks:
        raise RuntimeError(
            f"Expected {duration_weeks} weeks, "
            f"but received {len(weekly_plan)}."
        )

    required_week_fields = {
        "week",
        "focus",
        "topics",
        "activities",
        "suggestion",
    }

    for index, week in enumerate(weekly_plan, start=1):

        if not isinstance(week, dict):
            raise RuntimeError(
                f"Week {index} is not a valid object."
            )

        if not required_week_fields.issubset(week.keys()):
            raise RuntimeError(
                f"Week {index} is missing required fields."
            )

        if not isinstance(week["topics"], list):
            raise RuntimeError(
                f"Week {index} topics must be a list."
            )

        if not isinstance(week["activities"], list):
            raise RuntimeError(
                f"Week {index} activities must be a list."
            )

        if not str(week["focus"]).strip():
            raise RuntimeError(
                f"Week {index} has an empty focus."
            )

        if not str(week["suggestion"]).strip():
            raise RuntimeError(
                f"Week {index} has an empty suggestion."
            )

    final_recommendation = learning_path.get(
        "final_recommendation"
    )

    if not str(final_recommendation).strip():
        raise RuntimeError(
            "Learning path has an empty final recommendation."
        )

    return learning_path