import random
import pyfiglet as pfg
from sys import argv, exit

argl = len(argv)

# Check how many arguments there
if argl != 1 and argl != 3:
    exit("Invalid usage")

# Check if the argument is a font argument
if argl == 3 and argv[1].lower() != "-f" and argv[1].lower() != "--font":
    exit("Invalid usage")
if argl == 3:
    if not argv[2] in pfg.FigletFont.getFonts():
        exit("Invalid usage")

text = input("Input: ").strip()

if argl == 1:
    font = random.choice(pfg.FigletFont.getFonts())
else:
    font = argv[2]

print("Output: ")
print(pfg.figlet_format(text, font))
