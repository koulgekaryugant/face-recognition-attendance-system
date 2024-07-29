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
from datetime import datetime
import csv 

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")  
        self.root.title("Student Management System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1550, height=60)

        img_top = Image.open(r"C:\Users\Yugant\OneDrive\Desktop\mini project\colleges_images\istockphoto-1139859542-170667a.jpg")
        img_top = img_top.resize((650, 700), Image.LANCZOS) 
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=700)

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
        date_label.place(x=190,y=12,width=100,height=40)

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

        img_down = Image.open(r"C:\Users\Yugant\OneDrive\Desktop\mini project\colleges_images\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img_down = img_down.resize((950, 700), Image.LANCZOS) 
        self.photoimg_down = ImageTk.PhotoImage(img_down)

        f_lbl = Label(self.root, image=self.photoimg_down)
        f_lbl.place(x=650, y=55, width=950, height=700)

        #button
        b1_1 = Button(self.root, text="Face Recognition", cursor="hand2", font=("times new roman", 18, "bold"), bg="darkgreen", fg="white", command=self.face_recog)
        b1_1.place(x=1025, y=680, width=200, height=40)  # Adjust the x coordinate

        self.last_marked_time = {}  # Dictionary to store last marked time for each student

#====================================attendance===========================
#current_datetime: This variable stores the current date and time using datetime.now() from the datetime module.
#current_date: It extracts and formats the current date in the format "day/month/year" using strftime.
#current_hour: It extracts and formats the current hour in 24-hour format using strftime.
    def mark_attendance(self, student_id, name, department, remove=False):
        current_datetime = datetime.now()
        current_date = current_datetime.strftime("%Y-%m-%d")
        current_hour = current_datetime.strftime("%H")  # Extracting only the hour part
        current_time = current_datetime.strftime("%H:%M:%S")

        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Test@123",
                database="face_recognizer"
            )
            mycursor = mydb.cursor()

            for subject in ["attendance", "AIML", "CN"]:
                if subject == "attendance":
                    table_name = "attendance"
                    csv_filename = "attendance.csv"
                else:
                    table_name = f"{subject.lower()}_attendance"  # Adjust table name based on subject
                    csv_filename = f"{subject.lower()}_attendance.csv"

                last_marked_time = self.last_marked_time.get((student_id, subject))
                if last_marked_time and last_marked_time == current_hour:
                    print(f"Attendance already marked for {subject} for this student in this hour")
                    continue

                # Check attendance in the respective subject's table
                sql_check = f"SELECT * FROM {table_name} WHERE student_id = %s AND date = %s AND HOUR(time) = %s"
                val_check = (student_id, current_date, current_hour)
                mycursor.execute(sql_check, val_check)
                result_check = mycursor.fetchall()

                if result_check:
                    print(f"Attendance already marked for {subject} for this student in this hour")
                    continue

                # Insert attendance record into the database for the determined subject
                sql_insert_subject = f"INSERT INTO {table_name} (student_id, name, department, date, time, status) VALUES (%s, %s, %s, %s, %s, %s)"
                val_insert_subject = (student_id, name, department, current_date, current_time, "Present")
                mycursor.execute(sql_insert_subject, val_insert_subject)
                mydb.commit()

                # Write to CSV file for the determined subject
                with open(csv_filename, "a", newline="\n") as f:
                    writer = csv.writer(f)
                    writer.writerow([student_id, name, department, current_time, current_date, "Present"])

                print(f"Attendance added successfully for {subject}")

                # Update last marked time for the student and subject
                self.last_marked_time[(student_id, subject)] = current_hour

        except mysql.connector.Error as err:
            print("MySQL Error:", err)
        except Exception as e:
            print("Error adding attendance:", e)
        finally:
            if 'mycursor' in locals():
                mycursor.close()
            if 'mydb' in locals():
                mydb.close()

#================================face recodnize===============================
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbour, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbour)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="Test@123", database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute("select Name from student where Student_id=" + str(id))
                n = my_cursor.fetchone()

                if n is not None:
                    n = "+".join(map(str, n))  # Convert to a string if iterable
                else:
                    n = "Unknown"

                my_cursor.execute("select Student_id from student where Student_id=" + str(id))
                i = my_cursor.fetchone()
                i = "+".join(map(str, i)) if i is not None else "Unknown"

                my_cursor.execute("select Dep from student where Student_id=" + str(id))
                d = my_cursor.fetchone()
                d = "+".join(map(str, d)) if d is not None else "Unknown"

                if confidence > 75:
                    cv2.putText(img, f"ID:{i}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 3)
                    cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 3)
                    cv2.putText(img, f"Department:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 3)
                    self.mark_attendance(i, n, d)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 3)

                coord = [x, y, w, h]
            return coord


        def recognize(img, classifier, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to face Recognition", img)

            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
