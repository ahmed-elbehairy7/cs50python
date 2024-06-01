def main():
    fraction = input("Fraction: ").replace(" ", "")
    value = convert(fraction)
    print(gauge(value))


def convert(fraction):
    x, y = fraction.split("/")
    x, y = float(x), float(y)
    if y == 0:
         raise ZeroDivisionError
    if y < x:
        raise ValueError
    return round((x / y) * 100)


def gauge(value):
    match value:
        case _ if value <= 1:
            return "E"
        case _ if value >= 99:
            return "F"
        case _:
            return f"{value}%"


if __name__ == "__main__":
    main()
