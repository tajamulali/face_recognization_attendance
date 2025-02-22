from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognition System")

        # title of system
        title_lbl = Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1300,height=45)

        img_top = Image.open(r"images\dev.png")
        img_top = img_top.resize((1300,650),Image.LANCZOS)
        self.picture_top=ImageTk.PhotoImage(img_top)

        bg_img=Label(self.root,image=self.picture_top)
        bg_img.place(x=0,y=55,width=1300,height=650)

        # FRame
        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=860,y=5,width=400,height=500)

        img_top1 = Image.open(r"images\groot.jpg")
        img_top1 = img_top1.resize((150,200),Image.LANCZOS)
        self.picture_top1=ImageTk.PhotoImage(img_top1)

        bg_img=Label(main_frame,image=self.picture_top1)
        bg_img.place(x=245,y=0,width=150,height=200)
        
        # Developer Info
        dev_label = Label(main_frame,text="Hello My Name is Nuwaib",font=("times new roman",15,"bold"),bg="white")
        dev_label.place(x=0,y=5)

        dev_label = Label(main_frame,text="I am Full-Stack Developer",font=("times new roman",15,"bold"),bg="white")
        dev_label.place(x=0,y=40)

        img_top2 = Image.open(r"images\f22.jpg")
        img_top2 = img_top2.resize((395,300),Image.LANCZOS)
        self.picture_top2=ImageTk.PhotoImage(img_top2)

        bg_img=Label(main_frame,image=self.picture_top2)
        bg_img.place(x=0,y=200,width=395,height=300)





if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()