# To-Do List API

A simple **To-Do List API** built with **FastAPI** and **SQLite**, fully containerized with **Docker** and integrated with **Jenkins CI/CD**.

---

## Features

- Create, Read, Update, Delete tasks
- Task attributes: title, description, completed
- Interactive API docs via Swagger UI
- Containerized with Docker
- CI/CD with Jenkins:
  - Linting with flake8
  - Unit tests with pytest
  - Docker image build and push to Docker Hub

---

## Project Structure
```bash
todo_app/
├── app/
│ ├── main.py # FastAPI app entrypoint
│ ├── models.py # SQLAlchemy models
│ ├── schemas.py # Pydantic schemas
│ ├── crud.py # DB operations
│ ├── database.py # DB connection
│ └── routes/tasks.py # Task API routes
├── tests/
│ └── test_tasks.py # Unit tests
├── requirements.txt # Python dependencies
├── Dockerfile # Docker build instructions
├── Jenkinsfile # Jenkins CI/CD pipeline
└── README.md
```


---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Shuvra-458/To-Do_List_CI-CD.git
cd To-Do_List_CI-CD
```

### 2. Create a Python virtual environment
```bash
# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run the application locally
```bash
uvicorn app.main:app --reload
```

- Open your browser: http://localhost:8000/docs
- You’ll see the interactive Swagger UI for testing API endpoints.
