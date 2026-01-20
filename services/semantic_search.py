from numpy import dot
from numpy.linalg import norm
from services.embeddings_cache import get_cached_embedding

def cosine_similarity(vec1, vec2):
    return dot(vec1, vec2) / (norm(vec1) * norm(vec2))

def search(query: str, documents: list[str], top_k: int = 3):
    query_emb = get_cached_embedding(query)
    doc_embeddings = [get_cached_embedding(doc) for doc in documents]

    scores = [cosine_similarity(query_emb, emb) for emb in doc_embeddings]
    ranked_docs = sorted(zip(documents, scores), key=lambda x: x[1], reverse=True)
    return [doc for doc, _ in ranked_docs[:top_k]]
