from tkinter import *


def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(scvalue.get())
        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root = Tk()
root.geometry("500x600")
root.title("Calculator")
root.wm_iconbitmap("CodeClauseInternship_Calculator in Python\calculator.ico")

scvalue = StringVar()
scvalue.set("")
screen = Entry(textvariable=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=5, ipady=5, padx=10, pady=15)

padxa = 35
padxb = 35
padya = 11
padyb = 10

f = Frame(root, bg="gray", )
b = Button(f, text=f"C", font="lucida 17 bold", padx=31, pady=10)
b.pack(side=LEFT, padx=padxb, pady=padyb)
b.bind("<Button-1>", click)
b = Button(f, text=f"+", font="lucida 15 bold", padx=padxa, pady=padya)
b.pack(side=LEFT, padx=padxb, pady=padyb)
b.bind("<Button-1>", click)
b = Button(f, text=f"-", font="lucida 15 bold", padx=padxa, pady=padya)
b.pack(side=LEFT, padx=padxb, pady=padyb)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="gray")
for i in range(7, 10):
    b = Button(f, text=f"{i}", font="lucida 15 bold", padx=padxa, pady=padya)
    b.pack(side=LEFT, padx=padxb, pady=padyb)
    b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="gray", )
for i in range(4, 7):
    b = Button(f, text=f"{i}", font="lucida 15 bold", padx=padxa, pady=padya)
    b.pack(side=LEFT, padx=padxb, pady=padyb)
    b.bind("<Button-1>", click)
f.pack()
f = Frame(root, bg="gray", )
for i in range(1, 4):
    b = Button(f, text=f"{i}", font="lucida 15 bold", padx=padxa, pady=padya)
    b.pack(side=LEFT, padx=padxb, pady=padyb)
    b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="gray", )
b = Button(f, text=f". ", font="lucida 15 bold", padx=padxa, pady=padya)
b.pack(side=LEFT, padx=padxb, pady=padyb)
b.bind("<Button-1>", click)
b = Button(f, text=f"0", font="lucida 15 bold", padx=padxa, pady=padya)
b.pack(side=LEFT, padx=padxb, pady=padyb)
b.bind("<Button-1>", click)
b = Button(f, text=f"%", font="lucida 15 bold", padx=padxa, pady=padya)
b.pack(side=LEFT, padx=padxb, pady=padyb)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="gray", )
b = Button(f, text=f"*", font="lucida 15 bold", padx=37, pady=padya)
b.pack(side=LEFT, padx=36, pady=padyb)
b.bind("<Button-1>", click)
b = Button(f, text=f"/", font="lucida 15 bold", padx=36, pady=padya)
b.pack(side=LEFT, padx=36, pady=padyb)
b.bind("<Button-1>", click)
b = Button(f, text=f"=", font="lucida 15 bold", padx=padxa, pady=padya)
b.pack(side=LEFT, padx=36, pady=padyb)
b.bind("<Button-1>", click)
f.pack()
root.mainloop()