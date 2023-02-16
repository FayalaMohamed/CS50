import sys
from tkinter import *
from tkinter import ttk

expr = ""


def calc(res):
    global expr
    try:
        expr = str(round(eval(str(expr)), 6))
    except: 
        expr="ERRROR"
    res.config(text=expr)


def press(num, res):
    global expr
    expr = expr + str(num)
    res.config(text=expr)


def clear(res):
    global expr
    expr = ""
    res.config(text=expr)


def main():
    root = Tk()
    root.title("Calculator")
    frm = ttk.Frame(root, padding=20,cursor="man")
    frm.grid()

    res = ttk.Label(frm, text=expr)
    res.grid(column=1, row=0)
    ttk.Button(frm, text="7", command=lambda: press("7", res), width=20).grid(
        column=0, row=2
    )
    ttk.Button(frm, text="8", command=lambda: press("8", res), width=20).grid(
        column=1, row=2
    )
    ttk.Button(frm, text="9", command=lambda: press("9", res), width=20).grid(
        column=2, row=2
    )
    ttk.Button(frm, text="4", command=lambda: press("4", res), width=20).grid(
        column=0, row=3
    )
    ttk.Button(frm, text="5", command=lambda: press("5", res), width=20).grid(
        column=1, row=3
    )
    ttk.Button(frm, text="6", command=lambda: press("6", res), width=20).grid(
        column=2, row=3
    )
    ttk.Button(frm, text="1", command=lambda: press("1", res), width=20).grid(
        column=0, row=4
    )
    ttk.Button(frm, text="2", command=lambda: press("2", res), width=20).grid(
        column=1, row=4
    )
    ttk.Button(frm, text="3", command=lambda: press("3", res), width=20).grid(
        column=2, row=4
    )
    ttk.Button(frm, text="0", command=lambda: press("0", res), width=20).grid(
        column=0, row=5
    )
    ttk.Button(frm, text="/", command=lambda: press("/", res), width=20).grid(
        column=1, row=5
    )
    ttk.Button(frm, text="*", command=lambda: press("*", res), width=20).grid(
        column=2, row=5
    )
    ttk.Button(frm, text="-", command=lambda: press("-", res), width=20).grid(
        column=0, row=6
    )
    ttk.Button(frm, text="+", command=lambda: press("+", res), width=20).grid(
        column=1, row=6
    )
    ttk.Button(frm, text="=", command=lambda: calc(res), width=20).grid(column=2, row=6)
    ttk.Button(frm, text="clr", command=lambda: clear(res), width=20).grid(
        column=2, row=7
    )
    root.mainloop()


if __name__ == "__main__":
    main()
