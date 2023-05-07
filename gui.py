import sqlite3
import tkinter
from tkinter import *
from tkinter import ttk

#CRUD Functions-----------------------------------------------------------------------------

conn = sqlite3.connect('student.db')
c = conn.cursor()

c.execute(""" CREATE TABLE IF NOT EXISTS stuInfo(
    stu_Id INTEGER,
    stu_gsuite TEXT,
    stu_name TEXT,
    stu_course TEXT,
    stu_year INTEGER)""")



def clear():
    idEntry.delete(0, END)
    gsuiteEntry.delete(0, END)
    nameEntry.delete(0, END)
    courseEntry.delete(0, END)
    yearEntry.delete(0, END)



def reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup



def insert(id, gsuite, name, course, year):
    conn = sqlite3.connect('student.db')
    c = conn.cursor()

    c.execute("INSERT INTO stuInfo VALUES ('" + str(id) + "', '" + str(gsuite) + "', '" + str(name) + "', '" + str(course) + "', '" + str(year) + "')")
    conn.commit()



def update(id, gsuite, name, course, year, idName):
    conn = sqlite3.connect('student.db')
    c = conn.cursor()

    c.execute("UPDATE stuInfo SET stu_Id = '" + str(id) + "', stu_gsuite = '" + str(gsuite) + "', stu_name = '" + str(name) + "', stu_course = '" + str(course) + "', stu_year = '" + str(year) + "' WHERE stu_Id = '" + str(idName) + "' ")
    conn.commit()



def delete(data):
    conn = sqlite3.connect('student.db')
    c = conn.cursor()

    c.execute("DELETE FROM stuInfo WHERE stu_Id = '" + str(data) +  "'  ")
    conn.commit()


def read():
    conn = sqlite3.connect('student.db')
    c = conn.cursor()

    c.execute("SELECT * FROM stuInfo")
    results = c.fetchall()
    conn.commit()
    return results


def viewtable():
    for data in table.get_children():
        table.delete(data)

    for result in reverse(read()):
        table.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")   

    table.tag_configure('orow', background='#EEEEEE', font=('Ariel', 11))
    table.grid(row=6, column=0, columnspan=5, rowspan=10, padx=5, pady=5)



def add_data():
    stu_Id = str(idEntry.get())
    stu_gsuite = str(gsuiteEntry.get())
    stu_name = str(nameEntry.get())
    stu_course = str(courseEntry.get())
    stu_year = str(yearEntry.get())
    if stu_Id == "" or stu_Id == " ":
        print("Invalid Entry")
    if stu_gsuite == "" or stu_gsuite == " ":
        print("Invalid Entry")
    if stu_name == "" or stu_name == " ":
        print("Invalid Entry")
    if stu_course == "" or stu_course == " ":
        print("Invalid Entry")
    if stu_year == "" or stu_year == " ":
        print("Invalid Entry")
    else:
        insert(str(stu_Id), str(stu_gsuite), str(stu_name), str(stu_course), str(stu_year))
    viewtable()
    clear()


def update_data():
    selected_entry = table.selection()[0]
    update_entry = table.item(selected_entry)['values'][0]
    update(idEntry.get(), gsuiteEntry.get(), nameEntry.get(), courseEntry.get(), yearEntry.get(), update_entry)
    viewtable()
    clear()



def delete_data():
    selected_entry = table.selection()[0]
    delete_entry = str(table.item(selected_entry)['values'][0])   
    delete(delete_entry)
    viewtable()
    clear()





# System GUI--------------------------------------------------------------------------------

root = Tk()
title = root.title("BSCS CRUD System")
table = ttk.Treeview(root)
root.geometry('911x500')


mainLabel = Label(root, text= "BSCS Student Information", font=('Ariel', 15))
mainLabel.grid(row=0, column=0, columnspan=8, padx=20, pady=20)


idLabel = Label(root, text="Student ID", font=('Ariel', 13))
gsuiteLabel = Label(root, text="Gsuite", font=('Ariel', 13))
nameLabel = Label(root, text="Complete Name", font=('Ariel', 13))
courseLabel = Label(root, text="Course", font=('Ariel', 13))
yearLabel = Label(root, text="Year Level", font=('Ariel', 13))
idLabel.grid(row=1, column=0, padx=3, pady=3)
gsuiteLabel.grid(row=2, column=0, padx=3, pady=3)
nameLabel.grid(row=3, column=0, padx=3, pady=3)
courseLabel.grid(row=4, column=0, padx=3, pady=3)
yearLabel.grid(row=5, column=0, padx=3, pady=3)


idEntry = Entry(root, width=33, font=('Ariel', 13))
gsuiteEntry = Entry(root, width=33, font=('Ariel', 13))
nameEntry = Entry(root, width=33, font=('Ariel', 13))
courseEntry = Entry(root, width=33, font=('Ariel', 13))
yearEntry = Entry(root, width=33, font=('Ariel', 13))
idEntry.grid(row=1, column=1, padx=3, pady=3)
gsuiteEntry.grid(row=2, column=1, padx=3, pady=3)
nameEntry.grid(row=3, column=1, padx=3, pady=3)
courseEntry.grid(row=4, column=1, padx=3, pady=3)
yearEntry.grid(row=5, column=1, padx=3, pady=3)


addButton = Button(root, text="Add Entry", font=('Ariel', 13), bd=3, width=20, command=add_data)
addButton.grid(row=1, column=2, padx=3, pady=3)

upButton = Button(root, text="Update Entry", font=('Ariel', 13), bd=3, width=20, command=update_data)
upButton.grid(row=2, column=2, padx=3, pady=3)

delButton = Button(root, text="Delete Entry", font=('Ariel', 13), bd=3, width=20, command=delete_data)
delButton.grid(row=3, column=2, padx=3, pady=3)

style = ttk.Style()
style.configure("Treeview.Heading", font=('Ariel', 13))

table['columns'] = ("Student ID", "Gsuite", "Name", "Course", "Year")
table.column("#0", width=0, stretch=NO)
table.column("Student ID", width=100, anchor=W)
table.column("Gsuite", width=200, anchor=W)
table.column("Name", width=200, anchor=W)
table.column("Course", width=200, anchor=W)
table.column("Year", width=200, anchor=W)
table.heading("Student ID", text="Student ID", anchor=W)
table.heading("Gsuite", text="Gsuite Account", anchor=W)
table.heading("Name", text="Name", anchor=W)
table.heading("Course", text="CSP Course", anchor=W)
table.heading("Year", text="Year Level", anchor=W)

viewtable()


conn.commit()
conn.close()

root.mainloop()