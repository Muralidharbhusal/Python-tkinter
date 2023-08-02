import tkinter
from tkinter import ttk
from tkinter import messagebox

from establish_connection import establish_connection
cursor = establish_connection()


def submit_data():
    status = terms_check_var.get()
    if status == "Accepted":
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        title = title_combobox.get()
        age = age_spinbox.get()
        nationality = nationality_combobox.get()

        num_courses = num_courses_spinbox.get()
        num_semesters = num_semesters_spinbox.get()
        registration_status = reg_status_var.get()

        sql = f"""
                        INSERT INTO INFO (FIRST_NAME, LAST_NAME, TITLE, AGE, NATIONALITY, NUM_COURSES,
                        NUM_SEMESTER, REGISTRATION_STATUS) VALUES ('{first_name}', '{last_name}', '{title}', '{age}',
                        '{nationality}', '{num_courses}', '{num_semesters}', '{registration_status}')
                    """

        cursor.execute(sql)
        print("Data added successfully!")


    else:
        tkinter.messagebox.showwarning(title="Error", message="You have not accepted the terms and conditions")





window = tkinter.Tk()
window.title("Dta Entry Form")

frame = tkinter.Frame(window)
frame.pack()

# Saving user info
user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title_label = tkinter.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Ms."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

age_label = tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=100)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)


nationality_label = tkinter.Label(user_info_frame, text="Nationality")
nationality_combobox = ttk.Combobox(user_info_frame, values=["Nepal", "Singapore", "Japan"])
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


# Saving Course Info
courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)
registered_label = tkinter.Label(courses_frame, text="Registration Status")
reg_status_var = tkinter.StringVar(value="Not Registered")

registered_check = tkinter.Checkbutton(courses_frame, text="Currently Registered",
                                       variable=reg_status_var, onvalue="Registered", offvalue="Not Registered")
registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

num_courses_label = tkinter.Label(courses_frame, text="# Completed Courses")
num_courses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to='infinity')
num_courses_label.grid(row=0, column=1)
num_courses_spinbox.grid(row=1, column=1)

num_semesters_label = tkinter.Label(courses_frame, text="# Semesters")
num_semesters_spinbox = tkinter.Spinbox(courses_frame, from_=0, to='infinity')
num_semesters_label.grid(row=0, column=2)
num_semesters_spinbox.grid(row=1, column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


# Accept terms
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

terms_check_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text="I accept the terms and conditions",
                                  variable=terms_check_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)

# Button
button = tkinter.Button(frame, text="Submit", command=submit_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

window.mainloop()