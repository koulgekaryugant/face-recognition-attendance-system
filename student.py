from tkinter import Tk, Label, Frame, LabelFrame
from tkinter import RIDGE  # Import RIDGE from Tkinter
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import Tk, Button, Frame  # Add other imports as needed
from tkinter import BOTTOM, RIGHT
from tkinter import messagebox
from tkinter import Tk, StringVar
import mysql.connector
import cv2
from time import strftime



class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")  # Adjusted for a 14-inch screen with 1920x1080 resolution
        self.root.title("Student Management System")


       #============================variables==================================
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()  # Fix the typo in StringVar
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()  # Fix the typo in StringVar
        self.var_address = StringVar()  # Fix the typo in StringVar
        self.var_teacher = StringVar()
        




# First image
        img = Image.open(r"C:\Users\Yugant\OneDrive\Desktop\mini project\colleges_images\images.jpg")
        img = img.resize((500, 130), Image.LANCZOS)  # Adjusted dimensions
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

# Second image
        img1 = Image.open(r"C:\Users\Yugant\OneDrive\Desktop\mini project\colleges_images\abstract-facial-recognition-blue-background_23-2148202196.jpg")
        img1 = img1.resize((500, 130), Image.LANCZOS)  # Adjusted dimensions
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)

# Third image
        img2 = Image.open(r"C:\Users\Yugant\OneDrive\Desktop\mini project\colleges_images\train data.jpg")
        img2 = img2.resize((550, 130), Image.LANCZOS)  # Adjusted dimensions
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl= Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=550, height=130)

 # Background image
        img3 = Image.open(r"C:\Users\Yugant\OneDrive\Desktop\mini project\colleges_images\background.webp")
        img3 = img3.resize((1920, 750), Image.LANCZOS)  # Adjusted dimensions
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1920, height=880)

        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1600, height=60)

        #=================time==================
        def time():
            string= strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_lbl,font=("times new roman",16,"bold"),background="white",foreground="blue")
        lbl.place(x=10,y=0,width=200,height=60)
        time() 

        #==================date========================
        def update_date():
            date_string = strftime("%d-%m-%Y")  # Format for date: day-month-year
            date_label.config(text=date_string)
            date_label.after(1000, update_date)  # Update the date every 1000 milliseconds (1 second)

        # Create a label to display the date
        date_label = Label(root, font=("times new roman", 16, "bold"), background="white", foreground="blue")
        date_label.place(x=200,y=154,width=100,height=20)

        # Call the update_date function to start displaying the date
        update_date()  

        #=====================day===============
        def update_day_of_week():
            day_of_week_string = strftime("Day:%A")  # Format for day: Monday, Tuesday, etc.
            day_of_week_label.config(text=day_of_week_string)
            day_of_week_label.after(1000, update_day_of_week)  # Update every 1000 milliseconds (1 second)

        # Create a label to display the day of the week
        day_of_week_label = Label(root, font=("times new roman", 18, "bold"), background="white", foreground="blue")
        day_of_week_label.place(x=1300,y=145,width=200,height=40)

        # Call the update_day_of_week function to start displaying the day of the week
        update_day_of_week()

#main frame
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=10, y=70, width=1500, height=650)

# Left side label frame
        Left_frame = LabelFrame(main_frame, bd=2,bg="white",relief=RIDGE, text="Student Details", font=("times new roman", 13, "bold"))
        Left_frame.place(x=40, y=10, width=705, height=565)

        img_left = Image.open(r"C:\Users\Yugant\OneDrive\Desktop\mini project\colleges_images\student details.jpg")
        img_left = img_left.resize((705, 130), Image.LANCZOS)  # Adjusted dimensions
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=10, y=0, width=680, height=130)

#current course
        current_course_frame = LabelFrame(Left_frame, bd=2,bg="white",relief=RIDGE, text="Current Course information", font=("times new roman", 13, "bold"))
        current_course_frame.place(x=5, y=120, width=691, height=120)

#department
        dep_label=Label(current_course_frame,text="Department:",font=("times new roman", 12, "bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman", 12, "bold"),width=17,state="read only")
        dep_combo["values"]=("Select Department","Computer Science","Electronics and Communication","Electrical","Mechanical","Civil","Robotics And Automation","Artifical Intelligence and Data Science")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

# Course
        course_label = Label(current_course_frame, text="Course:", font=("times new roman", 12, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10)

        course_value_label = Label(current_course_frame, text="Bachelor of Engineering", font=("times new roman", 12, "bold"), bg="white")
        course_value_label.grid(row=0, column=3)

# Year
        year_label = Label(current_course_frame, text="Year:", font=("times new roman", 12, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=("times new roman", 12, "bold"), width=17, state="readonly")
        year_combo["values"] = ("Select Year", "2020-21", "2021-22", "2022-23", "2023-24")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky="w")

# Semester
        semester_label = Label(current_course_frame, text="Semester:", font=("times new roman", 12, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10)

        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, font=("times new roman", 12, "bold"), width=20, state="readonly")
        semester_combo["values"] = ("Select Semester", "Semester-1", "Semester-2", "Semester-3", "Semester-4", "Semester-5", "Semester-6", "Semester-7", "Semester-8")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky="w")


#class student information
        class_student_frame = LabelFrame(Left_frame, bd=2,bg="white",relief=RIDGE, text="Class Student Infromation", font=("times new roman", 13, "bold"))
        class_student_frame.place(x=5, y=250, width=691, height=290)

#student ID
        studentId_label=Label(class_student_frame,text="Student ID:",font=("times new roman", 12, "bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky="w")

        studentId_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_id, width=17, font=("times new roman",13,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky="w")

#student name
        studentName_label=Label(class_student_frame,text="Student Name:",font=("times new roman", 12, "bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky="w")

        studentName_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_name ,width=17, font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky="w")

#class division
        class_div_label=Label(class_student_frame,text=" Division:",font=("times new roman", 12, "bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky="w")

        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman", 12, "bold"),width=17,state="read only")
        div_combo["values"]=( "Select","A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky="w")


#roll no
        roll_no_label=Label(class_student_frame,text="Roll no:",font=("times new roman", 12, "bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky="w")

        roll_no_entry = ttk.Entry(class_student_frame,textvariable=self.var_roll ,width=17, font=("times new roman",13,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky="w")

#gender
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman", 12, "bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky="w")

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman", 12, "bold"),width=17,state="read only")
        gender_combo["values"]=("Select","Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky="w")

#date of birth
        dob_label=Label(class_student_frame,text="DOB:",font=("times new roman", 12, "bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky="w")

        dob_entry = ttk.Entry(class_student_frame,textvariable=self.var_dob ,width=17, font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky="w")

#Email
        email_label=Label(class_student_frame,text="Email:",font=("times new roman", 12, "bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky="w")

        email_entry = ttk.Entry(class_student_frame,textvariable=self.var_email ,width=17, font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky="w")

#phone no
        phone_label=Label(class_student_frame,text="Phone no:",font=("times new roman", 12, "bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky="w")

        phone_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone,width=17, font=("times new roman",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky="w")

#address
        address_label=Label(class_student_frame,text="Address:",font=("times new roman", 12, "bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky="w")

        address_entry = ttk.Entry(class_student_frame,textvariable=self.var_address ,width=17, font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky="w")

#Teacher name
        teacher_label=Label(class_student_frame,text="Teacher Name:",font=("times new roman", 12, "bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky="w")

        teacher_entry = ttk.Entry(class_student_frame,textvariable=self.var_teacher ,width=17, font=("times new roman",13,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky="w")

#radio buttons
        self.var_radio1=StringVar()
        radiobt1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take a Photo Sample",value="Yes")
        radiobt1.grid(row=6,column=0)

        radiobt2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="NO")
        radiobt2.grid(row=6,column=1)

#button frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=200,width=675,height=35)

        save_btn = Button(btn_frame, text="Save",command=self.add_data,width=16, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)
        
        update_btn = Button(btn_frame, text="Update",command=self.update_data,width=16, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete",command=self.delete_data,width=16, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data,width=16, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=5,y=232,width=675,height=30)

        take_photo_btn = Button(btn_frame1, command=self.generate_dataset,text="Take a Photo",width=33, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        take_photo_btn.place(relx=0, rely=0, relwidth=1, relheight=1)

#right side label frame
        Right_frame = LabelFrame(main_frame, bd=2,bg="white",relief=RIDGE, text="Student Details", font=("times new roman", 13, "bold"))
        Right_frame.place(x=765, y=10, width=700, height=565)

        img_right = Image.open(r"C:\Users\Yugant\OneDrive\Desktop\mini project\colleges_images\student details2.jpg")
        img_right = img_right.resize((705, 130), Image.LANCZOS)  # Adjusted dimensions
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=10, y=0, width=680, height=120)


#=======================================================search system===============================================

        Search_frame = LabelFrame(Right_frame, bd=2,bg="white",relief=RIDGE, text="Search System", font=("times new roman", 13, "bold"))
        Search_frame.place(x=5, y=120, width=687, height=70)

        search_label=Label(Search_frame,text="Search By:",font=("times new roman", 15, "bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky="w")

        search_combo=ttk.Combobox(Search_frame, font=("times new roman", 12, "bold"), width=20, state="read only")
        search_combo["values"]=("Select","Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky="w")

        search_entry = ttk.Entry(Search_frame, width=14, font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky="w")
        
        search_btn = Button(Search_frame, text="Search", width=10 ,font=("times new roman", 12, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3,padx=4,pady=1)


#============table frame================
        table_frame = Frame(Right_frame, bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5, y=195, width=687, height=345)

        scroll_x=ttk.Scrollbar(table_frame,orient="horizontal")
        scroll_y=ttk.Scrollbar(table_frame,orient="vertical")
        self.student_table = ttk.Treeview(root)

        self.student_table = ttk.Treeview(table_frame, columns=("dep", "course", "year", "sem", "id", "name", "div", "roll", "gender", "dob", "email", "phone", "address", "teacher", "photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set )
        scroll_x.pack(side=BOTTOM, fill="x")
        scroll_y.pack(side=RIGHT, fill="y")
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

      
# Set the heading for each column

        self.student_table["columns"] = ("dep", "course", "year", "sem", "id", "name", "div", "roll", "gender", "dob", "email", "phone", "address", "teacher", "photo")
        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Sem")
        self.student_table.heading("id", text="Student Id")
        self.student_table.heading("name", text="Student Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll no") # Add this line
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone no")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher name")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"
         
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)






        self.student_table.pack(fill="both", expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

#======================FUNCTION DECLARATION===================

    def add_data(self):
        if self.var_dep.get()=="select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("ERROR","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_id.get(),
                                                                                                                self.var_std_name.get(),
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
                messagebox.showinfo("Success","Students details has been added Sucessfully",parent=self.root)     
            except Exception as es:
                messagebox.showinfo("ERROR",f"Due to:{str(es)}",parent=self.root)
       
#=============fetch data=========================
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Test@123", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("","end", values=i)
            conn.commit()
        conn.close()



#==========================get cursor================================
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        print(data)  # Add this line to debug

    # Rest of the method...


        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

#==========================update function===========================
    def update_data(self):
        if self.var_dep.get()=="select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("ERROR","All Fields are required",parent=self.root)
        else:
                Update = messagebox.askyesno("Update", "Do you want to update this student details ", parent=self.root)
                if Update == 1:
                    # Your database update code here
                    conn = mysql.connector.connect(host="localhost", username="root", password="Test@123", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dep=%s, course=%s, Year=%s, Semester=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where Student_id=%s", (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                    ))

                    messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                        

        





# delete function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("student delete page","do u want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due TO:{str(es)}",parent=self.root)


                #reset

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Selet Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select")
        self.var_roll.set("")
        self.var_gender.set("Select")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")      


#=======================================Generate data set or Take photo samples===============================
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("ERROR", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Test@123",
                                               database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select *from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute(
    "UPDATE student SET Dep=%s, Course=%s, Year=%s, Semester=%s, Division=%s, Roll=%s, Gender=%s, "
    "Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s WHERE Student_id=%s",
    (
        self.var_dep.get(),
        self.var_course.get(),
        self.var_year.get(),
        self.var_semester.get(),
        self.var_div.get(),
        self.var_roll.get(),
        self.var_gender.get(),
        self.var_dob.get(),
        self.var_email.get(),
        self.var_phone.get(),
        self.var_address.get(),
        self.var_teacher.get(),
        self.var_radio1.get(),
        id + 1  # Fix the assignment here
    ))

                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #=================================Load predefined data on face frontals from opencv=====================

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #minimum neighbour=5
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)


                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()

                messagebox.showinfo("Result","Generating data set completed !!!!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due TO:{str(es)}",parent=self.root)

    
if __name__ == "__main__":
       root = Tk()
       obj = Student(root)
       root.mainloop()
