from tkinter import *
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="dreamhomefinal"
)

def insert_owner():
    owner_no = owner_no_entry.get()
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    address = address_entry.get()
    tel_no = tel_no_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    mycursor = mydb.cursor()
    sql = "INSERT INTO privateowner (ownerNo, fName, lName, address, telNo, email, password) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (owner_no, first_name, last_name, address, tel_no, email, password)
    mycursor.execute(sql, val)
    mydb.commit()
    success_label.config(text="Record inserted successfully.")
    print(mycursor.rowcount, "record inserted.")

root = Tk()
root.title("Insert into Private Owner Table")
root.geometry("500x500")

# Create header label
header_label = Label(root, text="Insert into Private Owner Table", font=("Arial", 18))
header_label.pack(pady=20)

# Create form
form_frame = Frame(root, padx=20, pady=10)
form_frame.pack()

owner_no_label = Label(form_frame, text="Owner Number", font=("Arial", 14))
owner_no_label.grid(row=0, column=0, padx=10, pady=10)

owner_no_entry = Entry(form_frame, font=("Arial", 14))
owner_no_entry.grid(row=0, column=1, padx=10, pady=10)

first_name_label = Label(form_frame, text="First Name", font=("Arial", 14))
first_name_label.grid(row=1, column=0, padx=10, pady=10)

first_name_entry = Entry(form_frame, font=("Arial", 14))
first_name_entry.grid(row=1, column=1, padx=10, pady=10)

last_name_label = Label(form_frame, text="Last Name", font=("Arial", 14))
last_name_label.grid(row=2, column=0, padx=10, pady=10)

last_name_entry = Entry(form_frame, font=("Arial", 14))
last_name_entry.grid(row=2, column=1, padx=10, pady=10)

address_label = Label(form_frame, text="Address", font=("Arial", 14))
address_label.grid(row=3, column=0, padx=10, pady=10)

address_entry = Entry(form_frame, font=("Arial", 14))
address_entry.grid(row=3, column=1, padx=10, pady=10)

tel_no_label = Label(form_frame, text="Telephone Number", font=("Arial", 14))
tel_no_label.grid(row=4, column=0, padx=10, pady=10)

tel_no_entry = Entry(form_frame, font=("Arial", 14))
tel_no_entry.grid(row=4, column=1, padx=10, pady=10)

email_label = Label(form_frame, text="Email", font=("Arial", 14))
email_label.grid(row=5, column=0, padx=10, pady=10)

email_entry = Entry(form_frame, font=("Arial", 14))
email_entry.grid(row=5, column=1, padx=10, pady=10)
# Create password label
password_label = Label(form_frame, text="Password", font=("Arial", 14))
password_label.grid(row=6, column=0, padx=10, pady=10)

password_entry = Entry(form_frame, show="*", font=("Arial", 14))
password_entry.grid(row=6, column=1, padx=10, pady=10)

submit_button = Button(root, text="Submit", command=insert_owner, bg="#4CAF50", fg="white", font=("Arial", 16), pady=10, padx=20)
submit_button.pack(side="bottom", pady=20)

# Create success label
success_label = Label(root, fg="#4CAF50", font=("Arial", 14))
success_label.pack()

root.mainloop()

