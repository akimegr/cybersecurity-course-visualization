from tkinter import *
import time

root = Tk()
root["width"] = 169
root["height"] = 169

counter = 1
check = [
    ["","",""],
    ["","",""],
    ["","",""]
]
b = True
def checkWin():
    global  check,b
    if (check[0][0]==check[0][1]==check[0][2]=="X" or check[1][0]==check[1][1]==check[1][2]=="X" or check[2][0]==check[2][1]==check[2][2]=="X" or check[0][0]==check[1][0]==check[2][0]=="X" or check[0][1]==check[1][1]==check[2][1]=="X" or check[0][2]==check[1][2]==check[2][2]=="X" or check[0][0]==check[1][1]==check[2][2]=="X" or check[2][0]==check[1][1]==check[0][2]=="X"):
        lbl = Label(root, text = "Выиграл игрок X")
        lbl.place(x=10,y=30)
        print("Выиграл игрок X")
        b=False
    elif (check[0][0]==check[0][1]==check[0][2]=="O" or check[1][0]==check[1][1]==check[1][2]=="O" or check[2][0]==check[2][1]==check[2][2]=="O" or check[0][0]==check[1][0]==check[2][0]=="O" or check[0][1]==check[1][1]==check[2][1]=="O" or check[0][2]==check[1][2]==check[2][2]=="O" or check[0][0]==check[1][1]==check[2][2]=="O" or check[2][0]==check[1][1]==check[0][2]=="O"):
        lbl = Label(root, text = "Выиграл игрок O")
        lbl.place(x=10,y=30)
        print("Выиграл игрок O")
        b=False

    elif counter==9:
        lbl = Label(root, text="Ничья")
        lbl.place(x=10, y=30)
        print("Ничья")
        b = False


        return
def tick(But,r,c):
    # temp = []
    # temp.append([row,column])
    # print(temp)
    # counter+=1

    global counter, check,b
    if not b:
        root.destroy()
        return

    if But["text"]=="":
        if counter%2==0:
            But["text"]="X"
            But.grid(ipadx=11)
            check[r][c] = "X"
            checkWin()
        else:
            But["text"]="O"
            But.grid(ipadx=9.5)
            check[r][c]="O"
            checkWin()
        counter+=1



but11 = Button(root, bg="blue", fg="red", text="", command=lambda: tick(but11,0,0))
but11.grid(padx=0, pady=0, column=0, row=0, ipadx=14, ipady=5)
but12 = Button(root, bg="blue", fg="red", text="", command=lambda: tick(but12,0,1))
but12.grid(padx=0, pady=0, column=1, row=0, ipadx=14, ipady=5)
but13 = Button(root, bg="blue", fg="red", text="", command=lambda: tick(but13,0,2))
but13.grid(padx=0, pady=0, column=2, row=0, ipadx=14, ipady=5)
but21 = Button(root, bg="blue", fg="red", text="", command=lambda: tick(but21,1,0))
but21.grid(padx=0, pady=0, column=0, row=1, ipadx=14, ipady=5)
but22 = Button(root, bg="blue", fg="red", text="", command=lambda: tick(but22,1,1))
but22.grid(padx=0, pady=0, column=1, row=1, ipadx=14, ipady=5)
but23 = Button(root, bg="blue", fg="red", text="", command=lambda: tick(but23,1,2))
but23.grid(padx=0, pady=0, column=2, row=1, ipadx=14, ipady=5)
but31 = Button(root, bg="blue", fg="red", text="", command=lambda: tick(but31,2,0))
but31.grid(padx=0, pady=0, column=0, row=2, ipadx=14, ipady=5)
but32 = Button(root, bg="blue", fg="red", text="", command=lambda: tick(but32,2,1))
but32.grid(padx=0, pady=0, column=1, row=2, ipadx=14, ipady=5)
but33 = Button(root, bg="blue", fg="red", text="", command=lambda: tick(but33,2,2))
but33.grid(padx=0, pady=0, column=2, row=2, ipadx=14, ipady=5)

root.mainloop()


