import os
from groq import Groq

class QAAgent:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def answer(self, question, context):
        response = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a Question Answering Agent. Answer the user's specific question based ONLY on the provided document text."},
                {"role": "user", "content": f"Question: {question}\n\nDocument Context: {context[:8000]}"}
            ],
            model="llama-3.3-70b-versatile",
        )
        return response.choices[0].message.content