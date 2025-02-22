from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognition System")

        
        # title of system
        title_lbl = Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1300,height=45)

        img_top = Image.open(r"images\f9.png")
        img_top = img_top.resize((1400,325),Image.LANCZOS)
        self.picture_top=ImageTk.PhotoImage(img_top)

        bg_img=Label(self.root,image=self.picture_top)
        bg_img.place(x=0,y=55,width=1400,height=270)

        # Button
        b1_1 = Button(self.root,text="Train Data",command=self.train_classifier,cursor="hand2",font=("times new roman",25,"bold"),bg="yellow",fg="green")
        b1_1.place(x=400,y=340,width=500,height=50)

        img_btm = Image.open(r"images\f13.png")
        img_btm = img_btm.resize((1400,325),Image.LANCZOS)
        self.picture_btm=ImageTk.PhotoImage(img_btm)

        bg_img=Label(self.root,image=self.picture_btm)
        bg_img.place(x=0,y=410,width=1400,height=270)


    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')     #Gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)

            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #==========Train Classifier & save================
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("Classifier.xml ")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")

         





if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()