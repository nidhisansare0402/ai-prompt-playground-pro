# from google import genai
# from config.settings import GEMINI_API_KEY

# client = genai.Client(api_key=GEMINI_API_KEY)

# response = client.models.generate_content(
#     model="gemini-2.0-flash",
#     contents="Say only the word Hello."
# )

# print(response.text)

# from config.settings import GEMINI_API_KEY
# print(GEMINI_API_KEY[:10])

# from google import genai

# API_KEY = "PASTE_YOUR_API_KEY"

# client = genai.Client(api_key=API_KEY)

# response = client.models.generate_content(
#     model="gemini-2.5-flash",
#     contents="Say Hello"
# )

# print(response.text)

from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

print(api_key[:10])      # first few chars
print(api_key[-6:])      # last few chars

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-flash-latest",
    contents="Hello"
)

print(response.text)