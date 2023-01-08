import tkinter as tk
import tkinter.filedialog 

#윈도우 생성
root=tk.Tk()

#타이틀 이름 설정
root.title('NextPage')

#창의 크기 설정
root.geometry("1000x400+100+100")


def openfile():
    global filename
    filename=tk.filedialog.askopenfilename(initialdir = "C:/oosp/data",
        title = "open file", filetypes = (("text file","*.txt"),("all files","*.*")))

lab1=tk.Label(root,text="사진선택",font=('Arial 13 bold'),bg='white',fg="black",width=11,height=1)
lab1.grid(row=0,column=0,padx=5,pady=20)

#이미지 추가
file_img=tk.PhotoImage(open("dog.jpg"))
#file_img= tkinter.PhotoImage(file="C:/Users/Do Yeon/oosp/oosp/icon.jpg")
file_img=file_img.subsample(50,50)


btn3 = tkinter.Button(root, overrelief="solid",width = 50, height = 50, command=openfile,bg="white",image=file_img)
btn3.grid(row=0, column=1, padx=5, pady=20)

root.mainloop()