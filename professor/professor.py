import random


def main():
    level=get_level()
    liste = []
    for i in range(10):
        test = []
        try:
            x=generate_integer(level)
            y = generate_integer(level)
        except ValueError:
            pass
        test.append(x)
        test.append(y)
        test.append(x+y)
        liste.append(test)

    nb = 0
    score = 0
    for i in range(10):
        nb = 0
        while True:
            try:
                print(liste[i][0], "+", liste[i][1], "= ", end="")
                res = int(input())
            except:
                print("EEE")
                nb += 1
                if nb == 3:
                    print(liste[i][0], "+", liste[i][1], "=", liste[i][2])
                    break
            else:
                if res == liste[i][2]:
                    score += 1
                    break
                print("EEE")
                nb += 1
                if nb == 3:
                    print(liste[i][0], "+", liste[i][1], "=", liste[i][2])
                    break
    print("Score:", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if level in [1, 2, 3]:
                break
    return level

def generate_integer(level):
    if level == 1:
        x = random.randint(1, 9)
    elif level == 2:
        x = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
    else:
        raise ValueError
    return x


if __name__ == "__main__":
    main()

