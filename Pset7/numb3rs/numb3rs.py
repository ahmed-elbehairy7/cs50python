import re


def main() -> None:
    print(validate(input("IPv4 Address: ")))


def validate(ip: str) -> bool:
    if re.fullmatch(r"[\d]+\.[\d]+\.[\d]+\.[\d]+", ip):
        number = ip.split(".")
        for num in number:
            try:
                tmp = int(num)
                if not 0 <= tmp <= 255:
                    raise ValueError
            except ValueError:
                return False
        return True
    return False


if __name__ == "__main__":
    main()
