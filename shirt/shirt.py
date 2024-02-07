import sys
from PIL import Image
from PIL import ImageOps
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")


li = len(sys.argv[1])
if (
    sys.argv[1][li - 4:] != ".png"
    and sys.argv[1][li - 4:] != ".jpg"
    and sys.argv[1][li - 5:] != ".jpeg"
):
    sys.exit("Invalid input")

lo = len(sys.argv[2])
if (
    sys.argv[2][lo - 4:] != ".png"
    and sys.argv[2][lo - 4:] != ".jpg"
    and sys.argv[2][lo - 5:] != ".jpeg"
):
    sys.exit("Invalid output")

if (
    sys.argv[1][li - 4:] != sys.argv[2][lo - 4:]
):
    sys.exit("Input and output have different extensions")

try:
    shirt=Image.open("shirt.png")
except FileNotFoundError:
    sys.exit("Could not find shirt.png")

try:
    before = Image.open(sys.argv[1],"r")
except FileNotFoundError:
    sys.exit("Input does not exist")

size = shirt.size
before=ImageOps.fit(before,size)
before.paste(shirt, shirt)
before.save(
    sys.argv[2]
)