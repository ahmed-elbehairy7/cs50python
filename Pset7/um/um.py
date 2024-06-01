import re
import sys


def main():
    print(count(input("Text: ")))


def count(text):
    return len(re.findall(r"\b(?:\W)*um(?:\W)*\b", text, re.IGNORECASE))


if __name__ == "__main__":
    main()
