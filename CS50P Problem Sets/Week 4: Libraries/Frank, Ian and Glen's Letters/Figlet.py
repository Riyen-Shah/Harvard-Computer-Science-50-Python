import sys
import random
from pyfiglet import Figlet
figlet = Figlet()
if len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in figlet.getFonts():
            OutputText = input("Input: ")
            Font = sys.argv[2]
            figlet.setFont(font=Font)
            print(figlet.renderText(OutputText))
        else:
            sys.exit("Incorrect Font Type")
    else:
        sys.exit("Incorrect First Argument")
elif len(sys.argv) == 1:
    OutputText = input("Input: ")
    FontList = figlet.getFonts()
    Range = len(FontList)
    Random = random.randrange(1, Range + 1)
    Font = FontList[Random]
    figlet.setFont(font=Font)
    print(figlet.renderText(OutputText))
else:
    sys.exit("Incorrect Number of Arguments")
