import sys
LOC = 0

try:
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        file_name = sys.argv[1]
        with open(file_name) as file:
            if file_name[-3:] != ".py":
                sys.exit("Not a Python file")
            else:
                for line in file:
                    if line.strip() == "" or line.strip().startswith("#"):
                        pass
                    else:
                        LOC += 1

except FileNotFoundError:
    sys.exit("File does not exist")

print(LOC)
