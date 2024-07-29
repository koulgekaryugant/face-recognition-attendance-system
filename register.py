from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

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
        img = Image.open(r"C:\Users\Yugant\OneDrive\Desktop\mini project\colleges_images\images.jpg")  # Update with your image path
        img = img.resize((1920, 1080), Image.LANCZOS)  # Adjusted dimensions
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=1920, height=1080)

        # =====================left image=====================
        img1 = Image.open(r"C:\Users\Yugant\OneDrive\Desktop\mini project\colleges_images\developer.png")  # Update with your image path
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
            messagebox.showerror("Error", "All fields are required.")
            return

        if self.user_password.get() != self.confirm_password.get():
            messagebox.showerror("Error", "Passwords do not match.")
            return

        if not self.terms_check.get():
            messagebox.showerror("Error", "Please agree to the Terms and Conditions.")
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
    root = Tk()
    app = Register(root)
    root.mainloop()
