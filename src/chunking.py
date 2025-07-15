def split_text(text: str, chunk_size: int = 500):
    sentences = text.replace('\n', ' ').split('. ')
    chunks, current_chunk = [], []
    current_size = 0

    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue
        if not sentence.endswith('.'):
            sentence += '.'
        if current_size + len(sentence) > chunk_size and current_chunk:
            chunks.append(' '.join(current_chunk))
            current_chunk, current_size = [sentence], len(sentence)
        else:
            current_chunk.append(sentence)
            current_size += len(sentence)

    if current_chunk:
        chunks.append(' '.join(current_chunk))
    return chunks
