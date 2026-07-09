from app.prompt_builder import build_prompt

print("Text\n")
print(build_prompt("What is the capital of India?", "text"))

print("=" * 50)

print("Markdown\n")
print(build_prompt("Explain SQL joins", "markdown"))

print("=" * 50)

print("JSON\n")
print(build_prompt("Explain Python decorators", "json"))