# 01 — Pre-requisites

## Objective

Set up the essential software, frameworks, dependencies, and API access required to develop and run EduGenie: Google Gemini Powered Learning Assistant.

## Project Requirements

The project requires:

- Python 3.10+
- FastAPI
- Uvicorn
- Jinja2
- HTML and CSS
- Google Gemini API access
- Python virtual environment

## Environment Setup

EduGenie was developed in a Python virtual environment to keep project dependencies isolated from the system Python installation.

**Python Version:** 3.12.0

## AI API Configuration

A Google Gemini API key is required for the Gemini-powered features.

The API key is stored locally in the `.env` file and is excluded from Git tracking using `.gitignore`.

A `.env.example` file will be provided in the repository as a safe configuration template without exposing the actual API key.

## Dependencies

The project dependencies are listed in:

`requirements.txt`

The main frameworks and libraries used include:

- FastAPI
- Uvicorn
- Jinja2
- google-genai
- python-dotenv
- Transformers
- PyTorch
- SentencePiece

## Verification

The project environment was successfully configured and EduGenie was run locally using FastAPI and Uvicorn.

## Status

**Completed**