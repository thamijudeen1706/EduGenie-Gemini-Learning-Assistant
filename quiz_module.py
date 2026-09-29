"""
EduGenie - Quiz Generation Module

Uses Gemini 3.5 Flash-Lite to generate
educational multiple-choice quizzes.
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
# QUIZ GENERATION
# ============================================================

def generate_quiz(
    topic: str,
    number_of_questions: int = 5,
    difficulty: str = "medium",
) -> list:
    """
    Generate a multiple-choice quiz using Gemini 3.5 Flash-Lite.
    """

    # --------------------------------------------------------
    # Validate topic
    # --------------------------------------------------------

    if not topic or not topic.strip():
        raise ValueError("Quiz topic cannot be empty.")

    topic = topic.strip()

    if len(topic) > 300:
        raise ValueError(
            "Quiz topic is too long. Maximum length is 300 characters."
        )


    # --------------------------------------------------------
    # Validate number of questions
    # --------------------------------------------------------

    if not 1 <= number_of_questions <= 20:
        raise ValueError(
            "Number of questions must be between 1 and 20."
        )


    # --------------------------------------------------------
    # Validate difficulty
    # --------------------------------------------------------

    difficulty = difficulty.strip().lower()

    allowed_difficulties = {
        "easy",
        "medium",
        "hard",
    }

    if difficulty not in allowed_difficulties:
        raise ValueError(
            "Difficulty must be easy, medium, or hard."
        )


    # ========================================================
    # PROMPT
    # ========================================================

    prompt = f"""
You are EduGenie, an AI learning assistant for college students.

Create a multiple-choice quiz about:

Topic: {topic}

Difficulty: {difficulty}

Number of questions: {number_of_questions}

Requirements:
- Create exactly {number_of_questions} questions.
- Each question must test understanding of the topic.
- Each question must have exactly four options.
- Label the options A, B, C, and D.
- Only one option must be correct.
- Include a short explanation for the correct answer.
- Avoid ambiguous questions.
- Do not repeat questions.
- Keep the questions appropriate for college students.

Return ONLY valid JSON in exactly this structure:

{{
    "questions": [
        {{
            "question": "Question text",
            "options": {{
                "A": "Option A",
                "B": "Option B",
                "C": "Option C",
                "D": "Option D"
            }},
            "correct_answer": "A",
            "explanation": "Explanation of why A is correct."
        }}
    ]
}}
"""


    # ========================================================
    # GEMINI REQUEST
    # ========================================================

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
                "Gemini returned an empty quiz response."
            )

        quiz_data = json.loads(response.text)

    except json.JSONDecodeError as exc:
        raise RuntimeError(
            "Gemini returned invalid JSON for the quiz."
        ) from exc

    except Exception as exc:
        raise RuntimeError(
            f"Gemini quiz generation failed: {exc}"
        ) from exc


    # ========================================================
    # VALIDATE RESPONSE STRUCTURE
    # ========================================================

    if not isinstance(quiz_data, dict):
        raise RuntimeError(
            "Quiz response must be a JSON object."
        )

    questions = quiz_data.get("questions")

    if not isinstance(questions, list):
        raise RuntimeError(
            "Quiz response does not contain a valid questions list."
        )

    if len(questions) != number_of_questions:
        raise RuntimeError(
            f"Expected {number_of_questions} questions, "
            f"but received {len(questions)}."
        )


    # ========================================================
    # VALIDATE EACH QUESTION
    # ========================================================

    required_option_keys = {"A", "B", "C", "D"}

    for index, question in enumerate(questions, start=1):

        if not isinstance(question, dict):
            raise RuntimeError(
                f"Question {index} is not a valid object."
            )

        required_fields = {
            "question",
            "options",
            "correct_answer",
            "explanation",
        }

        if not required_fields.issubset(question.keys()):
            raise RuntimeError(
                f"Question {index} is missing required fields."
            )

        options = question["options"]

        if not isinstance(options, dict):
            raise RuntimeError(
                f"Question {index} options must be an object."
            )

        if set(options.keys()) != required_option_keys:
            raise RuntimeError(
                f"Question {index} must contain exactly "
                f"A, B, C, and D options."
            )

        correct_answer = question["correct_answer"]

        if correct_answer not in required_option_keys:
            raise RuntimeError(
                f"Question {index} has an invalid correct answer."
            )

        if not str(question["question"]).strip():
            raise RuntimeError(
                f"Question {index} has empty question text."
            )

        if not str(question["explanation"]).strip():
            raise RuntimeError(
                f"Question {index} has an empty explanation."
            )


    # ========================================================
    # RETURN QUESTIONS
    # ========================================================

    return questions