#clientregistration
from tkinter import *
import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="1234",
  database="dreamhomefinal"
)

def insert_property():
    clientNo =clientNo_entry.get()
    fName = fName_entry.get()
    branchNo = branchNo_entry.get()
    baddress = baddress_entry.get()
    regBy = regBy_entry.get()
    regDate = regDate_entry.get()
    type = type_entry.get()
    maxRent = maxRent_entry.get()


    mycursor = mydb.cursor()
    sql = "INSERT INTO clientregistration (clientNo, fName, branchNo, baddress, regBy , regDate, type, maxRent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (clientNo, fName, branchNo, baddress, regBy , regDate, type, maxRent)
    mycursor.execute(sql, val)
    mydb.commit()
    success_label.config(text="Record inserted successfully.")
    print(mycursor.rowcount, "record inserted.")

root = Tk()
root.title("Insert into clientregistration Table")
root.geometry("500x600")

# Create header label
header_label = Label(root, text="Insert into clientregistration Table", font=("Arial", 18))
header_label.pack(pady=20)

# Create form
form_frame = Frame(root, padx=20, pady=10)
form_frame.pack()

clientNo_label = Label(form_frame, text="clientNo", font=("Arial", 14))
clientNo_label.grid(row=0, column=0, padx=10, pady=10)

clientNo_entry = Entry(form_frame, font=("Arial", 14))
clientNo_entry.grid(row=0, column=1, padx=10, pady=10)

fName_label = Label(form_frame, text="fName", font=("Arial", 14))
fName_label.grid(row=1, column=0, padx=10, pady=10)

fName_entry = Entry(form_frame, font=("Arial", 14))
fName_entry.grid(row=1, column=1, padx=10, pady=10)

branchNo_label = Label(form_frame, text="branchNo", font=("Arial", 14))
branchNo_label.grid(row=2, column=0, padx=10, pady=10)

branchNo_entry = Entry(form_frame, font=("Arial", 14))
branchNo_entry.grid(row=2, column=1, padx=10, pady=10)

baddress_label = Label(form_frame, text="baddress", font=("Arial", 14))
baddress_label.grid(row=3, column=0, padx=10, pady=10)

baddress_entry = Entry(form_frame, font=("Arial", 14))
baddress_entry.grid(row=3, column=1, padx=10, pady=10)

regBy_label = Label(form_frame, text="regBy", font=("Arial", 14))
regBy_label.grid(row=4, column=0, padx=10, pady=10)

regBy_entry = Entry(form_frame, font=("Arial", 14))
regBy_entry.grid(row=4, column=1, padx=10, pady=10)

regDate_label = Label(form_frame, text="regDate", font=("Arial", 14))
regDate_label.grid(row=5, column=0, padx=10, pady=10)

regDate_entry = Entry(form_frame, font=("Arial", 14))
regDate_entry.grid(row=5, column=1, padx=10, pady=10)

type_label = Label(form_frame, text="type", font=("Arial", 14))
type_label.grid(row=6, column=0, padx=10, pady=10)

type_entry = Entry(form_frame, font=("Arial", 14))
type_entry.grid(row=6, column=1, padx=10, pady=10)

maxRent_label = Label(form_frame, text="maxRent", font=("Arial", 14))
maxRent_label.grid(row=7, column=0, padx=10, pady=10)

maxRent_entry = Entry(form_frame, font=("Arial", 14))
maxRent_entry.grid(row=7, column=1, padx=10, pady=10)


submit_button = Button(root, text="Submit", command=insert_property, bg="#4CAF50", fg="white", font=("Arial", 16), pady=10, padx=20)
submit_button.pack(pady=20)

success_label = Label(root, fg="#4CAF50", font=("Arial", 14))
success_label.pack()


root.mainloop()