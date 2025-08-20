from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key= os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)


def summarize(text):
    if not text or not text.strip():
        return "No valid transcript text available for summarization."

    prompt = f"Please summarize the following in detail:\n\n{text}"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=500
    )
    return response.choices[0].message.content.strip()


