from pydantic import BaseModel
from typing import List


class PromptRequest(BaseModel):
    prompt: str


class LLMResponse(BaseModel):
    response: str
    latency_ms: float


class QueryRequest(BaseModel):
    query: str


class SearchResponse(BaseModel):
    results: List[str]

