import os
import pickle
from time import strftime
from datetime import datetime
from tkinter import Tk, Label, Entry, Button, Frame, messagebox
from PIL import Image, ImageTk
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from email.mime.text import MIMEText
from base64 import urlsafe_b64encode

# Define the scopes required for the Gmail API
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Student Management System")

        # Place the base image
        self.img_top = Image.open("C:/Users/Yugant/OneDrive/Desktop/mini project/colleges_images/help desk1_cleanup.jpg")  # Change to your image file path
        self.img_top = self.img_top.resize((1150, 700), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(self.img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=400, y=55, width=1150, height=700)

        dev_label1 = Label(self.root, text="Developer Email", font=("times new roman", 28, "bold"), bg="white", fg="black")
        dev_label1.place(x=715, y=300) 

        dev_label1 = Label(self.root, text="Email: 2AG21CS126@gmail.com", font=("times new roman", 28, "bold"), bg="white", fg="black")
        dev_label1.place(x=715, y=350)  # Adjust the coordinates as needed

        # Add title label
        title_lbl = Label(self.root, text="HELP DESK", font=("times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1550, height=60)


        #=========time=================
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
        day_of_week_label = Label(root, font=("times new roman", 16, "bold"), background="white", foreground="blue")
        day_of_week_label.place(x=320,y=10,width=200,height=40)

        # Call the update_day_of_week function to start displaying the day of the week
        update_day_of_week()

        # Add a frame for entry labels
        self.entry_frame = Frame(self.root, bg="white", bd=2, relief="ridge")
        self.entry_frame.place(x=10, y=100, width=370, height=200)

        # Add labels and entry widgets for email and issue details
        email_label = Label(self.entry_frame, text="Your Email:", font=("times new roman", 16), bg="white", fg="black")
        email_label.place(x=10, y=10)
        self.email_entry = Entry(self.entry_frame, font=("times new roman", 14), bg="white", fg="black")
        self.email_entry.place(x=120, y=10, width=220)

        issue_label = Label(self.entry_frame, text="Issue Details:", font=("times new roman", 16), bg="white", fg="black")
        issue_label.place(x=10, y=50)
        self.issue_entry = Entry(self.entry_frame, font=("times new roman", 14), bg="white", fg="black")
        self.issue_entry.place(x=120, y=50, width=220,height=100)

        # Add a submit button
        submit_btn = Button(self.entry_frame, text="Submit", font=("times new roman", 14, "bold"), bg="blue", fg="white", command=self.send_email)
        submit_btn.place(x=40, y=100)

    def authenticate(self):
        """
        Authenticate with OAuth2 and obtain credentials.
        """
        creds = None

        # The file token.pickle stores the user's access and refresh tokens
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)

        # If there are no (valid) credentials available, let the user log in
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)

            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        return creds

    def create_message(self, sender, to, subject, message_text):
        """
        Create a message for an email.
        """
        message = MIMEText(message_text)
        message['to'] = to
        message['from'] = sender
        message['subject'] = subject
        raw_message = urlsafe_b64encode(message.as_bytes())
        return {'raw': raw_message.decode()}

    def send_email(self):
        """
        Send an email message.
        """
        try:
            # Authenticate and obtain credentials
            creds = self.authenticate()

            # Build the Gmail service
            service = build('gmail', 'v1', credentials=creds)

            # Create a message
            sender = self.email_entry.get()
            to = '2ag21cs126@gmail.com'  # Replace with the recipient's email address
            subject = 'Issue Report from face recognition attendance System'
            message_text = self.issue_entry.get()
            message = self.create_message(sender, to, subject, message_text)

            # Send the email
            send_email(service, 'me', message)
            messagebox.showinfo("Success", "Email sent successfully!",parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send email.\nError: {str(e)}")

def send_email(service, user_id, message):
    """
    Send an email message.
    """
    try:
        message = (service.users().messages().send(userId=user_id, body=message)
                   .execute())
        print('Message Id: %s' % message['id'])
    except Exception as e:
        print('An error occurred: %s' % e)

if __name__ == '__main__':
    root = Tk()
    obj = Help(root)
    root.mainloop()
