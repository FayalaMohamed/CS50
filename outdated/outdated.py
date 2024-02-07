months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
p
while True:
    s = input("Input: ").strip()
    posUn = -1
    posDe = -1
    posTr=-1
    text=False
    for i, c in enumerate(s):
        if c == '/' and posUn == -1:
            posUn = i
        elif c == '/':
            posDe=i
            posTr=i

        if c == ' ' and posUn == -1:
            posUn = i
            text=True
        elif c == ',':
            posDe = i
        elif c==" ":
            posTr=i

    month=s[:posUn].title()
    day=s[1+posUn:posDe]
    year=s[posTr+1:]

    if text and month in months:
        month=months.index(month)+1
    try:
        month=int(month)
        year=int(year)
        day=int(day)
    except ValueError:
            pass
    else:
        if 0<day<=31 and 0<month<13:
            print(year,"-",sep="",end="")
            if month<10:
                print("0", month,"-", sep="", end="")
            else:
                print(month,"-", sep="", end="")
            if day < 10:
                print("0", day, sep="", end="")
            else:
                print(day, sep="", end="")
            print()
            break


