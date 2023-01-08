from tkinter import *

root = Tk()

root.geometry("1000x400+100+100")

def click():
    root.destroy()
    import nextpage


btn1 = Button(root, text ='시작하기')
btn1.config(command=click)
btn1.pack()


root.mainloop()