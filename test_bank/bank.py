def main():
    s = input("Greeting: ")
    print(value(s))


def value(s):
    s = s.strip().lower()
    if len(s) >= 5 and s[0:5] == "hello":
        return 0
    elif s[0:1] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
