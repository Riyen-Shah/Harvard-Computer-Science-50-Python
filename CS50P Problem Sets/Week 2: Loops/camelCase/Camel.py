CamelCase = input("Camel Case: ")
snake_case = ""
for character in CamelCase:
    if character.isupper():
        snake_case += "_" + character.lower()
    else:
        snake_case += character
print(f"snake_case: {snake_case}")
