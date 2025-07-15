from memory import format_history_for_prompt, add_message
from contextualizer import contextualize_query
from semantic_search import semantic_search, get_context_with_sources
from openai_integration import generate_response

def conversational_rag_query(collection, query: str, session_id: str, n_chunks: int = 3):
    history = format_history_for_prompt(session_id)
    standalone_query = contextualize_query(query, history)
    results = semantic_search(collection, standalone_query, n_chunks)
    context, sources = get_context_with_sources(results)
    response = generate_response(standalone_query, context, history)

    add_message(session_id, "user", standalone_query)
    add_message(session_id, "assistant", response)

    return response, sources
