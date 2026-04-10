from openai import OpenAI
import os

def run_comparison_agent(text1: str, text2: str, name1: str = "Document 1", name2: str = "Document 2") -> str:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    text1_short = text1[:5000]
    text2_short = text2[:5000]
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert document comparison analyst. "
                    "Compare two documents and format your response like this:\n\n"
                    "SIMILARITIES:\n• [similarity]\n\n"
                    "KEY DIFFERENCES:\n• [difference]\n\n"
                    "UNIQUE CONTRIBUTIONS OF DOCUMENT 1:\n• [point]\n\n"
                    "UNIQUE CONTRIBUTIONS OF DOCUMENT 2:\n• [point]\n\n"
                    "OVERALL VERDICT:\n[2-3 sentences]"
                )
            },
            {
                "role": "user",
                "content": f"Compare these two documents:\n\n=== {name1} ===\n{text1_short}\n\n=== {name2} ===\n{text2_short}"
            }
        ],
        max_tokens=800
    )
    return response.choices[0].message.content.strip()