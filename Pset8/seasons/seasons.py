from datetime import date
from sys import exit
import inflect


def main():
    try:
        year, month, day = input("Date of birth: ").split("-")
    except ValueError:
        exit("Invalid date")

    between = date.today() - date(int(year), int(month), int(day))
    print(convert(between.days * 1440), "minutes")


def convert(minutes):
    x = inflect.engine()
    return x.number_to_words(minutes).replace("and ", "").capitalize()


if __name__ == "__main__":
    main()
