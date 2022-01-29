from tkinter import *

root = Tk()
btn1 = Button(root)
btn1["text"] = "Превед"
btn1["bg"] = "blue"
btn1["fg"] = "white"
btn1.place(x=70, y=50)
btn2 = Button(root, text = "Медвед", bg = "blue", fg = "white")
btn2.place(x=150,y=50)
def f1():
    btn1["text"] = "Медвед"
    btn2["text"] = "Превед"
def f2():
    btn1["text"] = "Медвед"

    btn2["text"] = "Превед"

btn1['command'] =f1
btn2["command"] = f2

root.mainloop()