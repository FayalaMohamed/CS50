import sys

if(len(sys.argv)<2):
    sys.exit("Too few command-line arguments")
if (len(sys.argv) > 2):
    sys.exit("Too many command-line arguments")
l = len(sys.argv[1])
if sys.argv[1][l-3:]!=".py":
    sys.exit("Not a Python file")

nb=0
with open(sys.argv[1]) as file:
    for line in file:
        line=line.strip()
        if line!="" and line[0:1]!="#":
            nb+=1

print(nb)