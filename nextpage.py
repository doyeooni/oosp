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

#배경 색 지정
root['bg'] = '#FAF0E6'

#타이틀 이름 설정
root.title('NextPage')

#창의 크기 설정
root.geometry("1000x1000")

my_font = Font(
    family = 'Times',
    size = 23,
    weight = 'bold',
    slant = 'roman',
    underline = 0
)

sub_font = Font(
    family = 'Tiems',
    size = 12,
    weight = 'bold',
    slant = 'roman'
)

main_font = Font(
    family = 'Times',
    size = 10,
    weight = 'bold',
    underline = 0
)

#제목 설정
lab1 = tk.Label(root, text="Image Filter Convert Program", foreground="black", background="white", font=my_font)
lab1.pack()
lab1.place(x=280, y=1)

#첫화면으로 이동하는 함수
def click():
    root.destroy()
    import screen

#이미지 추가(jpg로 사용할 때 오류 뜸 // png로 불러올것)
file_img=tk.PhotoImage(file="C:/Users/Do Yeon/oosp/oosp/home_icon.png")
file_icon=tk.PhotoImage(file="C:/Users/Do Yeon/oosp/oosp/file_icon.png")
nextpage_img = tk.PhotoImage(file="C:/Users/Do Yeon/oosp/oosp/nextpage_img.png")


#파일을 불러오고 업로드하는 함수 구현
def open_file():
    global my_image
    global my_path
    global path
    root.filename = filedialog.askopenfilename(initialdir='', title='파일선택', filetypes=(
    ('png files', '*.png'), ('jpg files', '*.jpg'), ('all files', '*.*')))
 
    #Label(root, text=root.filename).pack() # 파일경로 view
    my_path = Label(root, text=root.filename)
    my_path.place(x=700,y=1)
    path = str(my_path)

    my_image = PhotoImage(file=root.filename)
    my_img = Label(image=my_image)
    my_img.pack()
    my_img.place(x=100, y=50)

    #Label(image=my_image).pack() #사진 view



my_btn = Button(root, command=open_file, image=file_icon)
my_btn.place(x=50,y=1)


''''''
#첫화면으로 이동하는 버튼 구현
btn3 = tk.Button(root, image=file_img, command=click, width=40, height=40)
btn3.pack(expand=1, anchor=CENTER)
btn3.place(x=1,y=1)


#'사진 선택' 불러오기 구현

#btn4 = tkinter.Button(root, overrelief="solid",width = 50, height = 50, command=open,bg="white",image=file_icon).pack()
#btn4.place(x=200,y=50)

#문구 라벨 추가
lb = tk.Label(root, text='Click the Filter YOU WANT!', font = sub_font, foreground= 'white', background= 'black')
lb.pack()
lb.place(x=130, y= 70)


#블러 효과 1번으로 페이지 이동
def blurred_ver_1():
    root.destroy()
    import Blurred_first


#블러 효과 1번 버튼 구현
blur_btn1 = tk.Button(root, text='Blurred_ver.1', font = main_font, command=blurred_ver_1, width =15, height = 5)
blur_btn1.place(x=150, y=120)


#블러 효과 1번 설명 라벨 추가
blur_lab = tk.Label(root, text = '사진을 블러 처리해주는 효과로, 1번은 약한 효과를 가지고 있습니다.', wraplength=100 , foreground='black'
, background= 'white')
blur_lab.pack()
blur_lab.place(x=280, y= 125)

#블러 효과 2번으로 페이지 이동
def blurred_ver_2():
    root.destroy()
    import Blurred_second

#블러 효과 2번 버튼 구현
blur_btn2 = tk.Button(root,text = 'Blurred_ver.2', font = main_font, command=blurred_ver_2, width = 15, height = 5)
blur_btn2.place(x=550, y=120)


#블러 효과 2번 설명 라벨 추가
blur_lab2 = tk.Label(root, text='사진을 블러 처리해주는 효과로, 2번은 더 강한 효과를 가지고 있습니다.', wraplength=100, foreground='black', background='white')
blur_lab2.pack()
blur_lab2.place(x=680, y=125)

#어두움 효과로 페이지 이동
def Darkness():
    root.destroy()
    import Darkness

#어두움 버튼 구현
darkness_btn = tk.Button(root, text='Darkness', font = main_font, command = Darkness, width=15, height=5)
darkness_btn.place(x=150, y=260)


#어두움 효과 설명 라벨 추가
darkness_lab = tk.Label(root, text = '사진을 어둡게 처리해주는 효과입니다.', wraplength=100, foreground= 'black', background='white')
darkness_lab.pack()
darkness_lab.place(x=280, y= 265)

#밝기 효과로 페이지 이동
def Brightness():
    root.destroy()
    import Brightness

#밝기 효과 버튼 구현
bright_btn2 = tk.Button(root, text='Brightness', font = main_font, command = Brightness, width=15, height=5)
bright_btn2.place(x=550, y=260)

#밝기 효과 설명 라벨 추가
brightness_lab = tk.Label(root, text = '사진을 밝게 처리해주는 효과입니다.', wraplength=100, background='white', foreground='black')
brightness_lab.pack()
brightness_lab.place(x=680, y=265)

#선명도 효과로 페이지 이동
def definition():
    root.destroy()
    import Auto

#엣지 효과 버튼 구현
definition_btn = tk.Button(root, text='Definition', font = main_font, command = definition, width=15, height=5)
definition_btn.place(x=150,y=400)

#엣지 효과 설명 라벨 추가
edge_lab = tk.Label(root, text = '사진을 선명하게 만들어주는 효과입니다. ', wraplength=100, background='white', foreground='black')
edge_lab.pack()
edge_lab.place(x=280, y= 410)

#밑 부분 사진 추가
bottom_lab = tk.Label(root, image = nextpage_img)
bottom_lab.pack(expand = 1, anchor=SW)


root.mainloop()