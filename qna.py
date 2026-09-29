"""
EduGenie - Question Answering Module

Uses Gemini 3.5 Flash-Lite to answer student questions
in a clear and educational manner.
"""

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
# QUESTION ANSWERING
# ============================================================

def answer_question(question: str) -> str:
    """
    Answer a student's question using Gemini 3.5 Flash-Lite.
    """

    if not question or not question.strip():
        raise ValueError("Question cannot be empty.")

    question = question.strip()

    if len(question) > 5000:
        raise ValueError(
            "Question is too long. Maximum length is 5000 characters."
        )

    prompt = f"""
You are EduGenie, an AI learning assistant for college students.

Answer the student's question clearly and accurately.

Guidelines:
- Explain in simple student-friendly language.
- Give the main answer first.
- Break complex ideas into smaller points.
- Use examples when they improve understanding.
- Use headings or bullet points when useful.
- For programming questions, include a small relevant example when appropriate.
- Do not unnecessarily make the answer very long.
- Do not mention that you are following these instructions.

Student Question:
{question}
"""

    try:
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt,
            config=types.GenerateContentConfig(
                max_output_tokens=2048,
            ),
        )

        answer = response.text

        if not answer:
            raise RuntimeError(
                "Gemini returned an empty response."
            )

        return answer.strip()

    except Exception as exc:
        raise RuntimeError(
            f"Gemini question answering failed: {exc}"
        ) from exc