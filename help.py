from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognition System")

        # title of system
        title_lbl = Label(self.root,text="Help",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1300,height=45)

        img_top = Image.open(r"images\helpdesk.png")
        img_top = img_top.resize((1300,650),Image.LANCZOS)
        self.picture_top=ImageTk.PhotoImage(img_top)

        bg_img=Label(self.root,image=self.picture_top)
        bg_img.place(x=0,y=55,width=1300,height=650)

        dev_label = Label(bg_img,text="Email:abc@gmail.com",font=("times new roman",15,"bold"),bg="white")
        dev_label.place(x=650,y=430)





if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()