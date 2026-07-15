from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

try:
    models = client.models.list()

    print("Connected successfully!")

    for model in models:
        print(model.name)

except Exception as e:
    print(e)