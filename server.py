from fastapi import FastAPI
import requests
import os

app = FastAPI()

GEMINI_KEY = os.getenv("GEMINI_API_KEY")

@app.post("/generate")
async def generate(data: dict):
    prompt = data["prompt"]

    r = requests.post(
        "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent",
        params={"key": GEMINI_KEY},
        json={
            "contents": [{
                "parts": [{"text": prompt}]
            }]
        }
    )

    return r.json()
