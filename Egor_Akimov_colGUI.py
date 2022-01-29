from tkinter import *


root = Tk()
paintRed = lambda : root.config(bg="red")
paintGreen = lambda : root.config(bg="green")
paintBlue = lambda : root.config(bg="blue")

but1 = Button(root, text="red", command = paintRed)
but1.pack()
but2 = Button(root, text="red", command = paintGreen)
but2.pack()
but3 = Button(root, text="red", command = paintBlue)
but3.pack()


root.mainloop()
