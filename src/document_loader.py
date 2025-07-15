import docx
import PyPDF2
import os

def read_text_file(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def read_pdf_file(file_path: str):
    text = ""
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

def read_docx_file(file_path: str):
    doc = docx.Document(file_path)
    return "\n".join([p.text for p in doc.paragraphs])

def read_document(file_path: str):
    _, ext = os.path.splitext(file_path.lower())
    if ext == '.txt':
        return read_text_file(file_path)
    elif ext == '.pdf':
        return read_pdf_file(file_path)
    elif ext == '.docx':
        return read_docx_file(file_path)
    else:
        raise ValueError(f"Unsupported file format: {ext}")
