import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    res = re.search(r"^.*src=\"([^\"]*)(?:\"){1}.*", s)
    if not res:
        return None
    reti = res.group(1)
    if ("http://youtube.com" not in reti
        and "https://youtube.com" not in reti
        and "https://www.youtube.com" not in reti):
        return None
    reti=reti.replace("http://youtube.com/embed" ,"https://youtu.be")
    reti=reti.replace("https://youtube.com/embed" ,"https://youtu.be")
    reti = reti.replace("https://www.youtube.com/embed", "https://youtu.be")
    return reti

if __name__ == "__main__":
    main()