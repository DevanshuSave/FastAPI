import requests
from config import OLLAMA_BASE_URL


def generate_embedding(text: str):
    response = requests.post(
        f"{OLLAMA_BASE_URL}/api/embeddings",
        json={
            "model": "nomic-embed-text",
            "prompt": text
        },
        timeout=30
    )
    response.raise_for_status()
    return response.json()["embedding"]
