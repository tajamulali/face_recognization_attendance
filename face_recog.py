from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
from time import strftime
from datetime import datetime
import numpy as np


class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognition System")

        title_lbl = Label(self.root,text="Face recognition",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1300,height=45)

        img_top = Image.open(r"images\f14.png")
        img_top = img_top.resize((500,600),Image.LANCZOS)
        self.picture_top=ImageTk.PhotoImage(img_top)

        bg_img=Label(self.root,image=self.picture_top)
        bg_img.place(x=0,y=50,width=500,height=600)

        img_btm = Image.open(r"images\f15.jpg")
        img_btm = img_btm.resize((780,600),Image.LANCZOS)
        self.picture_btm=ImageTk.PhotoImage(img_btm)

        bg_img=Label(self.root,image=self.picture_btm)
        bg_img.place(x=500,y=50,width=780,height=600)

        # Button
        b1_1 = Button(bg_img,text="Face Recognition",command=self.face_recog,cursor="hand2",font=("times new roman",15,"bold"),bg="darkgreen",fg="white")
    
        b1_1.place(x=350,y=530,width=170,height=50)

    # ============Attendance================

    def mark_attendance(self, stu, name, roll, dep):
        with open("nuwaib.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()  # Read all lines from the file
            name_list = []

            # Parse existing records
            for line in myDataList:
                entry = line.strip().split(",")  # Split line into fields
                name_list.append(entry[0])  # Store the first field (student ID)

            # Connect to the database and fetch student details
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="face_attendance")
            mycursor = conn.cursor()

            mycursor.execute("select std_id from student where std_id=%s", (stu,))
            s = mycursor.fetchone()

            # Convert result to string
            stu = "+".join(map(str, s)) if s else "Unknown"

            # Add attendance if student is not already in the list
            if stu not in name_list:
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{stu},{name},{roll},{dep},{dtString},{d1},Present")




    # =========Face recognition============

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coordinates = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", user="root", password="", database="face_attendance")
                mycursor = conn.cursor()

                # Fetch name
                mycursor.execute("select name from student where std_id=%s", (id,))
                n = mycursor.fetchone()
                name = "+".join(n) if n else "Unknown"

                # Fetch roll
                mycursor.execute("select roll from student where std_id=%s", (id,))
                r = mycursor.fetchone()
                roll = "+".join(r) if r else "Unknown"

                # Fetch department
                mycursor.execute("select dep from student where std_id=%s", (id,))
                d = mycursor.fetchone()
                dep = "+".join(d) if d else "Unknown"

                # Fetch Id
                mycursor.execute("select std_id from student where std_id=%s", (id,))
                s = mycursor.fetchone()
                stu = "+".join(map(str, s)) if s else "Unknown"

                if confidence > 77:
                    cv2.putText(img, f"Id:{stu}", (x, y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name:{name}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Noll:{roll}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department{dep}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(stu,name,roll,dep)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coordinates = [x, y, w, h]

            return coordinates

        
        def recognize(img,clf,faceCascade):
            coordinates=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("Classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Attendance",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()



if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()