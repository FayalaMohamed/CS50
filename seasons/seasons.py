import sys
import inflect
from datetime import datetime, date, timedelta

def main():
    s=input("Date of Birth: ").strip()
    print(sing(s))

def sing(s):
    try:
        if d := datetime.strptime(s, "%Y-%m-%d"):
            birthdate = datetime.combine(d, datetime.min.time())
    except:
        sys.exit("Invalid date")

    today = datetime.combine(date.today(), datetime.min.time())

    diff=today-birthdate
    delta = int(diff / timedelta(minutes=1))
    p = inflect.engine()
    lyrics = p.number_to_words(delta, andword="")
    lyrics = f"{lyrics} minutes".capitalize()

    return lyrics

if __name__ == "__main__":
    main()