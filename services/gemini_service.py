from google import genai
from config.settings import GEMINI_API_KEY, MODEL_NAME

# Initialize the Gemini client with the API key
client = genai.Client(api_key = GEMINI_API_KEY)

def generate_response(prompt: str) -> str:
    """
    Send user prompt to the Gemini API and return the generated response.
    """
    response = client.models.generate_content(
        model = MODEL_NAME,
        contents = prompt
    )
    return response.text