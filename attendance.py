from tkinter import Tk, Label, Frame, LabelFrame,Toplevel
from tkinter import RIDGE  # Import RIDGE from Tkinter
from PIL import Image, ImageTk
from tkinter import ttk, Button  # Add other imports as needed
from tkinter import BOTTOM, RIGHT
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog
from tkinter import messagebox
from tkinter import Tk, Label, Frame, LabelFrame, Toplevel, StringVar
from time import strftime





mydata=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")  # Adjusted for a 14-inch screen with 1920x1080 resolution
        self.root.title("Attendance Management System")
       
       
 #===================variables=============

        self.var_atten_id = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()
        




# First image
        img = Image.open(r"C:\Users\Yugant\OneDrive\Desktop\mini project\colleges_images\students4.jpg")
        img = img.resize((800, 200), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=800, height=200)

# Second image
        img1 = Image.open(r"C:\Users\Yugant\OneDrive\Desktop\mini project\colleges_images\student3.jpg")
        img1 = img1.resize((800, 200), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=800, y=0, width=800, height=200)

 # Background image
        img3 = Image.open(r"C:\Users\Yugant\OneDrive\Desktop\mini project\colleges_images\background.webp")
        img3 = img3.resize((1920, 750), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=200, width=1920, height=750)

        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=60)

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
        date_label.place(x=190,y=214,width=100,height=40)

        # Call the update_date function to start displaying the date
        update_date()   

        def update_day_of_week():
            day_of_week_string = strftime("Day:%A")  # Format for day: Monday, Tuesday, etc.
            day_of_week_label.config(text=day_of_week_string)
            day_of_week_label.after(1000, update_day_of_week)  # Update every 1000 milliseconds (1 second)

        # Create a label to display the day of the week
        day_of_week_label = Label(root, font=("times new roman", 18, "bold"), background="white", foreground="blue")
        day_of_week_label.place(x=1250,y=220,width=200,height=40)

        # Call the update_day_of_week function to start displaying the day of the week
        update_day_of_week()

#main frame
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=0, y=60, width=1600, height=600)

        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details", font=("times new roman", 13, "bold"))
        Left_frame.place(x=40, y=10, width=705, height=480)

        img_left = Image.open(r"C:\Users\Yugant\OneDrive\Desktop\mini project\colleges_images\Attendance.1jpg.jpg")
        img_left = img_left.resize((705, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=10, y=0, width=680, height=130)

        left_inside_frame = Frame(Left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=10, y=140, width=680, height=310)


# labels and entrys
#attendanceid  
        attendanceId_label=Label(left_inside_frame,text="Attendance ID:",font=("times new roman", 12, "bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky="w")

        attendanceId_entry = ttk.Entry(left_inside_frame, width=17,textvariable=self.var_atten_id ,font=("times new roman",13,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky="w")

 #name  
        namelabel=Label(left_inside_frame,text="Name:",font=("comicsansns", 12, "bold"),bg="white")
        namelabel.grid(row=1,column=0)

        atten_name = ttk.Entry(left_inside_frame, width=17,textvariable=self.var_atten_name ,font=("comicsansns",13,"bold"))
        atten_name.grid(row=1,column=1,padx=10,pady=8)

#dep
        deplabel=Label(left_inside_frame,text="Department:",font=("comicsansns", 12, "bold"),bg="white")
        deplabel.grid(row=0,column=2)

        atten_dep = ttk.Entry(left_inside_frame, width=17,textvariable=self.var_atten_dep ,font=("comicsansns",13,"bold"))
        atten_dep.grid(row=0,column=3,padx=10,pady=8)

#time
        timelabel=Label(left_inside_frame,text="Time:",font=("comicsansns", 12, "bold"),bg="white")
        timelabel.grid(row=2,column=0)

        atten_time = ttk.Entry(left_inside_frame, width=17,textvariable=self.var_atten_time ,font=("comicsansns",13,"bold"))
        atten_time.grid(row=2,column=1,pady=8)

#date
        datelabel=Label(left_inside_frame,text="Date:",font=("comicsansns", 12, "bold"),bg="white")
        datelabel.grid(row=1,column=2)

        atten_date = ttk.Entry(left_inside_frame, width=17,textvariable=self.var_atten_date ,font=("comicsansns",13,"bold"))
        atten_date.grid(row=1,column=3,pady=8)

#attendance
       #attendance
        attendancelabel=Label(left_inside_frame,text="Attendance Status:",font=("comicsansns", 12, "bold"),bg="white")
        attendancelabel.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,width=17,textvariable=self.var_atten_attendance,font=("comicsansns", 11, "bold"),state="readonly")
        self.atten_status["values"]=("Status", "Present", "Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=60, y=270, width=550, height=35)

        save_btn = Button(btn_frame, text="Import csv", command=self.importcsv, width=20, font=("comicsansns", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Export csv", command=self.exportCsv, width=16, font=("comicsansns", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        reset_btn = Button(btn_frame, text="Reset", width=16,command=self.reset_data ,font=("comicsansns", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)



# If you want to evenly distribute the buttons across the frame, you can use relwidth=1/3 for each button.



#right side label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("comicsansns", 13, "bold"))
        Right_frame.place(x=765, y=10, width=700, height=480)

        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=2, width=685, height=450)

        scroll_x = ttk.Scrollbar(table_frame, orient="horizontal")
        scroll_y = ttk.Scrollbar(table_frame, orient="vertical")

        self.AttendanceReportTable = ttk.Treeview(table_frame, columns=("id", "name", "department", "time", "date", "attendance"),
                                                  xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side="bottom", fill="x")
        scroll_y.pack(side="right", fill="y")

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        


        self.AttendanceReportTable.pack(fill="both", expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)


#=============================fetch data==================================
        
    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
           self.AttendanceReportTable.insert("", "end", values=i)



    # importcsv method
    def importcsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open csv", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)
        if fln:
             with open(fln) as myfile:
                csvread = csv.reader(myfile, delimiter=",")
                for i in csvread:
                        mydata.append(i)
             self.fetchData(mydata)

# exportCsv method
    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No data", "No data found to export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open csv", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)
            if fln:
                with open(fln, mode="w", newline="") as myfile:
                      exp_write = csv.writer(myfile, delimiter=",")
                      for i in mydata:
                          exp_write.writerows(i)
                messagebox.showinfo("Data export", f"Your data exported to {os.path.basename(fln)} successfully")
        except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']

        if rows and len(rows) >= 6:  # Check if rows is not empty and has at least 6 elements
                self.var_atten_id.set(rows[0])
                self.var_atten_name.set(rows[1])
                self.var_atten_dep.set(rows[2])
                self.var_atten_time.set(rows[3])
                self.var_atten_date.set(rows[4])
                self.var_atten_attendance.set(rows[5])
        else:
                # Handle the case where rows is empty or doesn't have enough elements
                # You might want to reset the variables or display a message
                self.var_atten_id.set("")
                self.var_atten_name.set("")
                self.var_atten_dep.set("")
                self.var_atten_time.set("")
                self.var_atten_date.set("")
                self.var_atten_attendance.set("")


    def update_data(self):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        selected_values = content['values']

        if not selected_values:
            messagebox.showerror("Error", "No data selected for update!",parent=self.root)
            return

        selected_index = selected_values[0]

        # Collect the updated data from the entry fields
        updated_row = [selected_index, self.var_atten_name.get(), self.var_atten_dep.get(),
                       self.var_atten_time.get(), self.var_atten_date.get(), self.var_atten_attendance.get()]

        # Find the index of the selected data in mydata
        index_to_update = None
        for index, row in enumerate(mydata):
            if row and row[0] == selected_index:
                index_to_update = index
                break

        if index_to_update is not None:
            # Update the data in the mydata list
            mydata[index_to_update] = updated_row

            # Update the Treeview widget
            self.fetchData(mydata)

            # Save the updated data back to the CSV file
            try:
                fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save Updated CSV",
                                                    filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")),
                                                    parent=self.root)
                if fln:
                    with open(fln, mode="w", newline="") as myfile:
                        exp_write = csv.writer(myfile, delimiter=",")
                        exp_write.writerows(mydata)

                    messagebox.showinfo("Update", "Data updated successfully and saved to CSV file!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Unable to save updated data to CSV: {str(es)}",parent=self.root)
        else:
            messagebox.showerror("Error", f"Data with ID {selected_index} not found for update!",parent=self.root)


    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
         
if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()