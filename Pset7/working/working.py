import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(text: str):
    if not re.fullmatch(
        r"[\d]{1,2}(:[\d]{1,2})? (AM|PM) to [\d]{1,2}(:[\d]{1,2})? (AM|PM)", text
    ):
        raise ValueError
    hours = re.split("to", (text.replace(" ", "")))
    if len(hours) != 2:
        raise ValueError

    for i in range(2):
        hours[i] = re.split(":", hours[i])

        if len(hours[i]) == 1:
            if "AM" in hours[i][0]:
                hours[i] = hours[i][0].replace("AM", "")
                if int(hours[i]) > 12:
                    raise ValueError

            elif "PM" in hours[i][0]:
                hours[i] = hours[i][0].replace("PM", "")
                if int(hours[i]) > 12:
                    raise ValueError
                hours[i] = str(int(hours[i]) + 12)

            else:
                raise ValueError

            hours[i] = [hours[i], "00"]
            if hours[i][0] == "12" or hours[i][0] == "24":
                hours[i][0] = str(int(hours[i][0]) - 12)
            continue

        elif len(hours[i]) != 2:
            raise ValueError

        if not 0 <= int(hours[i][0]) <= 12:
            raise ValueError

        if "AM" in hours[i][1]:
            hours[i][1] = hours[i][1].replace("AM", "")
            if int(hours[i][0]) > 12:
                raise ValueError

        elif "PM" in hours[i][1]:
            hours[i][1] = hours[i][1].replace("PM", "")
            if int(hours[i][0]) > 12:
                raise ValueError
            hours[i][0] = str(int(hours[i][0]) + 12)
        else:
            raise ValueError

        if not 0 <= int(hours[i][1]) < 60:
            raise ValueError

        if hours[i][0] == "12" or hours[i][0] == "24":
            hours[i][0] = str(int(hours[i][0]) - 12)

    return f"{(hours[0][0].zfill(2))}:{(hours[0][1].zfill(2))} to {(hours[1][0].zfill(2))}:{(hours[1][1].zfill(2))}"


if __name__ == "__main__":
    main()
