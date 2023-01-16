import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import *
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter.font import Font


#윈도우 생성
root=Tk()
root.title('Midpage')
#배경 색 지정
root['bg'] = '#F5FFFA'

#창의 크기 설정
root.geometry("700x600")

file_icon=tk.PhotoImage(file="C:/Users/Do Yeon/oosp/oosp/file_icon.png")
next_icon = tk.PhotoImage(file="C:/Users/Do Yeon/oosp/oosp/next_icon.png")
file_img=tk.PhotoImage(file="C:/Users/Do Yeon/oosp/oosp/home_icon.png")

my_font = Font(
    family = 'Consolas',
    size = 23,
    weight = 'bold',
    slant = 'roman',
    underline = 0
)

#제목 설정
lab1 = tk.Label(root, text=" Image Filter Convert Program ", foreground="black", background="white", font=my_font, relief='solid')
lab1.pack()
lab1.place(x=90, y=1)

#페이지 이동 함수
def click():
    root.destroy()
    import screen

def next():
    root.destroy()
    import nextpage

#파일을 불러오고 업로드하는 함수 구현
def open_file():
    global my_image
    global my_path
    global path
    root.filename = filedialog.askopenfilename(initialdir='', title='파일선택', filetypes=(
    ('png files', '*.png'), ('jpg files', '*.jpg'), ('all files', '*.*')))
 
    #Label(root, text=root.filename).pack() # 파일경로 view
    

    my_image = PhotoImage(file=root.filename)
    my_img = Label(image=my_image)
    my_img.pack()
    my_img.place(x=100, y=100)

    #Label(image=my_image).pack() #사진 view


#my_btn = Button(root, command=open_file, image=file_icon)
#my_btn.place(x=60,y=1)

next_btn = Button(root, command = next, image = next_icon)
next_btn.place(x=650, y=1)

#첫화면으로 이동하는 버튼 구현
btn3 = tk.Button(root, image=file_img, command=click, width=40, height=40)
btn3.pack(expand=1, anchor=CENTER)
btn3.place(x=1,y=1)


#정중앙 라벨 배치 -> 버튼으로 변경
txt_btn = tk.Button(root, text='BRING UP THE FILE!', command=open_file, foreground='black', background='#F0F8FF', width = 45, height = 20, relief='solid')
txt_btn.pack()
txt_btn.place(x=170, y=100)

root.mainloop()