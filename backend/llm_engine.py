import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

# Load API Key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemma-3-12b-it")


def generate_response(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"[Error generating response: {e}]"
