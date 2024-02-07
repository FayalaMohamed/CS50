def main():
    s = input("Fraction: ")
    p = convert(s)
    print(gauge(p))


def convert(s):
    pos = -1
    for i, c in enumerate(s):
        if c == '/' and pos == -1:
            pos = i
    try:
        x = int(s[:pos])
        y = int(s[pos+1:])
    except ValueError:
        pass
    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError

    p = int(round(x*100/y, 0))
    return p


def gauge(percentage):
    if percentage<=1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage)+"%"


if __name__ == "__main__":
    main()
