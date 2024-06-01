def main():
    text = input()
    text = convert(text)
    print(text)


def convert(string):
    return string.replace(":)", "🙂").replace(":(", "🙁")


main()
