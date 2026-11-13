Greeting = input("Greeting:").lower().strip()

if Greeting[0:5] == "hello":
    print("$0")
elif Greeting [0:1] == "h":
    print("$20")
else:
    print("$100")
