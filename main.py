from fastapi import FastAPI, Request
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse

from models.schemas import PromptRequest, QueryRequest, LLMResponse, SearchResponse
from services.llm_service import call_llm
from services.semantic_search import search

import logging

limiter = Limiter(key_func=get_remote_address)
app = FastAPI(title="Local LLM Service (Ollama)")
app.state.limiter = limiter


@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    # Using function params as they are required to match function signature. Logging to remove linter warning
    logging.warning(f"Rate limit hit from {request.client.host}: {exc}")
    return JSONResponse(
        status_code=429,
        content={"detail": "Rate limit exceeded"}
    )


@app.post("/generate", response_model=LLMResponse)
@limiter.limit("5/minute")
def generate_text(request: PromptRequest):
    response, latency = call_llm(request.prompt)

    return LLMResponse(
        response=response,
        latency_ms=latency
    )

# Sample documents for demo
documents = [
    "How to use embeddings in AI",
    "FastAPI tutorial",
    "CAP theorem explained",
    "Vector search and semantic search",
]


@app.post("/search", response_model=SearchResponse)
@limiter.limit("10/minute")
def semantic_search_endpoint(query_request: QueryRequest):
    results = search(query_request.query, documents, top_k=3)
    return SearchResponse(results=results)
