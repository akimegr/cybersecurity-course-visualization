
from tkinter import *


root = Tk()

root["width"] = 400
root["height"]=400

entry = Entry(root, width=20)
entry.place(x=40, y=20)
entry2 = Entry(root, width=20)
entry2.place(x=250, y=20)
lbl = Label(root, text = "ЗНАК")
lbl.place(x=185,y=20)

def tick(bt):
    s = 0.0
    if (bt["text"]=="+"):
        s = int(entry.get()) + int(entry2.get())
        lbl = Label(root, text="Ответ: " + str(s))
        lbl.place(x=185, y=50)
    elif (bt["text"]=="*"):
        s = int(entry.get()) * int(entry2.get())
        lbl1 = Label(root, text="Ответ: " + str(s))
        lbl1.place(x=185, y=50)
    elif (bt["text"]=="/"):
        s = int(entry.get()) / int(entry2.get())
        lbl2 = Label(root, text="Ответ: " + str(s))
        lbl2.place(x=185, y=50)
    elif (bt["text"]=="-"):
        s = int(entry.get()) - int(entry2.get())
        lbl3 = Label(root, text="Ответ: " + str(s))
        lbl3.place(x=185, y=50)
    elif (bt["text"]=="//"):
        s = int(entry.get()) // int(entry2.get())
        lbl4 = Label(root, text="Ответ: " + str(s))
        lbl4.place(x=185, y=50)
    elif (bt["text"]=="%"):
        s = int(entry.get()) % int(entry2.get())
        lbl5 = Label(root, text="Ответ: " + str(s))
        lbl5.place(x=185, y=50)




btn1 = Button(root, bg = "blue", fg = "white",text = "+", command  = lambda : tick(btn1) )
btn1.place(x=50, y =100)
btn2 = Button(root, bg = "blue", fg = "white",text = "*", command = lambda : tick(btn2) )
btn2.place(x=100, y =100)
btn3 = Button(root, bg = "blue", fg = "white",text = "/", command = lambda : tick(btn3))
btn3.place(x=140, y =100)
btn4 = Button(root, bg = "blue", fg = "white",text = "%", command = lambda : tick(btn4))
btn4.place(x=190, y =100)
btn5 = Button(root, bg = "blue", fg = "white",text = "//", command = lambda : tick(btn5))
btn5.place(x=240, y =100)
btn6 = Button(root, bg = "blue", fg = "white",text = "-", command = lambda : tick(btn6))
btn6.place(x=290, y =100)






root.mainloop()





