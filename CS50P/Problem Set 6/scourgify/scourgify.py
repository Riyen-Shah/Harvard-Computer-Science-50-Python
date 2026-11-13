import sys
import csv

def file_names():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        read_file = sys.argv[1]
        write_file = sys.argv[2]
        if read_file[-4:] != ".csv":
            sys.exit(f"{read_file} is not a CSV file")
 #       elif write_file[-4:] != ".csv":
 #           sys.exit(f"{write_file} is not a CSV file")
        else:
            return read_file, write_file

def file_transfer(read_file, write_file):
    try:
        with open(read_file) as input_file:
            reader = csv.reader(input_file)
            number = 1
            if write_file[-4:] != ".csv":
                write_file = write_file + ".csv"
            with open(write_file, "w") as wiping_file:
                pass
            for row in reader:
                if number == 1:
                    with open(write_file, "a", newline="") as output_file:
                        writer = csv.writer(output_file)
                        writer.writerow(["first", "last", "house"])
                    number += 1
                    pass
                else:
                    house = row[1]
                    full_name = row[0]
                    surname, first_name = full_name.split(",")
                    first_name = first_name.replace(" ", "")
                    with open(write_file, "a", newline="") as output_file:
                        writer = csv.writer(output_file)
                        writer.writerow([first_name, surname, house])
    except FileNotFoundError:
        sys.exit(f"Could not read {read_file}")

read_file, write_file = file_names()
file_transfer(read_file, write_file)
