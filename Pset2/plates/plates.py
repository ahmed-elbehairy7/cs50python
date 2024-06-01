from sys import exit


def main():
    plate = input("Plate: ")
    if not is_valid(plate):
        exit("INVALID")
    exit("VALID")


def is_valid(s):
    # Determines the length of string
    l = len(s)
    
    # If length is not acceptable
    if not 2 <= l <= 6:
        return False

    # If we don't have any digits then we don't need to execute the rest
    if s.isalpha():
        return True

    # if it have a digit but not at the end or start of string
    if not s[0].isdigit() and s[-0].isdigit():
        return False

    # check for every character
    for i in range(l):
        # If character is white space
        if s[i].isspace():
            return False

        # If the digit starts with zero
        if s[i] == "0" and not s[i - 1].isdigit():
            return False

        # If the digit is in the middle of the string alone
        if s[i].isdigit() and 0 < i < l - 1:
            if s[i - 1].isdigit():
                if not s[:i].isdigit():
                    return False
            elif s[i + 1].isdigit():
                if not s[i:].isdigit():
                    return False
            else:
                return False
    return True


if __name__ == "__main__":
    main()
