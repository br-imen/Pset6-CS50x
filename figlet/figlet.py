from pyfiglet import Figlet, FigletFont, FontNotFound
from cs50 import get_string
from sys import argv,exit


if len(argv) == 3 and argv[1] in ["--font", "-f"]:
    print(argv[2])
    try:
        FigletFont.preloadFont(argv[2])
    except FontNotFound as e:
        print("Invalid usage")
        exit(1)
    input = get_string("input:")
    f = Figlet(font = argv[2])
    output = f.renderText(input)
    print(output)
    exit(0)

elif len(argv) == 1:
    input = get_string("input:")
    print(input)
    exit(0)

else:
    print("Invalid usage")
    exit(2)

