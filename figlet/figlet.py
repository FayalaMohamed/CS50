from pyfiglet import Figlet
import sys

figlet = Figlet()
liste=figlet.getFonts()
print(sys.argv)
if len(sys.argv) == 2 or len(sys.argv) >3:
    sys.exit("Invalid usage 1")

f="slant"

if len(sys.argv) ==3:
    if sys.argv[1]!="-f" and sys.argv[1]!="--font" or sys.argv[2] not in liste:
        sys.exit("Invalid usage 2")
    f=sys.argv[2].lower()

s=input("Input: ")
print("Output: ")
figlet.setFont(font=f)
print(figlet.renderText(s))


