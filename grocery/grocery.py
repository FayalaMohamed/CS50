menu={}
while True:
    try:
        try:
            item = input("").upper()
            x = int(menu[item])
        except KeyError:
            menu[item]=1
        else:
            menu[item] = menu[item]+ 1

    except EOFError:
        menu=dict(sorted(menu.items()))
        for item in menu:
            print(menu[item],item)
        break
