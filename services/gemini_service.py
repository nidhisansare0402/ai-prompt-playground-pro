from google import genai
from google.genai.errors import ClientError, ServerError
from config.settings import GEMINI_API_KEY, MODEL_NAME

# Initialize the Gemini client
client = genai.Client(api_key=GEMINI_API_KEY)


def generate_response(prompt: str) -> str:
    """
    Send the user prompt to Gemini API and return the generated response.
    """

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        return response.text

    except ClientError as e:
        raise RuntimeError(f"Gemini Client Error: {e}")

    except ServerError as e:
        raise RuntimeError(f"Gemini Server Error: {e}")

    except Exception as e:
        raise RuntimeError(f"Unexpected Error: {e}")