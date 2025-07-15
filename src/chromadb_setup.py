import chromadb
from chromadb.utils import embedding_functions

client = chromadb.PersistentClient(path="chroma_db")

embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

collection = client.get_or_create_collection(
    name="documents_collection",
    embedding_function=embedding_fn
)
