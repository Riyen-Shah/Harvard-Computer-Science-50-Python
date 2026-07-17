def name():
    Name = []
    while True:
        try:
            Input = input("Name: ")
            Name.append(Input)
        except EOFError:
            print("\n")
            return Name

def Output(Name):
    Repetitions = len(Name)
    index = 0
    if Repetitions == 1:
        output = (f"Adieu, adieu, to {Name[0]}")
        return output
    elif Repetitions == 2:
        output = (f"Adieu, adieu, to {Name[0]} and {Name[1]}")
        return output
    else:
        output = "Adieu, adieu, to "
        for i in range(Repetitions - 1):
            output =  output + Name[index] + ", "
            index += 1
        output = output + "and " + Name[index]
        return output

Name = name()
output = Output(Name)
print(output)


