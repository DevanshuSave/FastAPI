# FastAPI Project with Ollama Integration

## Description
A FastAPI project demonstrating integration with Ollama, an open-source lightweight large language model (LLM) runtime. This application allows you to interact with Ollama models via FastAPI endpoints, making it easy to build AI-powered APIs.

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- <a href="https://ollama.ai/">Ollama</a> installed locally

### 1. Clone the Repository
```bash
git clone https://github.com/DevanshuSave/FastAPI.git
cd FastAPI
```

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 3. Install and Run Ollama
Follow the official Ollama installation guide for your OS from <a href="https://ollama.ai/download">https://ollama.ai/download</a>

Start Ollama on your local machine:
```bash
ollama serve
```

### 4. Run the FastAPI Application
```bash
uvicorn main:app --reload
```

The FastAPI app will be available at http://127.0.0.1:8000.

### 5. Test the API
Open your browser and navigate to http://127.0.0.1:8000/docs to access the interactive API documentation and try out endpoints.

---

Feel free to update this README with additional integration, usage, and deployment details as your project evolves.
