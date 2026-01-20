import time
import requests
from config import OLLAMA_BASE_URL, OLLAMA_MODEL

MAX_RETRIES = 5


def call_llm(prompt: str) -> tuple[str, float]:
    for attempt in range(MAX_RETRIES):
        try:
            start = time.time()

            payload = {
                "model": OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False
            }

            response = requests.post(
                f"{OLLAMA_BASE_URL}/api/generate",
                json=payload,
                timeout=30  # seconds
            )
            response.raise_for_status()

            data = response.json()
            latency_ms = (time.time() - start) * 1000

            return data["response"], latency_ms

        except requests.RequestException as e:
            if attempt == MAX_RETRIES - 1:
                raise e
            sleep_time = 2 ** attempt
            time.sleep(sleep_time)
