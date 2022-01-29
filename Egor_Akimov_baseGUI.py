from tkinter import *


root = Tk()

entry = Entry(root, width = 25)
entry.place(x=20, y = 70)

def binary():
    b = int(entry.get())
    if b==0:
        s=0
    s=""
    while(b>0):
        s += str(b % 2)
        b //= 2
    s=s[::-1]
    lbl["text"] = s

def eight():
    b = int(entry.get())
    if b==0:
        s=0
    s=""
    while(b>0):
        s += str(b % 8)
        b //= 8
    s=s[::-1]
    lbl["text"] = s

def sixteen():
    b = int(entry.get())
    if b==0:
        s=0
    s=""
    while(b>0):
        f= b % 16

        if f==10:
            f="A"
        elif f==11:
            f="B"
        elif f==12:
            f="C"
        elif f==13:
            f="D"
        elif f==14:
            f="E"
        elif f==15:
            f="F"

        s += str(f)
        b //= 16
    s=s[::-1]
    lbl["text"] = "Ответ: " + s


lbl = Label(root)
lbl.place(x=40,y=90)

btn1=Button(root, text = "В 2", bg = "blue", fg = "white")
btn1.place(x=20, y=20)
btn1["command"] = binary
btn2=Button(root, text = "В 8", bg = "blue", fg = "white")
btn2.place(x=60, y=20)
btn2["command"] = eight
btn2=Button(root, text = "В 16", bg = "blue", fg = "white")
btn2.place(x=100, y=20)
btn2["command"] = sixteen




root.mainloop()

