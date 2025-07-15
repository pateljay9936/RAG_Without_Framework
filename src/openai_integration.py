from openai import OpenAI
import os

client = OpenAI()
os.environ["OPENAI_API_KEY"] = "your-api-key"

def get_prompt(context: str, conversation_history: str, query: str):
    return f"""Based on the following context and conversation history, provide a relevant response.
If the answer can't be found in the context, say: "I don't have enough information to answer."

Context:
{context}

Conversation:
{conversation_history}

Human: {query}
Assistant:"""

def generate_response(query, context, conversation_history=""):
    prompt = get_prompt(context, conversation_history, query)
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0,
        max_tokens=500
    )
    return response.choices[0].message.content
