# 03 — Model Selection and Architecture

## Objective

Select suitable AI models for the EduGenie learning features and define the responsibility of each model within the application architecture.

## Selected AI Models

EduGenie uses two AI models with different responsibilities.

### Gemini 3.5 Flash-Lite

Gemini 3.5 Flash-Lite is used through the Google Gemini API for:

- Question and Answer
- Quiz Generation
- Content Summarization
- Personalized Learning Path

The model is integrated through the `google-genai` Python SDK.

### LaMini-Flan-T5-783M

LaMini-Flan-T5-783M is used locally for:

- Concept Explanation
- Simplifying educational concepts

The model is loaded using the Transformers library and runs locally without requiring a Gemini API request for the explanation feature.

## Model Assignment

| EduGenie Feature | Model |
|---|---|
| Question Answering | Gemini 3.5 Flash-Lite |
| Quiz Generation | Gemini 3.5 Flash-Lite |
| Summarization | Gemini 3.5 Flash-Lite |
| Personalized Learning Path | Gemini 3.5 Flash-Lite |
| Concept Explanation | LaMini-Flan-T5-783M |

## Architecture

EduGenie
|
FastAPI Application
|
+---------------------------+
|                           |
Gemini Features         Local Feature
|                           |
Gemini 3.5 Flash-Lite   LaMini-Flan-T5-783M
|                           |
+------+------+------+      |
|      |      |      |      |
Q&A   Quiz  Summary  Learning Path
                            |
                       Explanation

## Evidence

The model configuration is defined in:

- `model_config.py`

The model-specific implementations are contained in:

- `qna.py`
- `quiz_module.py`
- `summary_module.py`
- `learning_path.py`
- `explanation_module.py`

## Verification

The selected models were integrated into their assigned EduGenie features.

Gemini 3.5 Flash-Lite was successfully tested through the Gemini API, while LaMini-Flan-T5-783M was successfully loaded and used locally for concept explanation.

## Status

**Completed**