from sys import exit, argv
from PIL import Image, ImageOps
from os.path import splitext


class ExtensionError(Exception):
    ...


class ArgsError(Exception):
    ...


extensions = [".jpg", ".jpeg", ".png"]

try:
    if len(argv) != 3:
        raise ArgsError
    before, after = splitext(argv[1]), splitext(argv[2])
    if not before[1] in extensions or not after[1] in extensions:
        raise ExtensionError
    if before[1] != after[1]:
        raise ExtensionError
    with Image.open(f"{before[0]}{before[1]}") as img:
        with Image.open("shirt.png") as shirt:
            muppet = ImageOps.fit(img, shirt.size)
            muppet.paste(shirt, shirt)
            muppet.save(f"{after[0]}{after[1]}")

except:
    exit("An error occured, please try again")
