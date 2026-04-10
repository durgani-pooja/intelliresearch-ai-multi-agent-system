import os
from groq import Groq

class SummarizerAgent:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def process(self, text):
        response = self.client.chat.completions.create(
            messages=[{"role": "system", "content": "You are a Summarization Agent. Distill the following text into a 3-paragraph executive summary."},
                      {"role": "user", "content": text[:10000]}],
            model="llama-3.3-70b-versatile", # Using the latest working model
        )
        return response.choices[0].message.content