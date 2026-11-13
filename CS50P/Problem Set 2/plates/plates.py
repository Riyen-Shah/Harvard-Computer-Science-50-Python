def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    letters = 0
    for character in s:
        letters += 1
    if letters < 2 or letters > 6:
        return False
    else:
        if s.isalnum():
            if s[0:2].isalpha():
                if letters > 2:
                    if s.isalpha():
                        return True
                    else:
                        first_digit = next(c for c in s if c.isdigit())
                        first_digit_index = s.index(first_digit)
                        after_digit = s[first_digit_index+1:]
                        if first_digit == "0":
                            return False
                        else:
                            if any(a.isalpha() for a in after_digit):
                                return False
                            else:
                                return True
                else:
                    return True
            else:
                return False
        else:
            return False


main()
