import tkinter as tk
from tkinter import Tk, Label, Button
from PIL import Image, ImageTk
from tkinter import*
from PIL import Image, ImageTk
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
import tkinter as tk
from time import strftime
from datetime import datetime



class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")  # Adjusted for a 14-inch screen with 1920x1080 resolution
        self.root.title("Face Recognition System")



# First image
        img = Image.open(r"C:\Users\Yugant\OneDrive\Desktop\mini project\colleges_images\BestFacialRecognition.jpg")
        img = img.resize((500, 130), Image.LANCZOS)  # Adjusted dimensions
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)
# Second image
        img1 = Image.open(r"C:\Users\Yugant\OneDrive\Desktop\mini project\colleges_images\facialrecognition.jpg")
        img1 = img1.resize((500, 130), Image.LANCZOS)  # Adjusted dimensions
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=500, y=0, width=500, height=130)

# Third image
        img2 = Image.open(r"C:\Users\Yugant\OneDrive\Desktop\mini project\colleges_images\login.jpg")
        img2 = img2.resize((550, 130), Image.LANCZOS)  # Adjusted dimensions
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=1000, y=0, width=550, height=130)

# Background image
        img3 = Image.open(r"C:\Users\Yugant\OneDrive\Desktop\mini project\colleges_images\mainbackground.png")
        img3 = img3.resize((1920, 720), Image.LANCZOS)  # Adjusted dimensions
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=100, width=1920, height=880)

        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("times new roman", 35, "bold"),bg="white", fg="orange")
        title_lbl.place(x=0, y=0, width=1600, height=80)


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
        date_label.place(x=65,y=150,width=100,height=20)

        # Call the update_date function to start displaying the date
        update_date() 

        #=====================day===============
        def update_day_of_week():
            day_of_week_string = strftime("Day:%A")  # Format for day: Monday, Tuesday, etc.
            day_of_week_label.config(text=day_of_week_string)
            day_of_week_label.after(1000, update_day_of_week)  # Update every 1000 milliseconds (1 second)

        # Create a label to display the day of the week
        day_of_week_label = Label(root, font=("times new roman", 20, "bold"), background="white", foreground="blue")
        day_of_week_label.place(x=1310,y=120,width=200,height=40)

        # Call the update_day_of_week function to start displaying the day of the week
        update_day_of_week()


# Student button
        img4 = Image.open(r"C:\Users\Yugant\OneDrive\Desktop\mini project\colleges_images\student.jpg")
        img4 = img4.resize((250, 250), Image.LANCZOS)  # Adjusted dimensions
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4,command=self.student_details,cursor="hand2")  # Use 'Button' instead of 'button'
        b1.place(x=200, y=100, width=250, height=250)

        b1_1 = Button(bg_img, text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman", 25, "bold"),bg="darkblue", fg="white") # Use 'Button' instead of 'button'
        b1_1.place(x=200, y=310, width=250, height=40)

 # detect face button
        img5 = Image.open(r"C:\Users\Yugant\OneDrive\Desktop\mini project\colleges_images\face dectector.jpg")
        img5 = img5.resize((250, 250), Image.LANCZOS)  # Adjusted dimensions
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5,cursor="hand2",command=self.face_data)  # Use 'Button' instead of 'button'
        b1.place(x=500, y=100, width=250, height=250)

        b1_1 = Button(bg_img, text="Face Dectector",cursor="hand2",command=self.face_data,font=("times new roman", 25, "bold"),bg="darkblue", fg="white") # Use 'Button' instead of 'button'
        b1_1.place(x=500, y=310, width=250, height=40)

 # attendance face button
        img6 = Image.open(r"C:\Users\Yugant\OneDrive\Desktop\mini project\colleges_images\Attendance.jpg")
        img6 = img6.resize((250, 250), Image.LANCZOS)  # Adjusted dimensions
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6,cursor="hand2",command=self.attendance_data)  # Use 'Button' instead of 'button'
        b1.place(x=800, y=100, width=250, height=250)

        b1_1 = Button(bg_img, text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman", 25, "bold"),bg="darkblue", fg="white") # Use 'Button' instead of 'button'
        b1_1.place(x=800, y=310, width=250, height=40)
        

# help desk
        img7 = Image.open(r"C:\Users\Yugant\OneDrive\Desktop\mini project\colleges_images\help desk.jpg")
        img7 = img7.resize((250, 250), Image.LANCZOS)  # Adjusted dimensions
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimg7,cursor="hand2",command=self.help_data)  # Use 'Button' instead of 'button'
        b1.place(x=1100, y=100, width=250, height=250)

        b1_1 = Button(bg_img, text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman", 25, "bold"),bg="darkblue", fg="white") # Use 'Button' instead of 'button'
        b1_1.place(x=1100, y=310, width=250, height=40)

# train data
        img8 = Image.open(r"C:\Users\Yugant\OneDrive\Desktop\mini project\colleges_images\train data.jpg")
        img8 = img8.resize((250, 250), Image.LANCZOS)  # Adjusted dimensions
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8,cursor="hand2",command=self.train_data)  # Use 'Button' instead of 'button'
        b1.place(x=200, y=380, width=250, height=200)

        b1_1 = Button(bg_img, text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman", 25, "bold"),bg="darkblue", fg="white") # Use 'Button' instead of 'button'
        b1_1.place(x=200, y=580, width=250, height=40)

# photos
        img9 = Image.open(r"C:\Users\Yugant\OneDrive\Desktop\mini project\colleges_images\photos.jpg")
        img9 = img9.resize((250, 250), Image.LANCZOS)  # Adjusted dimensions
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9,cursor="hand2",command=self.open_img)  # Use 'Button' instead of 'button'
        b1.place(x=500, y=380, width=250, height=200)

        b1_1 = Button(bg_img, text="photos",cursor="hand2",command=self.open_img,font=("times new roman", 25, "bold"),bg="darkblue", fg="white") # Use 'Button' instead of 'button'
        b1_1.place(x=500, y=580, width=250, height=40)

# Developer
        img10 = Image.open(r"C:\Users\Yugant\OneDrive\Desktop\mini project\colleges_images\developer.png")
        img10 = img10.resize((250, 250), Image.LANCZOS)  # Adjusted dimensions
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimg10,cursor="hand2",command=self.developer_data)  # Use 'Button' instead of 'button'
        b1.place(x=800, y=380, width=250, height=200)

        b1_1 = Button(bg_img, text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman", 25, "bold"),bg="darkblue", fg="white") # Use 'Button' instead of 'button'
        b1_1.place(x=800, y=580, width=250, height=40)

# exit
        img11 = Image.open(r"C:\Users\Yugant\OneDrive\Desktop\mini project\colleges_images\exit.jpg")
        img11 = img11.resize((250, 250), Image.LANCZOS)  # Adjusted dimensions
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photoimg11,cursor="hand2",command=self.iExit)  # Use 'Button' instead of 'button'
        b1.place(x=1100, y=380, width=250, height=200)

        b1_1 = Button(bg_img, text="Exit",cursor="hand2",command=self.iExit,font=("times new roman", 25, "bold"),bg="darkblue", fg="white") # Use 'Button' instead of 'button'
        b1_1.place(x=1100, y=580, width=250, height=40)     

    def open_img(self):
        os.startfile("data")


    def iExit(self):
        result = tk.messagebox.askyesno("Face Recognition", "Are you sure you want to exit the project?",parent=self.root)
        if result:
           self.root.destroy()





#=================Functions=======================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)

if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognitionSystem(root)
    root.mainloop()