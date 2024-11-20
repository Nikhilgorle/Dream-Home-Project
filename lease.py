from tkinter import *
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sriram_008",
    database="dreamhomefinal"
)

def insert_lease():
    lease_id = lease_id_entry.get()
    client_no = client_no_entry.get()
    rent = rent_entry.get()
    deposit = deposit_entry.get()
    payment_method = payment_method_entry.get()
    property_no = property_no_entry.get()
    rent_start_dt = rent_start_dt_entry.get()
    rent_end_dt = rent_end_dt_entry.get()
    duration = duration_entry.get()

    mycursor = mydb.cursor()
    sql = "INSERT INTO lease (leaseId, clientNo, Rent, Deposit, paymentmethod, propertyNo, rentStartDt, rentEndDt, DurationInYears) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (lease_id, client_no, rent, deposit, payment_method, property_no, rent_start_dt, rent_end_dt, duration)
    mycursor.execute(sql, val)
    mydb.commit()
    success_label.config(text="Record inserted successfully.")
    print(mycursor.rowcount, "record inserted.")

root = Tk()
root.configure(bg = "#a8defb")
root.title("Insert into Lease Table")
root.geometry("700x700")

# Create header label
header_label = Label(root, text="Insert into Lease Table", font=("Arial", 18),bg = "#a8defb",fg = "black")
header_label.pack(pady=20)

# Create form
form_frame = Frame(root, padx=20, pady=10,bg = "#a8defb")
form_frame.pack()

lease_id_label = Label(form_frame, text="Lease ID", font=("Arial", 14),bg = "#a8defb",fg = "black")
lease_id_label.grid(row=0, column=0, padx=10, pady=10)

lease_id_entry = Entry(form_frame, font=("Arial", 14))
lease_id_entry.grid(row=0, column=1, padx=10, pady=10)

client_no_label = Label(form_frame, text="Client Number", font=("Arial", 14),bg = "#a8defb",fg = "black")
client_no_label.grid(row=1, column=0, padx=10, pady=10)

client_no_entry = Entry(form_frame, font=("Arial", 14))
client_no_entry.grid(row=1, column=1, padx=10, pady=10)

rent_label = Label(form_frame, text="Rent", font=("Arial", 14),bg = "#a8defb",fg = "black")
rent_label.grid(row=2, column=0, padx=10, pady=10)

rent_entry = Entry(form_frame, font=("Arial", 14))
rent_entry.grid(row=2, column=1, padx=10, pady=10)

deposit_label = Label(form_frame, text="Deposit", font=("Arial", 14),bg = "#a8defb",fg = "black")
deposit_label.grid(row=3, column=0, padx=10, pady=10)

deposit_entry = Entry(form_frame, font=("Arial", 14))
deposit_entry.grid(row=3, column=1, padx=10, pady=10)

payment_method_label = Label(form_frame, text="Payment Method", font=("Arial", 14),bg = "#a8defb",fg = "black")
payment_method_label.grid(row=4, column=0, padx=10, pady=10)

payment_method_entry = Entry(form_frame, font=("Arial", 14))
payment_method_entry.grid(row=4, column=1, padx=10, pady=10)

property_no_label = Label(form_frame, text="Property Number", font=("Arial", 14),bg = "#a8defb",fg = "black")
property_no_label.grid(row=5, column=0, padx=10, pady=10)

property_no_entry = Entry(form_frame, font=("Arial", 14))
property_no_entry.grid(row=5, column=1, padx=10, pady=10)

rent_start_dt_label = Label(form_frame, text="Rent Start Date (YYYY-MM-DD)", font=("Arial", 14),bg = "#a8defb",fg = "black")
rent_start_dt_label.grid(row=6, column=0, padx=10, pady=10)

rent_start_dt_entry = Entry(form_frame, font=("Arial", 14))
rent_start_dt_entry.grid(row=6, column=1, padx=10, pady=10)

rent_end_dt_label = Label(form_frame, text="Rent End Date (YYYY-MM-DD)", font=("Arial", 14),bg = "#a8defb",fg = "black")
rent_end_dt_label.grid(row=7, column=0, padx=10, pady=10)

rent_end_dt_entry = Entry(form_frame, font=("Arial", 14))
rent_end_dt_entry.grid(row=7, column=1, padx=10, pady=10)

duration_label = Label(form_frame, text="Duration in Years", font=("Arial", 14),bg = "#a8defb",fg = "black")
duration_label.grid(row=8, column=0, padx=10, pady=10)

duration_entry = Entry(form_frame, font=("Arial", 14))
duration_entry.grid(row=8, column=1, padx=10, pady=10)

#Create button to submit form
submit_button = Button(root, text="Insert Record", font=("Arial", 14), command=insert_lease,bg = "green",fg = "black")
submit_button.pack(pady=20)

#Create label for success message
success_label = Label(root, font=("Arial", 14),bg = "#a8defb",fg = "black")
success_label.pack(pady=20)

root.mainloop()