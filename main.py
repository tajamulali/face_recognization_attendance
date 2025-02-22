from tkinter import*
from tkinter import ttk
import tkinter.messagebox
from PIL import Image,ImageTk
import tkinter
from time import strftime
from datetime import datetime
from student import Student
import os
from train import Train
from face_recog import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
from chat import GigiBot


class F_R_A_S:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognition System")

        img = Image.open(r"images\f15.jpg")
        img = img.resize((500, 130),Image.LANCZOS)
        self.picture = ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.picture)
        f_lbl.place(x=0,y=0,width=450,height=130)

        img1 = Image.open(r"images\f21.png")
        img1 = img1.resize((500, 130),Image.LANCZOS)
        self.picture1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.picture1)
        f_lbl.place(x=450,y=0,width=450,height=130)

        img2 = Image.open(r"images\f3.png")
        img2 = img2.resize((500, 130),Image.LANCZOS)
        self.picture2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.picture2)
        f_lbl.place(x=900,y=0,width=450,height=130)

        # background image
        img3 = Image.open(r"images\f6.png")
        img3 = img3.resize((1400,570),Image.LANCZOS)
        self.picture3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.picture3)
        bg_img.place(x=0,y=130,width=1400,height=570)

        # title of system
        title_lbl = Label(bg_img,text="Face recognition Attendance System Software",font=("times new roman",35,"bold"),bg="skyblue",fg="yellow")
        title_lbl.place(x=0,y=0,width=1300,height=45)

        # ==========Time_________________
        def time():
            String = strftime('%H:%M:%S %p')
            lbl.config(text = String)
            lbl.after(1000,time)

        lbl = Label(title_lbl,font=("times new roman",15,"bold"),bg="white",fg="blue")
        lbl.place(x=0,y=0,width=120,height=50)
        time()

        #student button
        img4 = Image.open(r"images\f19.png")
        img4 = img4.resize((220,180),Image.LANCZOS)
        self.picture4=ImageTk.PhotoImage(img4)

        b1 = Button(bg_img,image=self.picture4,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=100,width=220,height=180)

        b1_1 = Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="yellow",fg="black")
        b1_1.place(x=100,y=250,width=220,height=40)

        #Detect face button
        img5 = Image.open(r"images\f14.png")
        img5 = img5.resize((220,180),Image.LANCZOS)
        self.picture5=ImageTk.PhotoImage(img5)

        b1 = Button(bg_img,image=self.picture5,command=self.face_data,cursor="hand2")
        b1.place(x=400,y=100,width=220,height=180)

        b1_1 = Button(bg_img,text="Face Detector",command=self.face_data,cursor="hand2",font=("times new roman",15,"bold"),bg="yellow",fg="black")
        b1_1.place(x=400,y=250,width=220,height=40)

        #Attendance button
        img6 = Image.open(r"images\f7.png")
        img6 = img6.resize((220,180),Image.LANCZOS)
        self.picture6=ImageTk.PhotoImage(img6)

        b1 = Button(bg_img,image=self.picture6,command=self.attendance_data,cursor="hand2")
        b1.place(x=700,y=100,width=220,height=180)

        b1_1 = Button(bg_img,text="Attendance",command=self.attendance_data,cursor="hand2",font=("times new roman",15,"bold"),bg="yellow",fg="black")
        b1_1.place(x=700,y=250,width=220,height=40)

        #Help button
        img7 = Image.open(r"images\f17.png")
        img7 = img7.resize((220,180),Image.LANCZOS)
        self.picture7=ImageTk.PhotoImage(img7)

        b1 = Button(bg_img,image=self.picture7,command=self.help_data,cursor="hand2")
        b1.place(x=1000,y=100,width=220,height=180)

        b1_1 = Button(bg_img,text="Help Desk",command=self.help_data,cursor="hand2",font=("times new roman",15,"bold"),bg="yellow",fg="black")
        b1_1.place(x=1000,y=250,width=220,height=40)

        #Train button
        img8 = Image.open(r"images\f9.png")
        img8 = img8.resize((220,220),Image.LANCZOS)
        self.picture8=ImageTk.PhotoImage(img8)

        b1 = Button(bg_img,image=self.picture8,command=self.train_data,cursor="hand2")
        b1.place(x=100,y=330,width=220,height=180)

        b1_1 = Button(bg_img,text="Train Data",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg="yellow",fg="black")
        b1_1.place(x=100,y=480,width=220,height=40)

        #Photos button
        img9 = Image.open(r"images\f13.png")
        img9 = img9.resize((220,220),Image.LANCZOS)
        self.picture9=ImageTk.PhotoImage(img9)

        b1 = Button(bg_img,image=self.picture9,command=self.open_img,cursor="hand2")
        b1.place(x=400,y=330,width=220,height=180)

        b1_1 = Button(bg_img,text="Photos",command=self.open_img,cursor="hand2",font=("times new roman",15,"bold"),bg="yellow",fg="black")
        b1_1.place(x=400,y=480,width=220,height=40)

        #Developer button
        img10 = Image.open(r"images\f18.png")
        img10 = img10.resize((220,220),Image.LANCZOS)
        self.picture10=ImageTk.PhotoImage(img10)

        b1 = Button(bg_img,image=self.picture10,command=self.developer_data,cursor="hand2")
        b1.place(x=700,y=330,width=220,height=180)

        b1_1 = Button(bg_img,text="Developer",command=self.developer_data,cursor="hand2",font=("times new roman",15,"bold"),bg="yellow",fg="black")
        b1_1.place(x=700,y=480,width=220,height=40)

        #Exit button
        img11 = Image.open(r"images\f16.jpg")
        img11 = img11.resize((220,220),Image.LANCZOS)
        self.picture11=ImageTk.PhotoImage(img11)

        b1 = Button(bg_img,image=self.picture11,command=self.iExit,cursor="hand2")
        b1.place(x=1000,y=330,width=220,height=180)

        b1_1 = Button(bg_img,text="Exit",command=self.iExit,cursor="hand2",font=("times new roman",15,"bold"),bg="yellow",fg="black")
        b1_1.place(x=1000,y=480,width=220,height=40)

        #Chat Button
        img12 = Image.open(r"images\gigi.jpg")
        img12 = img12.resize((50,50),Image.LANCZOS)
        self.picture12=ImageTk.PhotoImage(img12)

        b1 = Button(bg_img,image=self.picture12,command=self.waiby,cursor="hand2")
        b1.place(x=5,y=480,width=60,height=60)



    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognitoion","Are you sure to exit this system",parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return

    # ============function buttons=============
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)
        
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)

    def waiby(self):
        self.new_window = Toplevel(self.root)
        self.app = GigiBot(self.new_window)





if __name__ == "__main__":
    root=Tk()
    obj=F_R_A_S(root)
    root.mainloop()
