full = input("Input: ")
shortened = ""
for character in full:
    if character == "A" or character == "a" or character == "E" or character == "e" or character == "I" or character == "i" or character == "O" or character == "o" or character == "U" or character == "u":
        shortened += ""
    else:
        shortened += character
print(f"Output: {shortened}")
