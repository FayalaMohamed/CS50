import random


while True:
    try:
        x=int(input("Level: "))
    except:
        pass
    else:
        if x>0:
            break
x=random.randint(1,x)
while True:
    try:
        a = int(input("Guess: "))
    except:
        pass
    else:
        if a==x:
            print("Just right!")
            break
        elif a>x:
            print("Too large!")
        else:
            print("Too small!")


