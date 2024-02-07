import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    reti=""
    res = re.search(
        r"^([0-9]{1,2})(?::([0-9]{2}))? (AM|PM) to ([0-9]{1,2})(?::([0-9]{2}))? (AM|PM)", s)
    if not res:
        raise ValueError
    if (res.group(1) == None or res.group(3) == None or res.group(4) == None or res.group(6) == None):
        raise ValueError
    if ((res.group(2) != None and not 0 <= int(res.group(2)) < 60) or
            (res.group(5) != None and not 0 <= int(res.group(5)) < 60)):
        raise ValueError
    if (not 0 <= int(res.group(1)) < 25) or (not 0 <= int(res.group(4)) < 15):
        raise ValueError

    first=""
    if (res.group(3) =="PM"):
        a=(int(res.group(1))+12)%24
        if a < 10:
            first += "0"
        first+=str(a)
    else:
        if int(res.group(1))<10:
            first+="0"
        first += res.group(1)

    first+=":"
    if(res.group(2) == None):
        first+="00"
    else:
        first += res.group(2)

    second=""
    if (res.group(6) == "PM"):
        a=(int(res.group(4))+12) % 24
        if a < 10:
            second += "0"
        second += str(a)
    else:
        if int(res.group(4))<10:
            second+="0"
        second += res.group(4)

    second+=":"
    if(res.group(5) == None):
        second+="00"
    else:
        second += res.group(5)

    if second=="00:00":
        tmp=first
        first=second
        second=tmp
    reti+=first+" to "+second
    return reti

if __name__ == "__main__":
    main()