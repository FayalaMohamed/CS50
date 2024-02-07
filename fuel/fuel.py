def main():
    s=input("Fraction: ")
    (x,y,b)=check(s)
    while(b==False):
        s=input("Fraction: ")
        (x,y,b)=check(s)
    p=int(round(x*100/y,0))
    if p<=1:
        print("E")
    elif p >=99:
        print("F")
    else:
        print(p,"%",sep="")


def check(s):
    pos=-1
    for i,c in enumerate(s):
        if c=='/' and pos==-1:
            pos=i
        elif c == '/':
            return (-1,-1,False)

    try:
        x=int(s[:pos])
        y=int(s[pos+1:])
    except ValueError:
        return (-1, -1, False)
    if y==0 or x>y:
        return (-1, -1, False)
    return (x, y, True)


main()

