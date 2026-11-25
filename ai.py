
import os
from pathlib import Path

import requests
from dotenv import load_dotenv


# Load .env from the same folder as ai.py
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")


# Get NVIDIA API key
NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")

if not NVIDIA_API_KEY:
    raise ValueError(
        "NVIDIA_API_KEY is missing in .env"
    )


# NVIDIA model
MODEL = os.getenv(
    "MODEL",
    "nvidia/nemotron-3.5-lightning-30b-a3b"
)


def ask_ai(question, pdf_text):
    """
    Ask NVIDIA AI a question using the
    extracted PDF text.
    """

    prompt = f"""
You are an AI Study Assistant.

Answer the student's question using ONLY
the information present in the uploaded PDF.

If the answer cannot be found in the PDF,
say:

"The answer is not available in the uploaded PDF."

Give a clear and simple answer suitable
for a college student.

==============================
PDF CONTENT
==============================

{pdf_text}

==============================
STUDENT QUESTION
==============================

{question}

==============================
ANSWER
==============================
"""

    url = (
        "https://integrate.api.nvidia.com"
        "/v1/chat/completions"
    )

    headers = {
        "Authorization": f"Bearer {NVIDIA_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.2,
        "max_tokens": 1500,
        "stream": False
    }

    response = requests.post(
        url,
        headers=headers,
        json=data,
        timeout=120
    )

    if response.status_code != 200:
        raise RuntimeError(
            f"NVIDIA API Error "
            f"[{response.status_code}]: "
            f"{response.text}"
        )

    result = response.json()

    return result["choices"][0]["message"]["content"]
