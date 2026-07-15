from services.gemini_service import generate_response
from app.prompt_builder import build_prompt
from app.response_parser import parse_response
import json
from config.settings import MODEL_NAME
from services.history_service import HistoryService
from services.template_service import TemplateService

history_service = HistoryService()
template_service = TemplateService()

def get_response_format():
    """
    Display the available response formats and return the selected option.
    """
    print("\nSelect the response format:")
    print("1. Text")
    print("2. Markdown")
    print("3. JSON")

    choice = input("Enter your choice (1-3): ")

    formats = {
        "1": "text",
        "2": "markdown",
        "3": "json"
    }
    return formats.get(choice)

def process_prompt(user_prompt):
    """
    Process a prompt using the existing AI pipeline.
    """
    response_format = get_response_format()

    final_prompt = build_prompt(
        user_prompt,
        response_format
    )
    print("\nGenerating response...")

    try:

        raw_response = generate_response(final_prompt)

        parsed_response = parse_response(
            raw_response,
            response_format
        )

        print("\nGenerated Response\n")

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
            print(f"\nFailed to save history: {e}")

    except RuntimeError as e:
        print("\nGemini API Error")
        print(e)

    except ValueError as e:
        print("\nResponse Parsing Error")
        print(e)

    except Exception as e:
        print("\nUnexpected Error")
        print(e)

def normal_prompt():
    user_prompt = input("\nEnter your prompt: ")
    process_prompt(user_prompt)

def create_template():
    print("\nCreate New Template")
    name = input("Template Name: ")
    prompt = input("Template Prompt: ")

    template_service.save_template({
        "name": name,
        "prompt": prompt
    })

    print("\nTemplate created successfully.")


def view_templates():
    templates = template_service.list_templates()

    if not templates:
        print("\nNo templates available.")
        return

    print("\nAvailable Templates\n")

    for template in templates:
        print(f'{template["id"]}. {template["name"]}')


def delete_template():
    templates = template_service.list_templates()

    if not templates:
        print("\nNo templates available.")
        return

    view_templates()
    template_id = int(input("\nEnter Template ID: "))
    template_service.delete_template(template_id)

    deleted = template_service.delete_template(template_id)
    if deleted:
        print("\nTemplate deleted successfully.")
    else:
        print("\nTemplate not found.")


def use_template():
    templates = template_service.list_templates()

    if not templates:
        print("\nNo templates available.")
        return

    view_templates()
    template_id = int(input("\nEnter Template ID: "))
    template = template_service.get_template(template_id)

    if template is None:
        print("\nInvalid Template ID.")
        return

    process_prompt(template["prompt"])


def main():
    while True:

        print("\n" + "=" * 50)
        print("AI Prompt Playground Pro")
        print("=" * 50)
        print("1. Normal Prompt")
        print("2. Use Prompt Template")
        print("3. Create Prompt Template")
        print("4. View Templates")
        print("5. Delete Prompt Template")
        print("0. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            normal_prompt()

        elif choice == "2":
            use_template()

        elif choice == "3":
            create_template()

        elif choice == "4":
            view_templates()

        elif choice == "5":
            delete_template()

        elif choice == "0":
            print("\nThank you for using AI Prompt Playground Pro.")
            break

        else:
            print("\nInvalid choice.")


if __name__ == "__main__":
    main()