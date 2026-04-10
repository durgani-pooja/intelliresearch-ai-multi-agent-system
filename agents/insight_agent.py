import os
from groq import Groq

class InsightAgent:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def process(self, summary, text):
        # Existing insight logic...
        response = self.client.chat.completions.create(
            messages=[{"role": "system", "content": "Extract 5 high-level technical findings."},
                      {"role": "user", "content": f"Context: {text[:5000]}"}],
            model="llama-3.3-70b-versatile",
        )
        return response.choices[0].message.content

    def process_code(self, text):
        # NEW FEATURE: Specifically looks for code snippets in the PDF
        response = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": "Search the document for code snippets, algorithms, or logic. If found, explain them in very simple 'plain English' for a beginner. If no code exists, summarize the primary logical steps of the document."},
                {"role": "user", "content": f"Analyze code/logic here: {text[:8000]}"}
            ],
            model="llama-3.3-70b-versatile",
        )
        return response.choices[0].message.content