from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from main import FaceRecognitionSystem
from time import strftime

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1920x1080+0+0")

        # Load the image
        self.bg_image = Image.open(r"C:\Users\Yugant\OneDrive\Desktop\mini project\colleges_images\BestFacialRecognition_cleanup.jpg")
        self.bg_image = self.bg_image.resize((1540, 850), Image.LANCZOS)  # Resize the image

        self.bg = ImageTk.PhotoImage(self.bg_image)
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)
        
        frame = Frame(self.root, bg="black", bd=5, relief=SUNKEN,highlightbackground="white")
        frame.place(x=50, y=170, width=340, height=450)

        img1=Image.open(r"colleges_images\username.jpg")
        img1.resize((100,100),Image.LANCZOS)
        self.Photoimage1=ImageTk.PhotoImage(img1)

        lblimg1=Label(image=self.Photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=180,y=180,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        

#labels
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)
        


        #==============icon images============================
        img2=Image.open(r"C:\Users\Yugant\OneDrive\Desktop\mini project\colleges_images\user.png")
        img2.resize((25,25),Image.LANCZOS)
        self.Photoimage2=ImageTk.PhotoImage(img2)

        lblimg2=Label(image=self.Photoimage2,bg="black",borderwidth=0)
        lblimg2.place(x=95,y=323,width=25,height=25)

        img3=Image.open(r"C:\Users\Yugant\OneDrive\Desktop\mini project\colleges_images\password.png")
        img3.resize((25,25),Image.LANCZOS)
        self.Photoimage3=ImageTk.PhotoImage(img3)

        lblimg3=Label(image=self.Photoimage3,bg="black",borderwidth=0)
        lblimg3.place(x=95,y=393,width=25,height=25)
#login button
        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)
#register button
        registerbtn=Button(frame,text=" New User Register",command=self.register_window,font=("times new roman",10,"bold"),border=0,fg="white",bg="black",activebackground="black")
        registerbtn.place(x=10,y=350,width=170)
#forgot password
        forgetpassbtn=Button(frame,text="Forgot Password",command=self.forgot_password_window,font=("times new roman",10,"bold"),border=0,fg="white",bg="black",activebackground="black")
        forgetpassbtn.place(x=10,y=370,width=160,)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields required")
        elif self.txtuser.get() == "" and self.txtpass.get() == "":
            messagebox.showinfo("Success", "Welcome to the project")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Test@123", database="mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from users where email=%s and user_password=%s", (
                                                                                          self.txtuser.get(),
                                                                                          self.txtpass.get()
                                                                                             ))
            row = my_cursor.fetchone()
            if row is None:
               messagebox.showerror("Error", "Invalid username and password")
            else:
                open_main = messagebox.askyesno("YesNo", "Access only Admin")
                if open_main > 0:
                    self.new_window = Toplevel(self.root)
                    self.app = FaceRecognitionSystem(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

#==================================reset password===================================
    def reset_pass(self, security_q_entry):
        if security_q_entry.get() == "Select":
            messagebox.showerror("Error", "Select the security question")
        elif self.security_a_entry.get() == "":
            messagebox.showerror("Error", "Please enter the answer")
        elif self.txt_newpass.get() == "":
            messagebox.showerror("Error", "Please enter the new password")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Test@123", database="mydata")
            my_cursor = conn.cursor()

            query = "SELECT * FROM users WHERE email=%s AND security_question=%s AND security_answer=%s"
            value = (self.txtuser.get(), security_q_entry.get(), self.security_a_entry.get())
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row is None:
                messagebox.showerror("Error", "Please enter the correct answer")
            else:
                update_query = "UPDATE users SET user_password=%s WHERE email=%s"
                update_value = (self.txt_newpass.get(), self.txtuser.get())
                my_cursor.execute(update_query, update_value)

                conn.commit()
                conn.close()

                messagebox.showinfo("Password Reset", "Password has been reset successfully!",parent=self.root2)
                self.root2.destroy()  # Close the password reset window

    def forgot_password_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Please enter the email to reset password")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Test@123", database="mydata")
            my_cursor = conn.cursor()
            query = ("select * from users where email=%s")
            value = (self.txtuser.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row == None:
                messagebox.showerror("Error", "please enter the valid email")
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                l = Label(self.root2, text="Forgot Password", font=("times new roman", 20, "bold"), fg="red", bg="white")
                l.place(x=0, y=10, relwidth=1)

                # Select Security Question label and entry
                security_q_label = Label(self.root2, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white")
                security_q_label.place(x=50, y=80)

                security_q_entry = ttk.Combobox(self.root2, font=("times new roman", 15, "bold"), state="readonly")
                security_q_entry['values'] = (
                "Select", "What is your pet's name?", "What is your favorite color?", "What is the name of your school?")
                security_q_entry.place(x=50, y=110, width=250)
                security_q_entry.current(0)  # set the default value to "Select"

                # Security Answer label and entry
                security_a_label = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="white")
                security_a_label.place(x=50, y=150)

                self.security_a_entry = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
                self.security_a_entry.place(x=50, y=180, width=250)

                # new password
                new_password = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="white")
                new_password.place(x=50, y=220)

                self.txt_newpass = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
                self.txt_newpass.place(x=50, y=250, width=250)

                reset_btn = Button(self.root2, text="Reset Password", command=lambda: self.reset_pass(security_q_entry),
                                   font=("times new roman", 15, "bold"), fg="white", bg="green")
                reset_btn.place(x=50, y=300, width=250)


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1920x1080+0+0")

        # Simplified variable names
        self.first_name = StringVar()
        self.last_name = StringVar()
        self.phone_number = StringVar()
        self.email = StringVar()
        self.security_question = StringVar()
        self.security_answer = StringVar()
        self.user_password = StringVar()
        self.confirm_password = StringVar()
        self.terms_check = IntVar()

        # ======================bg image=====================
        img = Image.open(r"C:\Users\Yugant\OneDrive\Desktop\mini project\colleges_images\pastel-blue-solid-4dyj0r7fve79rb9s.png")  # Update with your image path
        img = img.resize((1920, 1080), Image.LANCZOS)  # Adjusted dimensions
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=1920, height=1080)

        # =====================left image=====================
        img1 = Image.open(r"C:\Users\Yugant\OneDrive\Desktop\mini project\colleges_images\view-3d-businessman_23-2150709814.jpg")  # Update with your image path
        self.bg1 = ImageTk.PhotoImage(img1)
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=180, y=150, width=460, height=550)

        # main frame
        main_frame = Frame(self.root, bd=2, bg="white")
        main_frame.place(x=640, y=150, width=800, height=550)

        # register label
        register_lbl = Label(main_frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="green", bg="white")
        register_lbl.place(x=20, y=20)

        # First Name label and entry
        fname_label = Label(main_frame, text="First Name", font=("times new roman", 15, "bold"), bg="white")
        fname_label.place(x=50, y=100)

        fname_entry = ttk.Entry(main_frame, textvariable=self.first_name, font=("times new roman", 15, "bold"))
        fname_entry.place(x=50, y=130, width=250)

        # Last Name label and entry
        lname_label = Label(main_frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white")
        lname_label.place(x=370, y=100)

        lname_entry = ttk.Entry(main_frame, textvariable=self.last_name, font=("times new roman", 15, "bold"))
        lname_entry.place(x=370, y=130, width=250)

        # Phone Number label and entry
        phone_label = Label(main_frame, text="Phone Number", font=("times new roman", 15, "bold"), bg="white")
        phone_label.place(x=50, y=170)

        phone_entry = ttk.Entry(main_frame, textvariable=self.phone_number, font=("times new roman", 15, "bold"))
        phone_entry.place(x=50, y=200, width=250)

        # Email label and entry
        email_label = Label(main_frame, text="Email", font=("times new roman", 15, "bold"), bg="white")
        email_label.place(x=370, y=170)

        email_entry = ttk.Entry(main_frame, textvariable=self.email, font=("times new roman", 15, "bold"))
        email_entry.place(x=370, y=200, width=250)

        # Select Security Question label and entry
        security_q_label = Label(main_frame, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white")
        security_q_label.place(x=50, y=240)

        security_q_entry = ttk.Combobox(main_frame, textvariable=self.security_question, font=("times new roman", 15, "bold"), state="readonly")
        security_q_entry['values'] = ("Select", "What is your pet's name?", "What is your favorite color?", "What is the name of your school?")
        security_q_entry.place(x=50, y=270, width=250)
        security_q_entry.current(0)  # set the default value to "Select"

        # Security Answer label and entry
        security_a_label = Label(main_frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white")
        security_a_label.place(x=370, y=240)

        security_a_entry = ttk.Entry(main_frame, textvariable=self.security_answer, font=("times new roman", 15, "bold"))
        security_a_entry.place(x=370, y=270, width=250)

        # Password label and entry
        password_label = Label(main_frame, text="Password", font=("times new roman", 15, "bold"), bg="white")
        password_label.place(x=50, y=310)

        password_entry = ttk.Entry(main_frame, textvariable=self.user_password, font=("times new roman", 15, "bold"), show="*")
        password_entry.place(x=50, y=340, width=250)

        # Confirm Password label and entry
        confirm_password_label = Label(main_frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white")
        confirm_password_label.place(x=370, y=310)

        confirm_password_entry = ttk.Entry(main_frame, textvariable=self.confirm_password, font=("times new roman", 15, "bold"), show="*")
        confirm_password_entry.place(x=370, y=340, width=250)

        # Checkbutton for Terms and Conditions
        terms_check = Checkbutton(main_frame, text="I agree to the Terms and Conditions", variable=self.terms_check, font=("times new roman", 12, "bold"), onvalue=1, offvalue=0, bg="white")
        terms_check.place(x=50, y=380)

        # Register Button
        register_btn = Button(main_frame, text="REGISTER", command=self.register_user, font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="green")
        register_btn.place(x=50, y=420, width=250)

        # Login Now Button
        login_now_btn = Button(main_frame, text="LOGIN NOW", command=self.login_now, font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="blue")
        login_now_btn.place(x=370, y=420, width=250)

        try:
            # Your MySQL connection configuration
            self.db_connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Test@123",
                database="mydata"
            )

            # Create a cursor object to interact with the database
            self.db_cursor = self.db_connection.cursor()

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            messagebox.showerror("Error", f"Error connecting to the database: {str(err)}")

    def register_user(self):
        if not self.first_name.get() or not self.last_name.get() or not self.phone_number.get() or not self.email.get() or not self.security_question.get() or not self.security_answer.get() or not self.user_password.get() or not self.confirm_password.get():
            messagebox.showerror("Error", "All fields are required.",parent=self.root)
            return

        if self.user_password.get() != self.confirm_password.get():
            messagebox.showerror("Error", "Passwords do not match.",parent=self.root)
            return

        if not self.terms_check.get():
            messagebox.showerror("Error", "Please agree to the Terms and Conditions.",parent=self.root)
            return

        try:
            # Check if the email is already registered
            email_check_query = "SELECT * FROM users WHERE email = %s"
            email_check_data = (self.email.get(),)
            self.db_cursor.execute(email_check_query, email_check_data)
            existing_user = self.db_cursor.fetchone()

            if existing_user:
                messagebox.showinfo("Registration", "User with this email has already registered.")
                return

            # Insert user data into the database
            insert_query = "INSERT INTO users (first_name, last_name, phone_number, email, security_question, security_answer, user_password) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            insert_data = (self.first_name.get(), self.last_name.get(), self.phone_number.get(), self.email.get(), self.security_question.get(), self.security_answer.get(), self.user_password.get())

            self.db_cursor.execute(insert_query, insert_data)
            self.db_connection.commit()

            messagebox.showinfo("Registration", "User Registered Successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Registration failed: {str(e)}")

    def login_now(self):
        messagebox.showinfo("Login", "Redirecting to Login Page...")

if __name__ == "__main__":
    main()