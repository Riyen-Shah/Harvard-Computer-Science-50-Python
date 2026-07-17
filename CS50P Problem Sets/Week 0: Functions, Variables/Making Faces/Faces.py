def main():
    emoji = input("What would you like to say today? ")
    print(convert(emoji))


def convert(emoji):
    emoji = emoji.replace(":(", "🙁").replace(":)", "🙂")
    return emoji

main()
