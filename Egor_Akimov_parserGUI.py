import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from tkinter import *
import lxml


root = Tk()
root["height"] = 800
root["width"] = 800


def findSevralTag(soup, TAG):
    global INFO
    INFO = soup.find_all(str(TAG))

def URLL():
    global soup
    website_url = requests.get(str(entrySite.get())).text
    soup = BeautifulSoup(website_url, 'lxml')

def findDate():
    global INFO, soup
    L=soup.find_all("div", class_="day")
    MY = soup.find("div", class_="month_year")
    INFO = []
    for i in L:
        INFO.append(i.get_text() + str(MY.get_text()))
    lblTg = Label(root, text=" Информация по датам найдена. Сохраняйте в файл" )
    lblTg.place(x=120, y=83)

def allDescription():
    global INFO, soup
    INF = soup.find_all("span", class_="lenta_textsmall")
    INFO = []
    for i in INF:
        INFO.append(i.get_text())

def allTitle():
    global INFO, soup
    INF = soup.find_all("span", class_="lenta_item_title")
    INFO = []
    for i in INF:
        INFO.append(i.get_text())

def entryTag():
    global TAG, soup
    TAG = entrytg.get()
    findSevralTag(soup,TAG)
    lblTg = Label(root, text="Tag: "+TAG +" . Информация найдена. Сохраняйте в файл" )
    lblTg.place(x=350, y=55)

def saveFile():
        global nameFile
        nameFile = entryName.get()
        file = open(str(nameFile) + ".txt", "wb")
        for i in INFO:
            file.write(str(i).encode("utf-8") + "\n".encode("utf-8"))


entrySite = Entry(root, width=100)
entrySite.place(x=10, y=20)
website_url = requests.get("https://www.belta.by/").text
soup = BeautifulSoup(website_url, 'lxml')



TAG = ""
INFO = ""
entrytg = Entry(root, width=30)
entrytg.place(x=160, y=55)


nameFile = ""



btnGetUrl = Button(root, bg = "black", fg = "white", text = "Get link", command = URLL)
btnGetUrl.place(x = 650, y = 17)
btnTag = Button(root,text="Enter tag: ", bg = "black", fg="white", command = entryTag )
btnTag.place(x=70,y=50)
btnSave = Button(root, text = "SAVE", bg = "red", fg = "white", command = saveFile)
btnSave.place(x=350,y = 695)
lblTg = Label(root, text="название файла: ")
lblTg.place(x=50, y=700)
entryName = Entry(root, width=30)
entryName.place(x=150, y=700)
btnDate = Button(root, text="Date", bg = "black", fg="white", command = findDate )
btnDate.place(x=70, y = 80)
btnDiscription = Button(root, text  = "Description", bg = "black", fg = "white", command = allDescription)
btnDiscription.place(x=70, y = 110)
btnDiscription = Button(root, text  = "Title", bg = "black", fg = "white", command = allTitle)
btnDiscription.place(x=70, y = 140)



root.mainloop()