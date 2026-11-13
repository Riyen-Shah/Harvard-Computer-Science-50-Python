import random

def main():
    level = get_level()
    score = 0
    for i in range(10):
        integerX = generate_integer(level)
        integerY = generate_integer(level)
        actual_answer = integerX + integerY
        incorrect = 0
        while True:
            if incorrect == 3:
                print(f"{integerX} + {integerY} = {actual_answer}")
                break
            else:
                try:
                    user_answer = int(input(f"{integerX} + {integerY} = "))
                    if user_answer == actual_answer:
                        score += 1
                        break
                    else:
                        print("EEE")
                        incorrect += 1
                        pass
                except ValueError:
                    print("EEE")
                    incorrect += 1
                    pass
    print(f"Score : {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level < 1 or level > 3:
                pass
            else:
                return level
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        integer = random.randint(0, 9)
    elif level == 2:
        integer = random.randint(10, 99)
    elif level == 3:
        integer = random.randint(100, 999)
    return integer

if __name__ == "__main__":
    main()
