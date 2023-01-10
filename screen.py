from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

root = Tk()

root.geometry("1000x1200")

#창 제목 설정
root.title('사진 필터 변환 프로그램')

def click():
    root.destroy()
    import nextpage

#제목 설정
lab1 = ttk.Label(root, text="사진 필터 변환 프로그램",padding=(40,0), foreground="black", background="white", font=("Times", "20"))
lab1.pack()

#다음페이지로 넘겨주는 버튼 구현
btn1 = Button(root, text ='시작하기')
btn1.config(command=click)
btn1.pack()


#첫화면 사진 넣기 구현
#file_img=tk.PhotoImage(file="C:/Users/Do Yeon/oosp/oosp/IMG_9096.png")
img = PhotoImage(file="C:/Users/Do Yeon/oosp/oosp/image_picture.png")
#img = img.resize((450,350), Image.ANTIALIAS)
#main_img = ImageTk.PhotoImage(img)
main_img = Label(image = img)
main_img.pack(padx=30, pady=100)



root.mainloop()