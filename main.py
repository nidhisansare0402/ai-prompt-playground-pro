from services.gemini_service import generate_response

def main():
    """
    Main function to run the application.
    """
    print("=" * 50)
    print("AI Prompt Playground Pro")
    print("=" * 50)

    prompt = input("Enter your prompt: ")
    print("\nGenerating response...\n")
    response = generate_response(prompt)
    print("Generated Response:", response)

if __name__ == "__main__":
    main()