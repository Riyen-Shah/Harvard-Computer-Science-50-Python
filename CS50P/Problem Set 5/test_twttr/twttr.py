def main():
    full = input("Input: ")
    new_word = shorten(full)
    print(f"Output: {new_word}")

def shorten(word):
    shortened = ""
    for character in word:
        if character == "A" or character == "a" or character == "E" or character == "e" or character == "I" or character == "i" or character == "O" or character == "o" or character == "U" or character == "u":
            shortened += ""
        else:
            shortened += character
    return shortened


if __name__ == "__main__":
    main()
