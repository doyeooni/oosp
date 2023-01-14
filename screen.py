from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter.font import Font

root = Tk()

root.geometry("1000x1200")

#창 제목 설정
root.title('사진 필터 변환 프로그램')

def click():
    root.destroy()
    import nextpage

my_font = Font(
    family = 'Times',
    size = 23,
    weight = 'bold',
    slant = 'roman',
    underline = 0
)


sub_font = Font(
    family = 'Tiems',
    size = 10,
    weight = 'bold',
    slant = 'roman'
)

#제목 설정
lab1 = ttk.Label(root, text="사진 필터 변환 프로그램",padding=(40,0), foreground="black", background="white", font=my_font)
lab1.pack()
lab1.place(x=300, y=10)

#다음페이지로 넘겨주는 버튼 구현
btn1 = Button(root, text ='START', width=10, height = 2, font = sub_font)
btn1.config(command=click)
btn1.pack()
btn1.place(x=400,y=55)

#종료하기 버튼 구현
exit_btn = Button(root, text="CLOSE", width = 10, height = 2, font = sub_font)
exit_btn.config (command = exit)
exit_btn.pack()
exit_btn.place(x=500, y=55)


#첫화면 사진 넣기 구현
#file_img=tk.PhotoImage(file="C:/Users/Do Yeon/oosp/oosp/IMG_9096.png")
img = PhotoImage(file="C:/Users/Do Yeon/oosp/oosp/image_picture.png")
#img = img.resize((450,350), Image.ANTIALIAS)
#main_img = ImageTk.PhotoImage(img)
main_img = Label(image = img)
main_img.pack(padx=30, pady=100)



root.mainloop()