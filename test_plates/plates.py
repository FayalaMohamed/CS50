def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if (len(s) < 2 or len(s) > 6):
        return False
    if (s[0].upper() == s[0].lower() or s[1].upper() == s[1].lower()):
        return False
    if (not s.isalnum()):
        return False
    numbers = 0
    pos = -1
    for i, c in enumerate(s):
        if c.upper() == c.lower():
            if pos == -1:
                if int(c) == 0:
                    return False
                pos = i
            numbers = numbers+1
    if (pos != len(s)-numbers and pos != -1):
        return False
    return True


if __name__ == "__main__":
    main()
