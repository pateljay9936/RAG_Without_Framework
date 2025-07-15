from openai import OpenAI
client = OpenAI()

def contextualize_query(query: str, conversation_history: str):
    contextualize_prompt = "Convert the question below into a standalone version using the conversation history."

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": contextualize_prompt},
            {"role": "user", "content": f"Chat history:\n{conversation_history}\n\nQuestion:\n{query}"}
        ]
    )
    return response.choices[0].message.content
