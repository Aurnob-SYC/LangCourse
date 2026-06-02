from __future__ import annotations

import hashlib
import re

try:
    import chromadb
except ImportError:  # pragma: no cover - friendly runtime hint
    chromadb = None


def embed_text(text: str, dim: int = 8) -> list[float]:
    """Tiny deterministic embedding helper for a simple ChromaDB demo."""
    vector = [0.0] * dim
    for token in re.findall(r"\w+", text.lower()):
        bucket = hashlib.sha1(token.encode("utf-8")).digest()[0] % dim
        vector[bucket] += 1.0
    return vector


def main() -> None:
    if chromadb is None:
        print("Install chromadb first: uv add chromadb")
        return

    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_or_create_collection(name="notes")

    if collection.count() == 0:
        docs = [
            "ChromaDB stores embeddings and metadata.",
            "Python is a good fit for quick vector database demos.",
            "Cats and dogs are common example topics.",
        ]
        collection.add(
            ids=["doc-1", "doc-2", "doc-3"],
            documents=docs,
            embeddings=[embed_text(doc) for doc in docs],
        )

    result = collection.query(
        query_embeddings=[embed_text("How do I use a vector database in Python?")],
        n_results=2,
    )

    print("Top matches:")
    for doc_id, document in zip(result["ids"][0], result["documents"][0]):
        print(f"- {doc_id}: {document}")


if __name__ == "__main__":
    main()
