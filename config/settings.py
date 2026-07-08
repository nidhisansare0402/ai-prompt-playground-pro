import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read the Gemini API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Default model for the application
MODEL_NAME = "gemini-2.5-flash"