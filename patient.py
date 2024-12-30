import tkinter as tk
from tkinter import ttk
window = tk.Tk()
window.title("Welcome to Hospital")
window.geometry("5000x4000") 
window.configure(bg='black')
label = tk.Label(window, text="Welcome to the Hospital", font=('Arial', 16), fg="white", bg="black")
label.grid(column=0, row=0, columnspan=3, pady=10)
frame = tk.Frame(window, bg="black")
frame.grid(column=0, row=1, columnspan=3, padx=20, pady=10)
hospital_label = tk.Label(frame, text="Enter Hospital Name:", font=('Arial', 12), fg="white", bg="black")
hospital_label.grid(row=0, column=0, sticky="e", padx=10)
txt = tk.Entry(frame, width=25, font=('Arial', 12), bg="white", fg="black")
txt.grid(row=0, column=1, padx=10)
department_label = tk.Label(frame, text="Select Department:", font=('Arial', 12), fg="white", bg="black")
department_label.grid(row=1, column=0, sticky="e", padx=10)
departments = ['Emergency', 'Radiology', 'Pediatrics', 'Surgery', 'Cardiology']
combo = ttk.Combobox(frame, values=departments, width=20, font=('Arial', 12), state="readonly", 
                      background="black", foreground="white")
combo.grid(row=1, column=1, padx=10)
name_label = tk.Label(frame, text="Enter Your Name:", font=('Arial', 12), fg="white", bg="black")
name_label.grid(row=2, column=0, sticky="e", padx=10)

name_entry = tk.Entry(frame, width=25, font=('Arial', 12), bg="white", fg="black")
name_entry.grid(row=2, column=1, padx=10)
contact_label = tk.Label(frame, text="Enter Contact Info (Phone/Email):", font=('Arial', 12), fg="white", bg="black")
contact_label.grid(row=3, column=0, sticky="e", padx=10)

contact_entry = tk.Entry(frame, width=25, font=('Arial', 12), bg="white", fg="black")
contact_entry.grid(row=3, column=1, padx=10)
status_label = tk.Label(window, text="", font=('Arial', 12), fg="green", bg="black")
status_label.grid(column=0, row=4, columnspan=3, pady=10)
def submit():
    hospital_name = txt.get()  
    department_name = combo.get()  
    user_name = name_entry.get()  
    contact_info = contact_entry.get() 
    if hospital_name and department_name and user_name and contact_info:
        res = f"Welcome {user_name} to {hospital_name} - {department_name} Department"
        label.configure(text=res)
        status_label.configure(text=f"Thank you, {user_name}! Your contact info: {contact_info}", fg="green")
        txt.delete(0, tk.END)
        name_entry.delete(0, tk.END)
        contact_entry.delete(0, tk.END)
        combo.set('')  
    else:
        status_label.configure(text="Please fill in all fields!", fg="red")
submit_button = tk.Button(window, text="Submit", bg="orange", fg="red", font=('Arial', 12), command=submit)
submit_button.grid(column=0, row=5, columnspan=3, pady=20)
def clear():
    txt.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    contact_entry.delete(0, tk.END)
    combo.set('')  
    label.configure(text="Welcome to the Hospital") 
    status_label.configure(text="", fg="green")  
clear_button = tk.Button(window, text="Clear", bg="lightblue", fg="black", font=('Arial', 12), command=clear)
clear_button.grid(column=0, row=6, columnspan=3, pady=10)
window.mainloop()
