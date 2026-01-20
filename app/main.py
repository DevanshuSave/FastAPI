from fastapi import FastAPI
from app.models.schemas import PromptRequest, LLMResponse
from app.services.llm_service import call_llm

app = FastAPI(title="Local LLM Service (Ollama)")

@app.post("/generate", response_model=LLMResponse)
def generate_text(request: PromptRequest):
    response, latency = call_llm(request.prompt)

    return LLMResponse(
        response=response,
        latency_ms=latency
    )
