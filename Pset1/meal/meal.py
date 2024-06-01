def main():
    time = input("What time is it? ")
    time = convert(time)
    match time:
        case s if 7 <= s <= 8:
            print("breakfast time")
        case s if 12 <= s <= 13:
            print("lunch time")
        case s if 18 <= s <= 19:
            print("dinner time")


def convert(time):
    a, b = time.split(":")
    return float(a) + (float(b) / 60)


if __name__ == "__main__":
    main()
