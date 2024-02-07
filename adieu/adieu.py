import inflect
p=inflect.engine()
liste=[]

while True:
    try:
        liste.append(input("Name: "))

    except EOFError:
        print()
        """ print("Adieu, adieu, to ",sep="",end="")
        if len(liste)>2:
            for item in liste[:-2]:
                print(item+", " ,sep="",end="")
        if len(liste)>1:
            print(liste[len(liste)-2]+" and "+liste[len(liste)-1])
        if len(liste)==1:
            print(liste[0]) """
        break
print("Adieu, adieu, to "+p.join(liste))
