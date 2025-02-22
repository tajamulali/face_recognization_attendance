from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


myData=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognition System")

        #=================Variables=================

        self.var_attenId = StringVar()
        self.var_attenName = StringVar()
        self.var_attenRoll = StringVar()
        self.var_attenDep = StringVar()
        self.var_attenTime = StringVar()
        self.var_attenDate = StringVar()
        self.var_attendance = StringVar()


        img = Image.open(r"images\f15.jpg")
        img = img.resize((700, 150),Image.LANCZOS)
        self.picture = ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.picture)
        f_lbl.place(x=0,y=0,width=700,height=150)

        img1 = Image.open(r"images\f12.jpg")
        img1 = img1.resize((700, 150),Image.LANCZOS)
        self.picture1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.picture1)
        f_lbl.place(x=700,y=0,width=700,height=150)

        # background image
        img3 = Image.open(r"images\f9.png")
        img3 = img3.resize((1400,590),Image.LANCZOS)
        self.picture3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.picture3)
        bg_img.place(x=0,y=150,width=1400,height=590)

        # title of system
        title_lbl = Label(bg_img,text="Attendance Management",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1300,height=40)

        # ======Main Frame========
        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=50,width=1250,height=480)

        #left label frame
        Left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=5,y=10,width=615,height=460)

        img_left = Image.open(r"images\f20.jpg")
        img_left = img_left.resize((600, 110),Image.LANCZOS)
        self.picture_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.picture_left)
        f_lbl.place(x=5,y=0,width=600,height=110)

        left_inside_frame = Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=5,y=120,width=600,height=150)

        # Label & entries
        # Attendance ID
        stuId_label = Label(left_inside_frame,text="Attendance Id",font=("times new roman",11,"bold"),bg="white")
        stuId_label.grid(row=0,column=0,padx=10,pady=2,sticky=W)

        stuId_entry = ttk.Entry(left_inside_frame,textvariable=self.var_attenId,width=20,font=("times new roman",11,"bold"))
        stuId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # Name
        stuName_label = Label(left_inside_frame,text="Name",font=("times new roman",11,"bold"),bg="white")
        stuName_label.grid(row=0,column=2,padx=10,pady=2,sticky=W)

        stuName_entry = ttk.Entry(left_inside_frame,textvariable=self.var_attenName,width=20,font=("times new roman",11,"bold"))
        stuName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # RoLL NUmber
        sturoll_label = Label(left_inside_frame,text="Name",font=("times new roman",11,"bold"),bg="white")
        sturoll_label.grid(row=1,column=0,padx=10,pady=2,sticky=W)

        sturoll_entry = ttk.Entry(left_inside_frame,textvariable=self.var_attenRoll,width=20,font=("times new roman",11,"bold"))
        sturoll_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        # Department
        stuDep_label = Label(left_inside_frame,text="Name",font=("times new roman",11,"bold"),bg="white")
        stuDep_label.grid(row=1,column=2,padx=10,pady=2,sticky=W)

        stuDep_entry = ttk.Entry(left_inside_frame,textvariable=self.var_attenDep,width=20,font=("times new roman",11,"bold"))
        stuDep_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        # Time
        attenTime_label = Label(left_inside_frame,text="Name",font=("times new roman",11,"bold"),bg="white")
        attenTime_label.grid(row=2,column=0,padx=10,pady=2,sticky=W)

        attenTime_entry = ttk.Entry(left_inside_frame,textvariable=self.var_attenTime,width=20,font=("times new roman",11,"bold"))
        attenTime_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        # Date
        attenDate_label = Label(left_inside_frame,text="Name",font=("times new roman",11,"bold"),bg="white")
        attenDate_label.grid(row=2,column=2,padx=10,pady=2,sticky=W)

        attenDate_entry = ttk.Entry(left_inside_frame,textvariable=self.var_attenDate,width=20,font=("times new roman",11,"bold"))
        attenDate_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # Attendance
        attendance_label = Label(left_inside_frame,text="Name",font=("times new roman",11,"bold"),bg="white")
        attendance_label.grid(row=3,column=0,padx=10,pady=2,sticky=W)

        self.attenStatus=ttk.Combobox(left_inside_frame,textvariable=self.var_attendance,width=20,font=("comicsansns",11,"bold"),state="readonly")
        self.attenStatus["values"]=("Status","Present","Absent")
        self.attenStatus.grid(row=3,column=1,padx=10,pady=10)
        self.attenStatus.current(0)

        #Button Frame
        btn_frame = Frame(Left_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=170,y=340,width=265,height=70)

        import_btn = Button(btn_frame,text="import csv",command=self.importCsv,width=12,font=("times new roman",13,"bold"),bg="blue",fg="white")
        import_btn.grid(row=0,column=1)

        export_btn = Button(btn_frame,text="Export csv",command=self.exportCsv,width=12,font=("times new roman",13,"bold"),bg="blue",fg="white")
        export_btn.grid(row=0,column=2)

        update_btn = Button(btn_frame,text="update",command=self.update_data,width=12,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=1,column=1)

        reset_btn = Button(btn_frame,text="Reset",command=self.reset_data,width=12,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=1,column=2)


        #Right label frame
        Right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=630,y=10,width=610,height=465)

        table_frame = Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=5,width=595,height=415)

        # ===========scrollbar table==============
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","name","roll","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("department",text="Derpartment")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)


        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    #==============Fetch data===========
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    # Import CSV
    def importCsv(self):
        global myData
        myData.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                myData.append(i)
            self.fetchData(myData)

    # Export CSV
    def exportCsv(self):
        try:
            if len(myData)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in myData:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data Exported to "+os.path.basename(fln)+" successfully")
        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_attenId.set(rows[0])
        self.var_attenName.set(rows[1])
        self.var_attenRoll.set(rows[2])
        self.var_attenDep.set(rows[3])
        self.var_attenTime.set(rows[4])
        self.var_attenDate.set(rows[5])
        self.var_attendance.set(rows[6])

    # =============Reset Funtion==============
    def reset_data(self):
        self.var_attenId.set("")
        self.var_attenName.set("")
        self.var_attenRoll.set("")
        self.var_attenDep.set("")
        self.var_attenTime.set("")
        self.var_attenDate.set("")
        self.var_attendance.set("")


    # =============Update Funtion==============
    def update_data(self):
        try:
            if self.var_attenId.get() == "":
                messagebox.showerror("Error", "Attendance ID must be provided", parent=self.root)
                return

            # Fetch updated data from the form
            updated_row = [
                self.var_attenId.get(),
                self.var_attenName.get(),
                self.var_attenRoll.get(),
                self.var_attenDep.get(),
                self.var_attenTime.get(),
                self.var_attenDate.get(),
                self.var_attendance.get(),
            ]

            # Ensure data exists in the table
            if not myData:
                messagebox.showerror("Error", "No data available to update", parent=self.root)
                return
            
            # Update the data in myData
            for index, row in enumerate(myData):
                if len(row) > 0 and row[0] == self.var_attenId.get():  # Match by Attendance ID
                    myData[index] = updated_row
                    break
            else:
                messagebox.showerror("Error", "Attendance ID not found in the data", parent=self.root)
                return

            # Refresh the Treeview to reflect updated data
            self.fetchData(myData)
            messagebox.showinfo("Success", "Table updated successfully!", parent=self.root)

        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)





if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()