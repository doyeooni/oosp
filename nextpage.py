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

#'사진선택' 문구 출력 (label 사용)
lab1=tk.Label(root,text="사진선택",font=('Arial 13 bold'),bg='white',fg="black",width=11,height=1)
lab1.place(x=70,y=70)

#이미지 추가(jpg로 사용할 때 오류 뜸 // png로 불러올것)
file_img=tk.PhotoImage(file="C:/Users/Do Yeon/oosp/oosp/back_icon.png")
file_icon=tk.PhotoImage(file="C:/Users/Do Yeon/oosp/oosp/file_icon.png")

#첫화면으로 이동하는 버튼 구현
btn3 = tk.Button(root, image=file_img, command=click, width=50, height=50)
btn3.pack(expand=1, anchor=CENTER)
btn3.place(x=1,y=1)

#'사진 선택' 불러오기 구현
btn4 = tkinter.Button(root, overrelief="solid",width = 50, height = 50, command=openfile,bg="white",image=file_icon)
btn4.place(x=200,y=50)

#불러온 사진 추가


root.mainloop()