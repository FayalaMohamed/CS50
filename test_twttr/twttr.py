def main():
    s = input("Input: ")
    print("Output:",shorten(s))

def shorten(s):
    vowels = ["o", "i", "e", "a", "u"]
    res=""
    for i, c in enumerate(s):
        if c.lower() not in vowels:
            res+=c
    return res


if __name__ == "__main__":
    main()
