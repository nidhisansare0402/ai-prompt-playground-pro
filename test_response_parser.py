from app.response_parser import parse_response

print("TEXT")
print(parse_response("Hello World", "text"))

print("\n")

print("MARKDOWN")
print(parse_response("# Python", "markdown"))

print("\n")

print("JSON")

json_string = '''
{
    "questions":[
        "What is SQL?",
        "Explain JOIN."
    ]
}
'''
print(type(json_string))
data = parse_response(json_string, "json")

print(data)

print(type(data))