from tabulate import tabulate
import sys
import csv

def name():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        file_name = sys.argv[1]
        if file_name[-4:] != ".csv":
            sys.exit("Not a CSV file")
        else:
            return file_name

def converter(file_name):
    try:
        with open(file_name) as file:
            reader = csv.reader(file)
            count = 1
            for row in reader:
                if count == 1:
                    first_row =[row[0],row[1],row[2]]
                    count += 1
                else:
                    rows = [row[0],row[1],row[2]]
                    file_lines.append(rows)
            return first_row
    except FileNotFoundError:
        sys.exit("File does not exist")

file_lines = []
file_name = name()
header = converter(file_name)
print(tabulate(file_lines, header, tablefmt="grid"))
