import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()  # load GROQ_API_KEY from .env

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_groq(prompt, model="llama-3.1-8b-instant", max_tokens=400):
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=max_tokens
    )
    return resp.choices[0].message.content
