import tkinter as tk
import tkinter.filedialog 
from PIL import ImageTk, Image
from tkinter import *

#윈도우 생성
root=tk.Tk()

#타이틀 이름 설정
root.title('NextPage')

#창의 크기 설정
root.geometry("1000x1000")

#첫화면으로 이동하는 함수
def click():
    root.destroy()
    import screen

#파일 불러오기 실행 함수
def openfile():
    global filename
    filename=tk.filedialog.askopenfilename(initialdir = "C:/oosp/data",
        title = "open file", filetypes = (("text file","*.txt"),("all files","*.*")))


#불러온 사진 추가


root.mainloop()