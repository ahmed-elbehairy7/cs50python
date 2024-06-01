import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(text):
    try:
        link = re.search('(?<=src=")https?://(www\.)?youtube.com/embed/[\w]+(?=")', text)
        link = re.sub(
            'https?://(www.)?youtube.com/embed', "https://youtu.be", link.group(0)
        )
        return link
    except AttributeError:
        return None


if __name__ == "__main__":
    main()
