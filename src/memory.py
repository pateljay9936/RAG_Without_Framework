import uuid
from datetime import datetime

conversations = {}

def create_session():
    session_id = str(uuid.uuid4())
    conversations[session_id] = []
    return session_id

def add_message(session_id, role, content):
    conversations[session_id].append({
        "role": role,
        "content": content,
        "timestamp": datetime.now().isoformat()
    })

def get_conversation_history(session_id, max_messages=5):
    return conversations.get(session_id, [])[-max_messages:]

def format_history_for_prompt(session_id, max_messages=5):
    history = get_conversation_history(session_id, max_messages)
    return "\n".join(
        f"{'Human' if m['role'] == 'user' else 'Assistant'}: {m['content']}"
        for m in history
    )
