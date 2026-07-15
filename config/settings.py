import os
from dotenv import load_dotenv

load_dotenv()

print("Loaded key:", os.getenv("GEMINI_API_KEY"))

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "gemini-flash-latest")