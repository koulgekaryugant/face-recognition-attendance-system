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
import os
import numpy as np
from time import strftime



class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")  # Adjusted for a 14-inch screen with 1920x1080 resolution
        self.root.title("Student Management System")

        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 35, "bold"), bg="white", fg="red")
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
        date_label.place(x=190,y=2,width=100,height=60)

        # Call the update_date function to start displaying the date
        update_date()

        #=====================day===============
        def update_day_of_week():
            day_of_week_string = strftime("Day:%A")  # Format for day: Monday, Tuesday, etc.
            day_of_week_label.config(text=day_of_week_string)
            day_of_week_label.after(1000, update_day_of_week)  # Update every 1000 milliseconds (1 second)

        # Create a label to display the day of the week
        day_of_week_label = Label(root, font=("times new roman", 16, "bold"), background="white", foreground="blue")
        day_of_week_label.place(x=300,y=10,width=200,height=40)

        # Call the update_day_of_week function to start displaying the day of the week
        update_day_of_week()

# Functions related to adding images and labels
        img_top = Image.open(r"C:\Users\Yugant\OneDrive\Desktop\mini project\colleges_images\240_F_266612851_MIUeQoitxam80X7OrF2oudGcdMwZexar.jpg")
        img_top = img_top.resize((1550, 325), Image.LANCZOS)  # Adjusted dimensions
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1550, height=325)

#button
        b1_1 = Button(self.root, text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman", 25, "bold"),bg="red", fg="white") # Use 'Button' instead of 'button'
        b1_1.place(x=0, y=380, width=1550, height=70)

        img_down = Image.open(r"C:\Users\Yugant\OneDrive\Desktop\mini project\colleges_images\240_F_266612851_MIUeQoitxam80X7OrF2oudGcdMwZexar.jpg")
        img_down = img_down.resize((1550, 325), Image.LANCZOS)  # Adjusted dimensions
        self.photoimg_down = ImageTk.PhotoImage(img_down)

        f_lbl = Label(self.root, image=self.photoimg_down)
        f_lbl.place(x=0, y=450, width=1550, height=325)


    def train_classifier(self):
        data_dir=("data")
        path=[ os.path.join(data_dir,file) for file in os.listdir(data_dir)] #list compherension

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert("L") #gray scale image
            imageNp=np.array(img,"uint8")
            id=int(os.path.split(image)[1].split('.')[1])
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)


        #==============================train the classfier=======================
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Training Completed", "Training dataset completed!",parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()