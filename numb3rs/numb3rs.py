import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    res = re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$",ip)
    if res:
        try:
            if (0 <= int(res.group(1)) <= 255
                and 0 <= int(res.group(2)) <= 255
                and 0 <= int(res.group(3)) <= 255
                and 0 <= int(res.group(4)) <= 255):
                return True
        except ValueError:
            return False
    return False


if __name__ == "__main__":
    main()