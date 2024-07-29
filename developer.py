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

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")  # Adjusted for a 14-inch screen with 1920x1080 resolution
        self.root.title("Student Management System")

        title_lbl = Label(self.root, text="DEVELOPER", font=("times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1550, height=60)

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
        date_label.place(x=200,y=2,width=100,height=60)

        # Call the update_date function to start displaying the date
        update_date()

        #=====================day===============
        def update_day_of_week():
            day_of_week_string = strftime("Day:%A")  # Format for day: Monday, Tuesday, etc.
            day_of_week_label.config(text=day_of_week_string)
            day_of_week_label.after(1000, update_day_of_week)  # Update every 1000 milliseconds (1 second)

        # Create a label to display the day of the week
        day_of_week_label = Label(root, font=("times new roman", 18, "bold"), background="white", foreground="blue")
        day_of_week_label.place(x=300,y=10,width=200,height=40)

        # Call the update_day_of_week function to start displaying the day of the week
        update_day_of_week()

    
        img_top = Image.open(r"C:\Users\Yugant\OneDrive\Desktop\mini project\colleges_images\PathForward-scaled.jpg")
        img_top = img_top.resize((1550, 720), Image.LANCZOS)  # Adjusted dimensions
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1550, height=720)

# leftframe
        main_frame = Frame(f_lbl, bd=2, bg="white")
        main_frame.place(x=250, y=0, width=1100, height=700)

        img_top1 = Image.open(r"C:\Users\Yugant\OneDrive\Desktop\mini project\colleges_images\yugant.png")
        img_top1 = img_top1.resize((200, 200), Image.LANCZOS)  # Adjusted dimensions
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_lbl = Label(main_frame, image=self.photoimg_top1)
        f_lbl.place(x=450, y=20, width=200, height=200)

        
        dev_label_text = "YUGANT DURGAPPA KOULGEKAR.\n USN:2AG21CS126"
        dev_label = Label(main_frame, text=dev_label_text, font=("times new roman", 12, "bold"), bg="white")
        dev_label.place(x=410, y=220)

       

        dev_label1_text = "PROJECT DESCRIPTION:\n\n"\
                  "-The Face Recognition Attendance System is an innovative solution designed for "\
                  "automatically marking attendance using facial recognition technology.\n "\
                  "-It utilizes computer vision algorithms to detect and recognize faces in real-time, allowing "\
                  "effortless attendance management without manual intervention.\n\n"\
                  "Key Features:\n"\
                  "- Real-time face detection and recognition\n"\
                  "- Automated attendance marking\n"\
                  "- Secure and reliable identification\n"\
                  "- Integration with existing student management systems\n"\
                  "- User-friendly interface for easy operation\n\n"\
                  "-This system enhances efficiency by reducing the time and effort required for "\
                  "attendance tracking, making it ideal for educational institutions, organizations,\n "\
                  "and businesses.\n\n"\
                  "Developed by:\nYugant Durgappa Koulgekar\n"\
                  "Version: 1.0\n"\
                  "Date: 20/03/2024\n"\
                  "Contact: 2ag21cs126@gmail.com"

        dev_label1 = Label(main_frame, text=dev_label1_text, font=("times new roman", 12, ), bg="white", justify="left")
        dev_label1.place(x=0, y=280, anchor="nw")




if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()