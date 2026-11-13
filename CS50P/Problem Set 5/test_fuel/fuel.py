def main():
    Fraction = input("Fraction: ")
    Percentage = convert(Fraction)
    Output = gauge(Percentage)
    print(f"{Output}")

def convert(fraction):
    if "/" not in fraction:
        raise ValueError
    else:
        try:
            Numerator, Denominator = map(int, fraction.split("/"))
        except ValueError:
            raise ValueError
        else:
            if Denominator <= 0:
                raise ZeroDivisionError
            elif Numerator > Denominator or Numerator < 0 or Denominator < 0:
                raise ValueError
            else:
                try:
                    Decimal = (Numerator/Denominator)
                except ZeroDivisionError:
                    raise ZeroDivisionError
                else:
                    Percent = round(Decimal*100)
                    return Percent

def gauge(percent):
    if percent >= 99:
        return "F"
    elif percent <= 1:
        return "E"
    else:
        percent = str(f"{percent}%")
        return percent

if __name__ == "__main__":
    main()
