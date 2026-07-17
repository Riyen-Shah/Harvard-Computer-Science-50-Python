def main():
    Percentage = level()
    if Percentage == "F" or Percentage == "E":
        print(f"{Percentage}")
    else:
        print(f"{Percentage}%")

def level():
    Percent = round(percentage())
    if Percent >= 99:
        Output = "F"
        return Output
    elif Percent <= 1:
        Output = "E"
        return Output
    else:
        Output = int(Percent)
        return Output

def percentage():
    while True:
        Fraction = input("Fraction: ")
        try:
            Numerator, Denominator = map(int, Fraction.split("/"))
        except ValueError:
            pass
        else:
            if Numerator > Denominator or Numerator < 0 or Denominator < 0:
                pass
            else:
                try:
                    Decimal = (Numerator/Denominator)
                except ZeroDivisionError:
                    pass
                else:
                    Percent = (Decimal*100)
                    return Percent

main()
