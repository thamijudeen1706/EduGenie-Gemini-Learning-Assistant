# 04 — Module Implementation

## Objective

Implement the core AI-powered learning modules of EduGenie according to the selected model architecture.

## Implemented Modules

EduGenie contains five core learning modules.

### 1. Question and Answer

**File:** `qna.py`

Uses Gemini 3.5 Flash-Lite to answer educational questions in a clear and structured manner.

### 2. Concept Explanation

**File:** `explanation_module.py`

Uses the locally loaded LaMini-Flan-T5-783M model to explain concepts in simplified language.

### 3. Quiz Generation

**File:** `quiz_module.py`

Uses Gemini 3.5 Flash-Lite to generate quizzes based on a selected topic, number of questions, and difficulty level.

### 4. Content Summarization

**File:** `summary_module.py`

Uses Gemini 3.5 Flash-Lite to summarize educational content according to the requested summary length.

### 5. Personalized Learning Path

**File:** `learning_path.py`

Uses Gemini 3.5 Flash-Lite to generate a personalized learning plan based on the subject, current level, learning goal, available time, and duration.

## Model Configuration

The central model assignments are maintained in:

`model_config.py`

This keeps the model configuration separate from the individual feature modules.

## Module Structure

EduGenie
|
├── qna.py
├── explanation_module.py
├── quiz_module.py
├── summary_module.py
├── learning_path.py
└── model_config.py

## Verification

All five core learning modules were implemented and integrated with their assigned AI models.

## Status

**Completed**