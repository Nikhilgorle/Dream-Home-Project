from tkinter import *
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="dreamhomefinal"
)

def insert_comment():
    clientNo = clientNo_entry.get()
    propertyNo = propertyNo_entry.get()
    viewdate = viewdate_entry.get()
    comment = comment_entry.get()

    mycursor = mydb.cursor()
    sql = "INSERT INTO viewing (clientNo, propertyNo, viewdate, comment) VALUES (%s, %s, %s, %s)"
    val = (clientNo, propertyNo, viewdate, comment)
    mycursor.execute(sql, val)
    mydb.commit()

    clientNo_entry.delete(0,END)
    propertyNo_entry.delete(0,END)
    viewdate_entry.delete(0,END)
    comment_entry.delete(0,END)

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

clientNo_label = Label(form_frame, text="Client Number", font=("Arial", 14),bg = "#a8defb",fg = "black")
clientNo_label.grid(row=0, column=0, padx=10, pady=10)

clientNo_entry = Entry(form_frame, font=("Arial", 14))
clientNo_entry.grid(row=0, column=1, padx=10, pady=10)

propertyNo_label = Label(form_frame, text="Property Number", font=("Arial", 14),bg = "#a8defb",fg = "black")
propertyNo_label.grid(row=1, column=0, padx=10, pady=10)

propertyNo_entry = Entry(form_frame, font=("Arial", 14))
propertyNo_entry.grid(row=1, column=1, padx=10, pady=10)

viewdate_label = Label(form_frame, text="Date viewed", font=("Arial", 14),bg = "#a8defb",fg = "black")
viewdate_label.grid(row=2, column=0, padx=10, pady=10)

viewdate_entry = Entry(form_frame, font=("Arial", 14))
viewdate_entry.grid(row=2, column=1, padx=10, pady=10)

comment_label = Label(form_frame, text="Comments", font=("Arial", 14),bg = "#a8defb",fg = "black")
comment_label.grid(row=3, column=0, padx=10, pady=10)

comment_entry = Entry(form_frame, font=("Arial", 14))
comment_entry.grid(row=3, column=1, padx=10, pady=10)

submit_button = Button(root, text="Submit", command=insert_comment, bg="green", fg="black", font=("Arial", 16), pady=10, padx=20)
submit_button.pack(pady=20)

success_label = Label(root, fg="#4CAF50", font=("Arial", 14),bg = "#a8defb")
success_label.pack()

root.mainloop()