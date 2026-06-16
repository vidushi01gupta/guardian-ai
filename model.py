import os
import requests
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

OLLAMA_URL = os.getenv(
    "OLLAMA_URL",
    "http://localhost:11434/api/generate"
)

MODEL = os.getenv(
    "OLLAMA_MODEL",
    "mistral"
)


def get_ai_response(message):
    print("MODEL.PY FUNCTION CALLED")

    prompt = f"""
You are Guardian AI, a smart and helpful AI voice assistant.

Rules:
- Give clear and accurate answers.
- Keep responses concise.
- Speak naturally like ChatGPT.
- Answer educational and technical questions properly.

User: {message}

Assistant:
"""

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.7,
            "num_predict": 150
        }
    }

    try:

        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=60
        )

        


        print("STATUS CODE:", response.status_code)
        print("RAW RESPONSE:", response.text)

        if response.status_code == 200:
            return response.json()["response"].strip()

        return f"AI model not responding. Status: {response.status_code}"

    except Exception as e:

        print("OLLAMA ERROR:", e)

        return "Unable to connect to AI model."