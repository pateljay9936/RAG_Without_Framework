import os
from document_loader import read_document
from chunking import split_text

def process_document(file_path: str):
    content = read_document(file_path)
    chunks = split_text(content)
    file_name = os.path.basename(file_path)
    ids = [f"{file_name}_chunk_{i}" for i in range(len(chunks))]
    metadatas = [{"source": file_name, "chunk": i} for i in range(len(chunks))]
    return ids, chunks, metadatas

def add_to_collection(collection, ids, texts, metadatas):
    if not texts:
        return
    for i in range(0, len(texts), 100):
        collection.add(
            documents=texts[i:i+100],
            metadatas=metadatas[i:i+100],
            ids=ids[i:i+100]
        )

def process_and_add_documents(collection, folder_path: str):
    for file in os.listdir(folder_path):
        path = os.path.join(folder_path, file)
        if os.path.isfile(path):
            ids, texts, metadatas = process_document(path)
            add_to_collection(collection, ids, texts, metadatas)
