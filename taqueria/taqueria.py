menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total=float(0)
while True:
    try:
        while True:
            try:
                item = input("Item: ").title()

                x=float(menu[item])
            except KeyError:
                pass
            else:
                break
        total = float(total+x)
        total=float(format(total,'.2f'))
        print(f"Total: ${total:.2f}")

    except EOFError:
        print()
        break
