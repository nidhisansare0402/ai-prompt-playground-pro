from services.gemini_service import generate_response
from app.prompt_builder import build_prompt
from app.response_parser import parse_response
import json
from config.settings import MODEL_NAME
from services.history_service import HistoryService
from services.template_service import TemplateService

def get_response_format():
    """
    Display the available response formats and return the selected option.
    """
    print("Select the response format:")
    print("1. Text")
    print("2. Markdown")
    print("3. JSON")

    choice = input("Enter your choice (1-3): ")
    # I have added a dictionary to map the user's choice to the corresponding response format.
    formats = {
        "1": "text",
        "2": "markdown",
        "3": "json"
    }
    return formats.get(choice)    

def main():
    """
    Main function to run the application.
    """
    print("=" * 50)
    print("AI Prompt Playground Pro")
    print("=" * 50)

    history_service = HistoryService()

    user_prompt = input("Enter your prompt: ")
    response_format = get_response_format()

    # Build the final prompt based on user input and desired response format
    final_prompt = build_prompt(user_prompt, response_format)


    print("Generating response...")

    try:
        # Response from the Gemini API
        raw_response = generate_response(final_prompt)
        
        # Parse the response based on the selected format
        parsed_response = parse_response(
            raw_response,
            response_format
        )

        print("\nGenerated Response:\n")

        if response_format == "json":
            print(json.dumps(parsed_response, indent=4))
        else:
            print(parsed_response)

        record = {
        "user_prompt": user_prompt,
        "enhanced_prompt": final_prompt,
        "output_format": response_format,
        "model": MODEL_NAME,
        "response": parsed_response
        }

        try:
            history_service.save_history(record)
        except Exception as e:
            print(f"Failed to save history: {e}")

    except RuntimeError as e:
        print("\n" + "=" * 50)
        print("Gemini API Error")
        print("=" * 50)
        print(e)

    except ValueError as e:
        print("\n" + "=" * 50)
        print("Response Parsing Error")
        print("=" * 50)
        print(e)

    except Exception as e:
        print("\nUnexpected Error")
        print(e)

    

if __name__ == "__main__":
    main()