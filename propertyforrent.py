from tkinter import *
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="dreamhomefinal"
)

def insert_property():
    propertyNo = propertyNo_entry.get()
    street = street_entry.get()
    city = city_entry.get()
    postcode = postcode_entry.get()
    type = type_entry.get()
    rooms = rooms_entry.get()
    rent = rent_entry.get()
    ownerNo = ownerNo_entry.get()
    staffNo = staffNo_entry.get()
    branchNo = branchNo_entry.get()

    mycursor = mydb.cursor()
    sql = "INSERT INTO propertyforrent (propertyNo, street, city, postcode, type, rooms, rent, ownerNo, staffNo, branchNo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (propertyNo, street, city, postcode, type, rooms, rent, ownerNo, staffNo, branchNo)
    mycursor.execute(sql, val)
    mydb.commit()
    success_label.config(text="Record inserted successfully.")
    print(mycursor.rowcount, "record inserted.")

root = Tk()
root.configure(bg = "#a8defb")
root.title("Property renting details")
root.geometry("700x700")

header_label = Label(root, text="Insert property deatails", font=("Arial", 18),bg = "#a8defb",fg = "black")
header_label.pack(pady=20)

form_frame = Frame(root, padx=20, pady=10,bg = "#a8defb")
form_frame.pack()

propertyNo_label = Label(form_frame, text="Property Number", font=("Arial", 14),bg = "#a8defb",fg = "black")
propertyNo_label.grid(row=0, column=0, padx=10, pady=10)

propertyNo_entry = Entry(form_frame, font=("Arial", 14))
propertyNo_entry.grid(row=0, column=1, padx=10, pady=10)

street_label = Label(form_frame, text="Street", font=("Arial", 14),bg = "#a8defb",fg = "black")
street_label.grid(row=1, column=0, padx=10, pady=10)

street_entry = Entry(form_frame, font=("Arial", 14))
street_entry.grid(row=1, column=1, padx=10, pady=10)

city_label = Label(form_frame, text="City", font=("Arial", 14),bg = "#a8defb",fg = "black")
city_label.grid(row=2, column=0, padx=10, pady=10)

city_entry = Entry(form_frame, font=("Arial", 14))
city_entry.grid(row=2, column=1, padx=10, pady=10)

postcode_label = Label(form_frame, text="Postcode", font=("Arial", 14),bg = "#a8defb",fg = "black")
postcode_label.grid(row=3, column=0, padx=10, pady=10)

postcode_entry = Entry(form_frame, font=("Arial", 14))
postcode_entry.grid(row=3, column=1, padx=10, pady=10)

type_label = Label(form_frame, text="Type", font=("Arial", 14),bg = "#a8defb",fg = "black")
type_label.grid(row=4, column=0, padx=10, pady=10)

type_entry = Entry(form_frame, font=("Arial", 14))
type_entry.grid(row=4, column=1, padx=10, pady=10)

rooms_label = Label(form_frame, text="Rooms", font=("Arial", 14),bg = "#a8defb",fg = "black")
rooms_label.grid(row=5, column=0, padx=10, pady=10)

rooms_entry = Entry(form_frame, font=("Arial", 14))
rooms_entry.grid(row=5, column=1, padx=10, pady=10)

rent_label = Label(form_frame, text="Rent", font=("Arial", 14),bg = "#a8defb",fg = "black")
rent_label.grid(row=6, column=0, padx=10, pady=10)

rent_entry = Entry(form_frame, font=("Arial", 14))
rent_entry.grid(row=6, column=1, padx=10, pady=10)

ownerNo_label = Label(form_frame, text="ownerNo", font=("Arial", 14),bg = "#a8defb",fg = "black")
ownerNo_label.grid(row=7, column=0, padx=10, pady=10)

ownerNo_entry = Entry(form_frame, font=("Arial", 14))
ownerNo_entry.grid(row=7, column=1, padx=10, pady=10)

staffNo_label = Label(form_frame, text="staffNo", font=("Arial", 14),bg = "#a8defb",fg = "black")
staffNo_label.grid(row=8, column=0, padx=10, pady=10)

staffNo_entry = Entry(form_frame, font=("Arial", 14))
staffNo_entry.grid(row=8, column=1, padx=10, pady=10)

branchNo_label = Label(form_frame, text="branchNo", font=("Arial", 14),bg = "#a8defb",fg = "black")
branchNo_label.grid(row=9, column=0, padx=10, pady=10)

branchNo_entry = Entry(form_frame, font=("Arial", 14))
branchNo_entry.grid(row=9, column=1, padx=10, pady=10)

submit_button = Button(root, text="Submit", command=insert_property, bg="green", fg="black", font=("Arial", 16), pady=10, padx=20)
submit_button.pack(pady=20)

success_label = Label(root, fg="#4CAF50", font=("Arial", 14),bg = "#a8defb")
success_label.pack()

root.mainloop()