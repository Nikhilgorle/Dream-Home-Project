from tkinter import *
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password= "1234",
  database="dreamhomefinal"
)

def insert_staff():
    staffNo = staffNo_entry.get()
    fName = fName_entry.get()
    position = position_entry.get()
    sex = sex_entry.get()
    telephone = telephone_entry.get()
    Dob = Dob_entry.get()
    salary = salary_entry.get()
    branchNo = branchNo_entry.get()

    mycursor = mydb.cursor()
    sql = "INSERT INTO staff(staffNo,fName,position,sex,telephone,DOB,salary,branchNo) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (staffNo,fName,position,sex,telephone,Dob,salary,branchNo)
    mycursor.execute(sql, val)
    mydb.commit()
    
    staffNo_entry.delete(0,END)
    fName_entry.delete(0,END)
    position_entry.delete(0,END)
    sex_entry.delete(0,END)
    telephone_entry.delete(0,END)
    Dob_entry.delete(0,END)
    salary_entry.delete(0,END)
    branchNo_entry.delete(0,END)

    success_label.config(text="Record inserted successfully.")
    print(mycursor.rowcount, "record inserted.")

root = Tk()
root.configure(bg= "#a8defb")
root.title("Staff details")
root.geometry("700x700")

# Create header label
header_label = Label(root, text="Enter staff details", font=("Arial", 18),bg = "#a8defb",fg = "black")
header_label.pack(pady=20)

# Create form
form_frame = Frame(root, padx=20, pady=10,bg = "#a8defb")
form_frame.pack()

staffNo_label = Label(form_frame, text="Staff Number", font=("Arial", 14),bg = "#a8defb",fg = "black")
staffNo_label.grid(row=0, column=0, padx=10, pady=10)

staffNo_entry = Entry(form_frame, font=("Arial", 14))
staffNo_entry.grid(row=0, column=1, padx=10, pady=10)

fName_label = Label(form_frame, text="Name", font=("Arial", 14),bg = "#a8defb",fg = "black")
fName_label.grid(row=1, column=0, padx=10, pady=10)

fName_entry = Entry(form_frame, font=("Arial", 14))
fName_entry.grid(row=1, column=1, padx=10, pady=10)

position_label = Label(form_frame, text="Position", font=("Arial", 14),bg = "#a8defb",fg = "black")
position_label.grid(row=2, column=0, padx=10, pady=10)

position_entry = Entry(form_frame, font=("Arial", 14))
position_entry.grid(row=2, column=1, padx=10, pady=10)

sex_label = Label(form_frame, text="Sex", font=("Arial", 14),bg = "#a8defb",fg = "black")
sex_label.grid(row=3, column=0, padx=10, pady=10)

sex_entry = Entry(form_frame, font=("Arial", 14))
sex_entry.grid(row=3, column=1, padx=10, pady=10)

telephone_label = Label(form_frame, text="Telephone", font=("Arial", 14),bg = "#a8defb",fg = "black")
telephone_label.grid(row=4, column=0, padx=10, pady=10)

telephone_entry = Entry(form_frame, font=("Arial", 14))
telephone_entry.grid(row=4, column=1, padx=10, pady=10)

Dob_label = Label(form_frame, text="Date of Birth", font=("Arial", 14),bg = "#a8defb",fg = "black")
Dob_label.grid(row=5, column=0, padx=10, pady=1)
Dob_entry = Entry(form_frame, font=("Arial", 14))
Dob_entry.grid(row=5, column=1, padx=10, pady=10)

salary_label = Label(form_frame, text="Salary", font=("Arial", 14),bg = "#a8defb",fg = "black")
salary_label.grid(row=6, column=0, padx=10, pady=1)
salary_entry = Entry(form_frame, font=("Arial", 14))
salary_entry.grid(row=6, column=1, padx=10, pady=10)

branchNo_label = Label(form_frame, text="Branch number", font=("Arial", 14),bg = "#a8defb",fg = "black")
branchNo_label.grid(row=7, column=0, padx=10, pady=1)
branchNo_entry = Entry(form_frame, font=("Arial", 14))
branchNo_entry.grid(row=7, column=1, padx=10, pady=10)

submit_button = Button(root, text="Submit", command=insert_staff, bg="#4CAF50", fg="black", font=("Arial", 16), pady=10, padx=20)
submit_button.pack(pady=20)

# Create success label
success_label = Label(root, fg="black", font=("Arial", 14),bg = "#a8defb")
success_label.pack()


root.mainloop()
