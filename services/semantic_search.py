from numpy import dot
from numpy.linalg import norm
from services.embeddings_cache import get_cached_embedding

def cosine_similarity(vec1, vec2):
    norm1 = norm(vec1)
    norm2 = norm(vec2)
    if norm1 == 0 or norm2 == 0:
        return 0.0
    return dot(vec1, vec2) / (norm1 * norm2)

def search(query: str, documents: list[str], top_k: int = 3):
    query_emb = get_cached_embedding(query)
    doc_embeddings = [get_cached_embedding(doc) for doc in documents]

    scores = [cosine_similarity(query_emb, emb) for emb in doc_embeddings]
    ranked_docs = sorted(zip(documents, scores), key=lambda x: x[1], reverse=True)
    return [doc for doc, _ in ranked_docs[:top_k]]
