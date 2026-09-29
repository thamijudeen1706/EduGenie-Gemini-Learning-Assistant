"""
EduGenie AI Model Configuration

This file is the central configuration for all AI models used by EduGenie.

Project model architecture:

- Gemini 3.5 Flash-Lite:
    Question Answering
    Quiz Generation
    Summarization
    Personalized Learning Path

- LaMini-Flan-T5-783M:
    Concept Explanation
"""


# ============================================================
# GEMINI MODEL
# ============================================================

GEMINI_MODEL = "gemini-3.5-flash-lite"


# ============================================================
# LOCAL EXPLANATION MODEL
# ============================================================

LOCAL_EXPLANATION_MODEL = "MBZUAI/LaMini-Flan-T5-783M"


# ============================================================
# FEATURE → MODEL MAPPING
# ============================================================

MODEL_ASSIGNMENTS = {
    "question_answering": GEMINI_MODEL,
    "quiz_generation": GEMINI_MODEL,
    "summarization": GEMINI_MODEL,
    "learning_path": GEMINI_MODEL,
    "concept_explanation": LOCAL_EXPLANATION_MODEL,
}


# ============================================================
# PROJECT INFORMATION
# ============================================================

PROJECT_NAME = "EduGenie"

PROJECT_DESCRIPTION = "Google Gemini Powered Learning Assistant"


# ============================================================
# MODEL PURPOSES
# ============================================================

MODEL_PURPOSES = {
    GEMINI_MODEL: [
        "Question answering",
        "Quiz generation",
        "Educational content summarization",
        "Personalized learning path generation",
    ],

    LOCAL_EXPLANATION_MODEL: [
        "Concept explanation",
        "Simplifying educational concepts",
    ],
}


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_model_for_feature(feature: str) -> str:
    """
    Return the AI model assigned to a specific EduGenie feature.
    """

    if feature not in MODEL_ASSIGNMENTS:
        raise ValueError(
            f"Unknown EduGenie feature: {feature}"
        )

    return MODEL_ASSIGNMENTS[feature]


def get_model_purpose(model: str) -> list[str]:
    """
    Return the purposes assigned to a specific model.
    """

    if model not in MODEL_PURPOSES:
        raise ValueError(
            f"Unknown EduGenie model: {model}"
        )

    return MODEL_PURPOSES[model]