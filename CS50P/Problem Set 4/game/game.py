import random

def prompt():
    while True:
        try:
            range = int(input("Level: "))
            if range < 0:
                pass
            else:
                return range
        except ValueError:
            pass

def generator(range):
    number = random.randint(1, range)
    return number

def guesser(number):
    while True:
        try:
            guess = int(input("Guess: "))
            if guess < 1:
                pass
            else:
                if guess == number:
                    print("Just right!")
                    break
                elif guess < number:
                    print("Too small!")
                    pass
                elif guess > number:
                    print("Too large!")
                    pass
        except ValueError:
            pass

range = prompt()
number = generator(range)
guesser(number)
