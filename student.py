from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognition System")

        #=========Variables=======
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_stdId = StringVar()
        self.var_stdName = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

        img = Image.open(r"images\f15.jpg")
        img = img.resize((500, 110),Image.LANCZOS)
        self.picture = ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.picture)
        f_lbl.place(x=0,y=0,width=450,height=110)

        img1 = Image.open(r"images\f20.jpg")
        img1 = img1.resize((500, 110),Image.LANCZOS)
        self.picture1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.picture1)
        f_lbl.place(x=450,y=0,width=450,height=110)

        img2 = Image.open(r"images\f4.png")
        img2 = img2.resize((500, 110),Image.LANCZOS)
        self.picture2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.picture2)
        f_lbl.place(x=900,y=0,width=450,height=110)

        # background image
        img3 = Image.open(r"images\f10.png")
        img3 = img3.resize((1400,590),Image.LANCZOS)
        self.picture3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.picture3)
        bg_img.place(x=0,y=110,width=1400,height=590)

        # title of system
        title_lbl = Label(bg_img,text="Student Management",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1300,height=45)

        # ======Main Frame========
        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1250,height=515)

        #left label frame
        Left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=5,y=10,width=615,height=490)

        img_left = Image.open(r"images\f9.png")
        img_left = img_left.resize((600, 40),Image.LANCZOS)
        self.picture_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.picture_left)
        f_lbl.place(x=5,y=0,width=600,height=40)

        #current course Information
        current_c_frame = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Info",font=("times new roman",12,"bold"))
        current_c_frame.place(x=5,y=45,width=605,height=120)

        # Department
        dep_label = Label(current_c_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo = ttk.Combobox(current_c_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="read only",width=20)
        dep_combo['values']=('Select Department','CS','CSE','IMBA')
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # Course
        course_label = Label(current_c_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        dep_combo = ttk.Combobox(current_c_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="read only",width=20)
        dep_combo['values']=('Select Course','MCA','BTECH','Management','Education')
        dep_combo.current(0)
        dep_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # Batch
        batch_label = Label(current_c_frame,text="Batch",font=("times new roman",12,"bold"),bg="white")
        batch_label.grid(row=1,column=0,padx=10,sticky=W)

        batch_combo = ttk.Combobox(current_c_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="read only",width=20)
        batch_combo['values']=('Select Year','2022','2023','2024')
        batch_combo.current(0)
        batch_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # Semester
        sem_label = Label(current_c_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        sem_label.grid(row=1,column=2,padx=10,sticky=W)

        sem_combo = ttk.Combobox(current_c_frame,textvariable=self.var_sem,font=("times new roman",12,"bold"),state="read only",width=20)
        sem_combo['values']=('Select SEM','SEM-1','SEM-2','SEM-3','SEM-4')
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #Class student info
        student_info_frame = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Student Info",font=("times new roman",12,"bold"))
        student_info_frame.place(x=5,y=170,width=605,height=295)

        # student ID
        studentid_label = Label(student_info_frame,text="Student ID",font=("times new roman",13,"bold"),bg="white")
        studentid_label.grid(row=0,column=0,padx=10,pady=2,sticky=W)

        studentID_entry = ttk.Entry(student_info_frame,textvariable=self.var_stdId,width=15,font=("times new roman",13,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # student name
        studentname_label = Label(student_info_frame,text="Student Name",font=("times new roman",13,"bold"),bg="white")
        studentname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry = ttk.Entry(student_info_frame,textvariable=self.var_stdName,width=15,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # Class Division
        class_div_label = Label(student_info_frame,text="Student Division",font=("times new roman",13,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        div_combo = ttk.Combobox(student_info_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="read only",width=15)
        div_combo['values']=('Select Division','A','B','C')
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)


        # Roll no
        roll_no_label = Label(student_info_frame,text="Roll No:",font=("times new roman",13,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry = ttk.Entry(student_info_frame ,textvariable=self.var_roll,width=15,font=("times new roman",13,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        # Gender
        gender_label = Label(student_info_frame,text="Gender",font=("times new roman",13,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo = ttk.Combobox(student_info_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="read only",width=15)
        gender_combo['values']=('Male','Female')
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        # DOB
        dob_label = Label(student_info_frame,text="DOB",font=("times new roman",13,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry = ttk.Entry(student_info_frame,textvariable=self.var_dob,width=15,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # Email
        email_label = Label(student_info_frame,text="Email",font=("times new roman",13,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry = ttk.Entry(student_info_frame,textvariable=self.var_email,width=15,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        # Phone no
        ph_label = Label(student_info_frame,text="Phone No:",font=("times new roman",13,"bold"),bg="white")
        ph_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        ph_entry = ttk.Entry(student_info_frame,textvariable=self.var_phone,width=15,font=("times new roman",13,"bold"))
        ph_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        # Address
        address_label = Label(student_info_frame,text="Address",font=("times new roman",13,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry = ttk.Entry(student_info_frame,textvariable=self.var_address,width=15,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        # Teacher
        tea_label = Label(student_info_frame,text="Teacher",font=("times new roman",13,"bold"),bg="white")
        tea_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        tea_entry = ttk.Entry(student_info_frame,textvariable=self.var_teacher,width=15,font=("times new roman",13,"bold"))
        tea_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        # radio buttons
        self.var_radio1 = StringVar()
        Radiobtn1 = ttk.Radiobutton(student_info_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        Radiobtn1.grid(row=5,column=0)

        Radiobtn2 = ttk.Radiobutton(student_info_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        Radiobtn2.grid(row=5,column=1)

        #Button Frame
        btn_frame = Frame(student_info_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=0,y=200,width=600,height=70)

        save_btn = Button(btn_frame,text="Save",command=self.add_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn = Button(btn_frame,text="update",command=self.update_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn = Button(btn_frame,text="Delete",command=self.delete_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn = Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        take_pic_btn = Button(btn_frame,text="Take Photo Sample",command=self.generate_dataset,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_pic_btn.grid(row=1,column=1)

        upd_pic_btn = Button(btn_frame,text="Update Photo Sample",width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        upd_pic_btn.grid(row=1,column=2)

        #Right label frame
        Right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=630,y=10,width=610,height=490)

        img_right = Image.open(r"images\f10.png")
        img_right = img_right.resize((600, 100),Image.LANCZOS)
        self.picture_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.picture_right)
        f_lbl.place(x=5,y=0,width=600,height=100)

        # ========Search System=========
        search_frame = LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=110,width=595,height=70)

        search_label = Label(search_frame,text="Search By",font=("times new roman",12,"bold"),bg="yellow",fg="black")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo = ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="read only",width=12)
        search_combo['values']=('Select','Roll_no','Phone_no')
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry = ttk.Entry(search_frame,width=15,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn = Button(search_frame,text="Search",width=10,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn = Button(search_frame,text="Show All",width=10,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)

        table_frame = Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=180,width=595,height=290)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    # ===========Function Declaration
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_stdName.get()=="" or self.var_stdId.get()=="":
           messagebox.showerror("Error","All Fields are required!",parent=self.root) 
        else:
            try:
                conn = mysql.connector.connect(host="localhost",user="root",password="",database="face_attendance")
                mycursor = conn.cursor()
                mycursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_sem.get(),
                                                                                                                self.var_stdId.get(),
                                                                                                                self.var_stdName.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get()
                                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully (:",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)


    # ============Fetch Data===================
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",user="root",password="",database="face_attendance")
        mycursor = conn.cursor()
        mycursor.execute("select * from student")
        data = mycursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # ===========Get Cursor================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_stdId.set(data[4]),
        self.var_stdName.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14]),

    # ============Update Function==============
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_stdName.get() == "" or self.var_stdId.get() == "":
            messagebox.showerror("Error", "All Fields are required!", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update this student details", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="", database="face_attendance")
                    mycursor = conn.cursor()
                    mycursor.execute("update student set dep=%s, course=%s, year=%s, sem=%s, name=%s, division=%s, roll=%s, gender=%s, dob=%s, email=%s, phone=%s, address=%s, teacher=%s, photo_sample=%s where std_id=%s", (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_stdName.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_stdId.get()
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    # =======delete function==========
    def delete_data(self):
        if self.var_stdId.get()=="":
            messagebox.showerror("Error","Student is required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Deleting","Do you want to delete this student details",parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="", database="face_attendance")
                    mycursor = conn.cursor()
                    sql="delete from student where std_id=%s"
                    val=(self.var_stdId.get(),)
                    mycursor.execute(sql,val)

                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    # ============Reset============
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_stdId.set("")
        self.var_stdName.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1 .set("")


    # ===========Generate data set or Take photo sample
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_stdName.get() == "" or self.var_stdId.get() == "":
            messagebox.showerror("Error", "All Fields are required!", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="", database="face_attendance")
                mycursor = conn.cursor()
                mycursor.execute("select * from student where std_id=%s", (self.var_stdId.get(),))
                myresult = mycursor.fetchall()
                id = self.var_stdId.get()
                
                mycursor.execute("update student set dep=%s, course=%s, year=%s, sem=%s, name=%s, division=%s, roll=%s, gender=%s, dob=%s, email=%s, phone=%s, address=%s, teacher=%s, photo_sample=%s where std_id=%s", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_stdName.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    id
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ==========Load predefined data on Face Frontal from openCV============
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    # scaling factor=1.3
                    # minimum neighbor=5

                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped
                    return None

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, myframe = cap.read()
                    if face_cropped(myframe) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(myframe), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating Data sets Completed!!!!")
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)






if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()