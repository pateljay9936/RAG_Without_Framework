def semantic_search(collection, query: str, n_results: int = 3):
    return collection.query(query_texts=[query], n_results=n_results)

def get_context_with_sources(results):
    context = "\n\n".join(results["documents"][0])
    sources = [f"{m['source']} (chunk {m['chunk']})" for m in results["metadatas"][0]]
    return context, sources
