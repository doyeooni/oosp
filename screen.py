from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image

root = Tk()
root.title('사진불러오기')
#root.geometry('800x600')#윈도우 크기 설정
root.resizable(True,True)

def click():
    root.destroy()
    import nextscreen
    
btn1 = Button(root, text="시작하기")
btn1.config(command=click)
btn1.place(x=750,y=50)


img = ImageTk.PhotoImage(Image.open("image_picture.jpg"))

l = Label(image=img)
l.pack(padx=150, pady=150)

root.mainloop()