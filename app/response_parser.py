# parse the response from the Gemini API and return a structured output

import json

def clean_json_response(response: str) -> str:
    """
    Remove common Markdown formatting from Gemini JSON responses.
    """
    response = response.strip()

    if response.startswith("```json"):
        response = response.replace("```json", "", 1)

    if response.startswith("```"):
        # 1 tells that only the first occurrence of ``` will be replaced by an empty string
        response = response.replace("```", "", 1)

    if response.endswith("```"):
        response = response[:-3]

    return response.strip()

def parse_response(response: str, response_format: str):
    """
    Parse the LLM response based on the desired response format (text, JSON, markdown).
    """
    response_format = response_format.lower()

    if response_format == "text":
        return response

    elif response_format == "markdown":
        return response

    elif response_format == "json":
        cleaned_response = clean_json_response(response)
        try:
            return json.loads(cleaned_response)
        
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON response from the Gemini API.")

    else:
        raise ValueError("Invalid response format. Choose from 'text', 'markdown', or 'json'.")