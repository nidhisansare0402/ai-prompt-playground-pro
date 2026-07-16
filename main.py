import json
from app.ai_processor import process_prompt

def get_response_format():
    """
    Display the available response formats and return the selected option.
    """
    formats = {
        "1": "text",
        "2": "markdown",
        "3": "json"
    }

    while True:
        print("\nSelect the response format:")
        print("1. Text")
        print("2. Markdown")
        print("3. JSON")

        choice = input("Enter your choice (1-3): ")

        if choice in formats:
            return formats[choice]

        print("\nInvalid choice. Please try again.")

def main():
    print("=" * 50)
    print("AI Prompt Playground Pro (CLI)")
    print("=" * 50)

    while True:
        user_prompt = input("\nEnter your prompt (or type 'exit' to quit): ")

        if user_prompt.lower() == "exit":
            print("\nGoodbye!")
            break

        response_format = get_response_format()

        print("\nGenerating response...\n")

        try:
            parsed_response = process_prompt(
                user_prompt,
                response_format
            )

            print("\nGenerated Response:\n")

            if response_format == "json":
                print(
                    json.dumps(
                        parsed_response,
                        indent=4,
                        ensure_ascii=False
                    )
                )
            else:
                print(parsed_response)

        except RuntimeError as e:
            print("Gemini API Error")
            print(e)

        except ValueError as e:
            print("Response Parsing Error")
            print(e)

        except Exception as e:
            print("\nUnexpected Error")
            print(e)

if __name__ == "__main__":
    main()