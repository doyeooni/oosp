import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import *

#윈도우 생성
root=Tk()

#타이틀 이름 설정
root.title('NextPage')

#창의 크기 설정
root.geometry("1000x1000")

#첫화면으로 이동하는 함수
def click():
    root.destroy()
    import screen

#이미지 추가(jpg로 사용할 때 오류 뜸 // png로 불러올것)
file_img=tk.PhotoImage(file="C:/Users/Do Yeon/oosp/oosp/home_icon.png")
file_icon=tk.PhotoImage(file="C:/Users/Do Yeon/oosp/oosp/file_icon.png")

#파일을 불러오고 업로드하는 함수 구현
def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir='', title='파일선택', filetypes=(
    ('png files', '*.png'), ('jpg files', '*.jpg'), ('all files', '*.*')))
 
    Label(root, text=root.filename).pack() # 파일경로 view
    my_image = PhotoImage(file=root.filename)
    Label(image=my_image).pack() #사진 view

 
my_btn = Button(root, command=open, image=file_icon)
my_btn.place(x=50,y=1)


#'사진선택' 문구 출력 (label 사용)
'''
lab1=tk.Label(root,text="사진선택",font=('Arial 13 bold'),bg='white',fg="black",width=11,height=1)
lab1.place(x=70,y=70)
'''


#첫화면으로 이동하는 버튼 구현
btn3 = tk.Button(root, image=file_img, command=click, width=40, height=40)
btn3.pack(expand=1, anchor=CENTER)
btn3.place(x=1,y=1)

#'사진 선택' 불러오기 구현

#btn4 = tkinter.Button(root, overrelief="solid",width = 50, height = 50, command=open,bg="white",image=file_icon).pack()
#btn4.place(x=200,y=50)


#불러온 사진 추가


root.mainloop()