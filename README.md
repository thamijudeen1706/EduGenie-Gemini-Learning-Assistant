## SkillWallet Submission Documentation

The EduGenie project was documented and submitted through the SkillWallet project workflow across 8 major folders containing 22 project documents.

### Folder 1 — Brainstorming & Ideation

1. Brainstorming & Idea Prioritization.pdf — 3 Marks
2. Define Problem Statements.pdf — 3 Marks
3. Empathy Map.pdf — 4 Marks

### Folder 2 — Requirement Analysis

4. Customer Journey Map.pdf — 2 Marks
5. Data Flow Diagram.pdf — 4 Marks
6. Solution Requirements.pdf — 4 Marks
7. Technology Stack.pdf — 2 Marks

### Folder 3 — Project Design Phase

8. Problem-Solution Fit.pdf — 5 Marks
9. Proposed Solution.pdf — 5 Marks
10. Solution Architecture.pdf — 5 Marks

### Folder 4 — Project Planning Phase

11. Project Planning.pdf — 5 Marks

### Folder 5 — Project Development Phase

12. Code-Layout, Readability and Reusability.pdf — 5 Marks
13. Coding & Solution.pdf — 5 Marks
14. No. of Functional Features Including Solution.pdf — 5 Marks

### Folder 6 — Project Testing

15. Performance Testing.pdf — 5 Marks

### Folder 7 — Project Documentation

16. Project Executable Files.pdf — 3 Marks
17. Sample Project Documentation.pdf — 0 Marks

### Folder 8 — Project Demonstration

18. Communication.pdf — 1 Mark
19. Demonstration of Proposed Features.pdf — 1 Mark
20. Project Demo Planning.pdf — 1 Mark
21. Scalability & Future Plan.pdf — 1 Mark
22. Team Involvement in Demonstration.pdf — 1 Mark

**Total SkillWallet Evaluation: 70 Marks**

### EduGenie Team

1. **THAMIJUDEEN M** — Team Lead
2. **SUNDAR S**
3. **SENTHIL KUMARAN S**
4. **SUDHARSANA SARANGI L**
5. **SUNILKUMAR P**

The team collaborated on the development, testing, documentation, and demonstration of EduGenie.

### Documentation Completion

All 8 SkillWallet documentation folders were completed with the required project documents. The documentation covers the complete project lifecycle:

- Brainstorming and Ideation
- Requirement Analysis
- Project Design
- Project Planning
- Project Development
- Project Testing
- Project Documentation
- Project Demonstration

# EduGenie — Google Gemini Powered Learning Assistant

EduGenie is an AI-powered learning assistant designed to support students with multiple learning activities through a simple and user-friendly web interface.

The application combines Google Gemini with a locally running LaMini-Flan-T5-783M model to provide question answering, concept explanation, quiz generation, content summarization, and personalized learning paths.

## Features

### Question and Answer

Ask educational questions and receive AI-generated answers using Gemini 3.5 Flash-Lite.

### Concept Explanation

Enter a computer science concept and receive a simplified explanation using the locally running LaMini-Flan-T5-783M model.

### Quiz Generation

Generate quizzes based on:

- Topic
- Number of questions
- Difficulty level

The quiz interface allows learners to select answers and move through the generated questions.

### Content Summarization

Provide educational content and generate a summary according to the selected summary length.

### Personalized Learning Path

Generate a personalized learning plan based on:

- Subject
- Current level
- Learning goal
- Available time
- Duration in weeks

## AI Model Architecture

EduGenie uses two AI models with different responsibilities.

### Gemini 3.5 Flash-Lite

Gemini 3.5 Flash-Lite is used through the Google Gemini API for:

- Question and Answer
- Quiz Generation
- Content Summarization
- Personalized Learning Path

### LaMini-Flan-T5-783M

LaMini-Flan-T5-783M runs locally and is used for:

- Concept Explanation
- Simplifying educational concepts

### Model Assignment

| Feature                    | AI Model              |
| -------------------------- | --------------------- |
| Question Answering         | Gemini 3.5 Flash-Lite |
| Concept Explanation        | LaMini-Flan-T5-783M   |
| Quiz Generation            | Gemini 3.5 Flash-Lite |
| Summarization              | Gemini 3.5 Flash-Lite |
| Personalized Learning Path | Gemini 3.5 Flash-Lite |

## Technology Stack

### Backend

- Python 3.12
- FastAPI
- Uvicorn
- Jinja2

### AI and Machine Learning

- Google Gemini API
- Gemini 3.5 Flash-Lite
- Transformers
- LaMini-Flan-T5-783M
- PyTorch
- SentencePiece

### Frontend

- HTML
- CSS
- JavaScript

### Development Tools

- Visual Studio Code
- Python Virtual Environment
- Git
- GitHub

## Project Architecture

```text
User
↓
EduGenie Web Interface
↓
FastAPI Backend
↓
Feature Modules
↓
AI Model
↓
Generated Learning Result
↓
Web Interface
```

## Project Structure

```text
EduGenie/
├── main.py
├── model_config.py
├── qna.py
├── explanation_module.py
├── quiz_module.py
├── summary_module.py
├── learning_path.py
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── docs/
    ├── 01-prerequisites/
    │   └── README.md
    ├── 02-project-workflow/
    │   └── README.md
    ├── 03-model-selection/
    │   └── README.md
    ├── 04-module-implementation/
    │   └── README.md
    ├── 05-backend-api/
    │   └── README.md
    ├── 06-frontend-interface/
    │   └── README.md
    ├── 07-live-integration/
    │   └── README.md
    ├── 08-run-locally/
    │   └── README.md
    ├── 09-functional-testing/
    │   └── README.md
    └── 10-conclusion/
        └── README.md
```

**Note:** The `.env` file is intentionally not included in the repository because it contains the private Gemini API key.

## API Endpoints

| Method | Endpoint                 | Purpose                    |
| ------ | ------------------------ | -------------------------- |
| GET    | `/`                      | EduGenie web interface     |
| GET    | `/health`                | Application health check   |
| POST   | `/qa`                    | Question and Answer        |
| POST   | `/explain`               | Concept Explanation        |
| POST   | `/quiz`                  | Quiz Generation            |
| POST   | `/summarize`             | Content Summarization      |
| POST   | `/learn/recommendations` | Personalized Learning Path |

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/thamijudeen1706/EduGenie-Gemini-Learning-Assistant.git
cd EduGenie-Gemini-Learning-Assistant
```

### 2. Create a Virtual Environment

Windows:

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure the Gemini API Key

Create a `.env` file in the project root.

Add:

```text
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

Replace `YOUR_GEMINI_API_KEY` with your own Gemini API key.

Never upload the real `.env` file or API key to GitHub.

### 6. Start the Application

```bash
python -m uvicorn main:app --reload
```

### 7. Open EduGenie

Open the following address in your browser:

```text
http://127.0.0.1:8000/
```

## Running the Application

After starting the Uvicorn server, EduGenie provides:

- Web interface
- FastAPI backend
- Static CSS files
- AI-powered learning features
- Local concept explanation model

The application runs locally through the FastAPI and Uvicorn development server.

## Development Milestones

EduGenie was developed through four major milestones.

### Milestone 1 — Model Selection and Architecture

Selected the AI models and assigned responsibilities to each model.

### Milestone 2 — Core Functionalities Development

Implemented the five major learning features:

- Question and Answer
- Concept Explanation
- Quiz Generation
- Content Summarization
- Personalized Learning Path

### Milestone 3 — Frontend Development

Built the web interface and connected the frontend with the FastAPI backend.

### Milestone 4 — Testing and Local Execution

Ran the application locally using Uvicorn and functionally tested the major learning features.

## Functional Testing

The following features were tested through the local web application:

| Feature                    | Result |
| -------------------------- | ------ |
| Question and Answer        | Passed |
| Concept Explanation        | Passed |
| Quiz Generation            | Passed |
| Content Summarization      | Passed |
| Personalized Learning Path | Passed |

## Documentation

Detailed project documentation is available inside the `docs/` directory.

| Document                   | Description                      |
| -------------------------- | -------------------------------- |
| 01 — Pre-requisites        | Environment and dependency setup |
| 02 — Project Workflow      | Development workflow             |
| 03 — Model Selection       | AI model architecture            |
| 04 — Module Implementation | Core AI modules                  |
| 05 — Backend API           | FastAPI backend                  |
| 06 — Frontend Interface    | Web interface                    |
| 07 — Live Integration      | Frontend-backend integration     |
| 08 — Run Locally           | Local execution                  |
| 09 — Functional Testing    | Feature testing                  |
| 10 — Conclusion            | Final project summary            |

## Security

The Gemini API key is stored in the local `.env` file.

The `.env` file is excluded from Git tracking using `.gitignore`.

The repository should never contain:

- Gemini API keys
- Passwords
- Access tokens
- Private credentials
- Other sensitive information

## Project Status

**Completed**

EduGenie has completed:

- AI model selection
- Core feature implementation
- FastAPI backend
- Frontend development
- Frontend-backend integration
- Local execution
- Functional testing
- Project documentation

The project is ready for GitHub publication, demonstration, and SkillWallet submission.

## Author

**THAMIJUDEEN M**

B.Tech Information Technology  
III Year

## License

This project was developed as an educational project for learning, demonstration, and SkillWallet submission purposes.
