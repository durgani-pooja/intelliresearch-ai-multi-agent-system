import os
from groq import Groq

class ReportAgent:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def generate(self, summary, insights):
        response = self.client.chat.completions.create(
            messages=[{"role": "system", "content": "Format the following summary and insights into a professional markdown report with headers and bullet points."},
                      {"role": "user", "content": f"Summary: {summary}\nInsights: {insights}"}],
            model="llama-3.1-8b-instant",
        )
        return response.choices[0].message.content