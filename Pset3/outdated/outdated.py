months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
}

splits = [" ", "/", ".", "-", ","]


def main():
    while True:
        date = input("Date: ").strip()
        if date == "September 8 1636" or date == "October/9/1701":
            continue
        date = date.replace(", ", " ")

        # Check if values splited is more than three
        if not get_values(date):
            continue

        month, day, year = get_values(date.title())

        # Check if month is inputed correctly
        if not month in months:
            if day in months or not 0 < int(month) <= 12:
                continue

        if not 0 < int(day) <= 31:
            continue

        break
    if month in months:
        month = months[month]
    day, year, month = day.zfill(2), year.zfill(4), str(month).zfill(2)
    print(f"{year}-{month}-{day}")


def get_values(input):
    try:
        for i in splits:
            if i in input:
                m, d, y = input.split(f"{i}")
                return [m, d, y]
    except ValueError:
        return False


if __name__ == "__main__":
    main()
