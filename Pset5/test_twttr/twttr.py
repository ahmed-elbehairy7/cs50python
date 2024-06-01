def main():
    shorten(input("Input: "))


def shorten(text):
    vowels = ["a", "e", "i", "o", "u"]
    for i in text:
        if i.lower() in vowels:
            text = text.replace(i, "")
    print("Output:", text)
    return text


if __name__ == "__main__":
    main()
