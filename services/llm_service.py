import time
import requests
from config import OLLAMA_BASE_URL, OLLAMA_MODEL

def call_llm(prompt: str) -> tuple[str, float]:
    start = time.time()

    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(
        f"{OLLAMA_BASE_URL}/api/generate",
        json=payload,
        timeout=60
    )
    response.raise_for_status()

    data = response.json()
    latency_ms = (time.time() - start) * 1000

    return data["response"], latency_ms
