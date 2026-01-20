from functools import lru_cache
from services.embedding_service import generate_embedding


@lru_cache(maxsize=100)
def get_cached_embedding(text: str):
    return generate_embedding(text)
