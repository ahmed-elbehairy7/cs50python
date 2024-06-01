def main():
    while True:
        try:
            x, y = input("Fraction: ").replace(" ", "").split("/")
            x, y = float(x), float(y)
            if x > y or x % 1 != 0 or y % 1 != 0:
                continue
            z = round((float(x) / float(y)) * 100)
            break
        except (ValueError, ZeroDivisionError) as errors:
            continue

    if z <= 1:
        print("E")
    elif z >= 99:
        print("F")
    else:
        print(f"{z}%")


if __name__ == "__main__":
    main()
