# Get response in multiple formats (text, JSON, markdown) based on user preference
# It takes the user prompt and the desired format as input, and adds instructions to the prompt to specify the output format. It then calls the Gemini API to generate the response and returns it in the requested format.

def build_prompt(user_prompt: str, response_format: str) -> str:
    """
    Build a prompt for the Gemini API based on user input and desired response format.
    """
    response_format = response_format.lower()

    if response_format == "text":
        return user_prompt
    
    elif response_format == "markdown":
        return (f"{user_prompt}\n\n"
                "Return the response in Markdown format."
        )

    elif response_format == "json":
        return (f"{user_prompt}\n\n"
                "Return only valid JSON format.\n"
                "Do not include explanations, markdown, or extra text.\n\n"
                "Use the following schema:"
                "{\n"
                '  "title": "",\n'
                '  "difficulty": "",\n'
                '  "questions": []\n'
                "}"
        )

    else:
        raise ValueError("Invalid response format. Choose from 'text', 'markdown', or 'json'.")