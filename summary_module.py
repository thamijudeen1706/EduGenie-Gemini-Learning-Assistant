"""
EduGenie - Summarization Module

Uses Gemini 3.5 Flash-Lite to summarize
educational content clearly for college students.
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
# SUMMARIZATION
# ============================================================

def summarize_content(
    content: str,
    summary_length: str = "medium",
) -> str:
    """
    Summarize educational content using Gemini 3.5 Flash-Lite.
    """

    # --------------------------------------------------------
    # Validate content
    # --------------------------------------------------------

    if not content or not content.strip():
        raise ValueError("Content cannot be empty.")

    content = content.strip()

    if len(content) > 30000:
        raise ValueError(
            "Content is too long. Maximum length is 30000 characters."
        )


    # --------------------------------------------------------
    # Validate summary length
    # --------------------------------------------------------

    summary_length = summary_length.strip().lower()

    allowed_lengths = {
        "short",
        "medium",
        "long",
    }

    if summary_length not in allowed_lengths:
        raise ValueError(
            "Summary length must be short, medium, or long."
        )


    # ========================================================
    # LENGTH INSTRUCTIONS
    # ========================================================

    length_instructions = {
        "short": (
            "Keep the summary very concise. "
            "Focus only on the most important information."
        ),
        "medium": (
            "Give a balanced summary with the main ideas, "
            "important details, and key concepts."
        ),
        "long": (
            "Give a detailed summary while removing repetition "
            "and unnecessary information."
        ),
    }

    length_instruction = length_instructions[summary_length]


    # ========================================================
    # PROMPT
    # ========================================================

    prompt = f"""
You are EduGenie, an AI learning assistant for college students.

Summarize the following educational content.

Summary length: {summary_length}

Instructions:
- {length_instruction}
- Preserve the original meaning and important facts.
- Do not invent information.
- Use simple, student-friendly language.
- Organize the response clearly.
- Include the most important concepts and points.
- Use headings and bullet points when useful.
- Do not mention these instructions.

Return the summary using this structure:

Summary:
A clear explanation of the main content.

Key Points:
- Important point 1
- Important point 2
- Important point 3

Important Concepts:
- Concept 1
- Concept 2

Educational Content:
{content}
"""


    # ========================================================
    # GEMINI REQUEST
    # ========================================================

    try:
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt,
            config=types.GenerateContentConfig(
                max_output_tokens=2048,
            ),
        )

        if not response.text:
            raise RuntimeError(
                "Gemini returned an empty summary response."
            )

        return response.text.strip()

    except Exception as exc:
        raise RuntimeError(
            f"Gemini summarization failed: {exc}"
        ) from exc