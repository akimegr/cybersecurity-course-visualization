from tkinter import *

root = Tk()
# btn1 = Button(root)
# btn1["text"] = "Превед"
# btn1["bg"] = "blue"
# btn1["fg"] = "white"
# btn1.place(x=70, y=50)
# btn2 = Button(root, text = "Медвед", bg = "blue", fg = "white")
# btn2.place(x=150,y=50)
# def f1():
#     root.title(btn1["text"])
# def f2():
#     root.title(btn2["text"])
#
# btn1['command'] =f1
# btn2["command"] = f2
#
#
# root.mainloop()
#
#

# root["width"] = 400
# root["height"] = 200

# entry = Entry(root, width = 25)
# entry.place(x=20,y=20)
#
# btn = Button(root, text="Вычислить")
# btn.place(x=20,y=50)
#
# lbl = Label(root)
# lbl.place(x=200, y = 20)
#
# def btn_commang():
#     b = entry.get().split("+")
#     res = 0
#     for i in b:
#         res+=int(i)
#     lbl["text"] = "= " + str(res)
#
# btn["command"] = btn_commang

# v = StringVar()
# v.set("Пр")
# ent = Entry(root, width =20, bd = 3, textvariabl =v)
# ent.place(x=20,y=50)

#
# var1 = IntVar()
# var2 = IntVar()
# var1.set(1)
# var2.set(0)
# r1 = Radiobutton(root,text = "Первая", variable=var1, value=0)
# r1.place(x=20,y=50)
# r2 = Radiobutton(root,text = "Вторая", variable=var1, value=1)
# r2.place(x=60,y=50)
# r3 = Radiobutton(root,text = "Пятая", variable=var2, value=0)
# r3.place(x=20,y=20)
# r4 = Radiobutton(root,text = "Четвёртая", variable=var2, value=1)
# r4.place(x=60,y=20)


# v1 = IntVar()
# v2 = IntVar()
# check1 = Checkbutton(root, text="Первый флажок",variable=v1, onvalue=1, offvalue=0)
# check2 = Checkbutton(root, text="Второй флажок",variable=v2, onvalue=5, offvalue=0)
# check1.place(x=20,y=50)
# check2.place(x=100,y=50)

# words = ['Linux', 'Python', 'Tk', 'TKKKK']
# listbox = Listbox(root, selectmode=SINGLE, height=4)
# for i in words:
#     listbox.insert(END,i)
# listbox.place(x=20,y=50)
# entry = Entry(root, width = 25)
# entry.pack()
# lbl = Label(root, text= '= 1000')
# lbl.pack(side="top")
# btn = Button(root, text='Вычислить')
# btn.pack(side="right")

# f1=Frame(root,bg='gray', bd=5)
# f2=Frame(root,bg='gray', bd=5)
# f1.pack()
# f2.pack()
#
# entry= Entry(f1,width=25)
# entry.pack(side=LEFT)
# lbl = Label(f1, text='= 1000',bg='gray')
# lbl.pack(side=LEFT)
# btn = Button(f2, text='Вычислить')
# btn.pack()

#
# entry = Entry(root, width=25)
# entry.grid(row=0,column=0, padx=5, pady=5)
#
# lbl = Label(root, text="=1000", bg = "gray")
# lbl.grid(row=0, column=1, padx=5, pady=5)
# btn=Button(root, text="Вычислить")
# btn.grid(row=1,column=0, columnspan=2)


# entry = Entry(root, width = 25)
# entry.place(relx = 0.1, rely = 0.1)
# lbl = Label(root, text='= 1000', bg='gray')
# lbl.place(relx = 0.7, rely = 0.1)
# btn = Button(root, text='Вычислить')
# btn.place(relx = 0.4, rely = 0.5)
#

#
# def show(ev):
#     str = "x={0} y={1}".format(ev.x, ev.y)
#     root = ev.widget.master
#     root.title(str)
#
# f1 = Frame(root, bg = "yellow", width = 400, height = 400)
# f1.pack()
# f1.bind("<Motion>", show)

canvas = Canvas(root, width = 500, height = 500, bg ="lightblue", cursor = "pencil")
canvas.create_line(200,50,300,50,width=3,fill="blue")
canvas.create_line(0,0,100,100,width=2,arrow=LAST)
x = 75
y = 110
canvas.create_rectangle(x,y,x+80,y+50,fill="white", outline="blue")
canvas.create_polygon([250,100],[200,150],[300,150],
fill="yellow")
canvas.create_polygon([300,80],[400,80],[450,75],[450,200],[300,180],[330,160],outline="white",smooth=1)

canvas.create_oval([20,200],[150,300],fill="gray50")


root.mainloop()





