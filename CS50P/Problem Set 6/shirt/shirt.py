import sys
from PIL import Image, ImageOps


def file_names():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        read_file = sys.argv[1]
        write_file = sys.argv[2]
        if (read_file[-5:] == ".jpeg" or read_file[-4:] == ".png" or read_file[-4:] == ".jpg") and (write_file[-5:] == ".jpeg" or write_file[-4:] == ".png" or write_file[-4:] == ".jpg"):
            if (read_file[-5:] == ".jpeg" or read_file[-4:] == ".jpg") and (write_file[-5:] == ".jpeg" or write_file[-4:] == ".jpg") or (read_file[-4:] == ".png" and write_file[-4:] == ".png"):
                return read_file, write_file
            else:
                sys.exit("Input and output have different extensions")
        else:
            sys.exit("Invalid input")


def overlay(read_file, write_file):
    try:
        shirt = Image.open("shirt.png")
        size = shirt.size
        image = Image.open(read_file)
        image = ImageOps.fit(image, size)
        image.paste(shirt, (0, 0), shirt)
        image.save(write_file)
    except FileNotFoundError:
        sys.exit("File not found")

read_file, write_file = file_names()
overlay(read_file, write_file)
