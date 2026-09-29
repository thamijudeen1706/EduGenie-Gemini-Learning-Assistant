"""
EduGenie - FastAPI Application

Main backend application for:
- Question Answering
- Concept Explanation
- Quiz Generation
- Summarization
- Personalized Learning Path
"""

from fastapi import (
    FastAPI,
    Request,
    HTTPException,
)
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field


from qna import answer_question
from explanation_module import explain_concept
from quiz_module import generate_quiz
from summary_module import summarize_content
from learning_path import generate_learning_path


# ============================================================
# APPLICATION CONFIGURATION
# ============================================================

app = FastAPI(
    title="EduGenie",
    description=(
        "Google Gemini Powered Learning Assistant"
    ),
    version="1.0.0",
)


# ============================================================
# TEMPLATES AND STATIC FILES
# ============================================================

templates = Jinja2Templates(
    directory="templates"
)

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static",
)


# ============================================================
# REQUEST MODELS
# ============================================================

class QARequest(BaseModel):

    question: str = Field(
        ...,
        min_length=1,
        max_length=5000,
    )


class ExplanationRequest(BaseModel):

    concept: str = Field(
        ...,
        min_length=1,
        max_length=300,
    )

    context: str = Field(
        default="",
        max_length=500,
    )


class QuizRequest(BaseModel):

    topic: str = Field(
        ...,
        min_length=1,
        max_length=300,
    )

    number_of_questions: int = Field(
        default=5,
        ge=1,
        le=20,
    )

    difficulty: str = Field(
        default="medium",
    )


class SummaryRequest(BaseModel):

    content: str = Field(
        ...,
        min_length=1,
        max_length=30000,
    )

    summary_length: str = Field(
        default="medium",
    )


class LearningPathRequest(BaseModel):

    subject: str = Field(
        ...,
        min_length=1,
        max_length=200,
    )

    current_level: str = Field(
        ...,
    )

    learning_goal: str = Field(
        ...,
        min_length=1,
        max_length=500,
    )

    available_time: str = Field(
        default="1 hour per day",
    )

    duration_weeks: int = Field(
        default=4,
        ge=1,
        le=52,
    )


# ============================================================
# GLOBAL EXCEPTION HANDLER
# ============================================================

def handle_service_error(exc: Exception) -> None:
    """
    Convert internal feature errors into HTTP 500 errors.
    """

    raise HTTPException(
        status_code=500,
        detail=str(exc),
    )


# ============================================================
# HOME PAGE
# ============================================================

@app.get("/")
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
    )


# ============================================================
# HEALTH CHECK
# ============================================================

@app.get("/health")
async def health_check():

    return {
        "status": "healthy",
        "application": "EduGenie",
    }


# ============================================================
# QUESTION ANSWERING
# ============================================================

@app.post("/qa")
async def question_answering(request: QARequest):

    try:

        answer = answer_question(
            request.question
        )

        return {
            "success": True,
            "feature": "question_answering",
            "question": request.question,
            "answer": answer,
        }

    except ValueError as exc:

        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )

    except Exception as exc:

        handle_service_error(exc)


# ============================================================
# CONCEPT EXPLANATION
# ============================================================

@app.post("/explain")
async def concept_explanation(
    request: ExplanationRequest,
):

    try:

        explanation = explain_concept(
            concept=request.concept,
            context=request.context,
        )

        return {
            "success": True,
            "feature": "concept_explanation",
            "concept": request.concept,
            "explanation": explanation,
        }

    except ValueError as exc:

        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )

    except Exception as exc:

        handle_service_error(exc)


# ============================================================
# QUIZ GENERATION
# ============================================================

@app.post("/quiz")
async def quiz_generation(
    request: QuizRequest,
):

    try:

        quiz = generate_quiz(
            topic=request.topic,
            number_of_questions=request.number_of_questions,
            difficulty=request.difficulty,
        )

        return {
            "success": True,
            "feature": "quiz_generation",
            "topic": request.topic,
            "difficulty": request.difficulty,
            "questions": quiz,
        }

    except ValueError as exc:

        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )

    except Exception as exc:

        handle_service_error(exc)


# ============================================================
# SUMMARIZATION
# ============================================================

@app.post("/summarize")
async def summarization(
    request: SummaryRequest,
):

    try:

        summary = summarize_content(
            content=request.content,
            summary_length=request.summary_length,
        )

        return {
            "success": True,
            "feature": "summarization",
            "summary_length": request.summary_length,
            "summary": summary,
        }

    except ValueError as exc:

        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )

    except Exception as exc:

        handle_service_error(exc)


# ============================================================
# PERSONALIZED LEARNING PATH
# ============================================================

@app.post("/learn/recommendations")
async def learning_path(
    request: LearningPathRequest,
):

    try:

        path = generate_learning_path(
            subject=request.subject,
            current_level=request.current_level,
            learning_goal=request.learning_goal,
            available_time=request.available_time,
            duration_weeks=request.duration_weeks,
        )

        return {
            "success": True,
            "feature": "personalized_learning_path",
            "learning_path": path,
        }

    except ValueError as exc:

        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )

    except Exception as exc:

        handle_service_error(exc)