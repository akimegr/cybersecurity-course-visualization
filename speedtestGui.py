from tkinter import *

import speedtest


def clicked():
    test = speedtest.Speedtest()
    download = test.download()
    upload = test.upload()
    lbl.configure(text = f"Speed: {(download/1024)/1024} Mb/s \n Upload Speed: {(upload/1024)/1024} Mb/s")

window = Tk()
window.title("Доброе пожаловать в предложение speed test")
window.geometry("400x250")
lbl = Label(window, text = "Привет", font = ("Arial Bold", 10))
lbl.grid(column = 0, row = 0)
btn = Button(window, text = "Запустить тест скорости!", command = clicked)
btn.grid(column = 1, row = 0)
window.mainloop()


