import sqlite3
import tkinter
from tkinter import ttk
from tkinter import *




# System GUI--------------------------------------------------------------------------------------------------------------
root = Tk()
title = root.title("BSCS CRUD System")
root.geometry('710x500')
display = ttk.Treeview(root)
sms = "Student Management System"


#CRUD Functions------------------------------------------------------------------------------------------------------------


conn = sqlite3.connect('data.db')
c = conn.cursor()

c.execute(""" CREATE TABLE IF NOT EXISTS stuInfo(
    stu_Id INTEGER,
    stu_name TEXT,
    stu_gsuite TEXT,
    stu_course TEXT,
    stu_year INTEGER)""")




def clear():
    idEntry.delete(0, END)
    gsuiteEntry.delete(0, END)
    nameEntry.delete(0, END)
    courseEntry.delete(0, END)
    yearEntry.delete(0, END)   


def reverse(tuples):
    func_tup = tuples[::-1]
    return func_tup


def insert(id, name, gsuite, course, year):
    conn=sqlite3.connect("data.db")
    c =conn.cursor()
    c.execute("INSERT INTO stuInfo VALUES('"+str(id)+"','"+str(name)+'","'+str(gsuite)+'","'+str(course)+'","'+str(year)+"')")
    conn.commit()


def update(id, gsuite, name, course, year, idName):
    conn=sqlite3.connect("data.db")
    c =conn.cursor()
    c.execute("UPDATE stuInfo SET stu_Id ='"+str(id)+"', stu_name = '"+str(name)+"', stu_gsuite = '"+str(gsuite)+"',stu_course ='"+str(course)+"', stu_year = '"+str(year)+"' WHERE stu_Id = '" +str(idName)+ "'  ")
    conn.commit()


def delete(data):
    conn=sqlite3.connect("data.db")
    c =conn.cursor()
    c.execute("DELETE FROM stuInfo WHERE stu_Id = '" +str(data)+ "'  ")
    conn.commit()



def read():
    conn=sqlite3.connect("data.db")
    c =conn.cursor()
    c.execute("SELECT * FROM stuInfo")
    results= c.fetchall()
    conn.commit()
    return results



def viewtable():
    for data in display.get_children():
        display.delete(data)

    for result in reverse(read()):
        display.insert(parent='',index='end',iid=result,text="",values=(result),tag="sms")

    display.tag_configure('sms',background="#EEEEEE",font=('Arial bold', 11))
    display.grid(row=6,column=0,columnspan=5,rowspan=20,padx=5,pady=5)



#Inserting Data--------------------------------------------------------------------------------------------------------------
def insert_data():
    stu_Id = str(idEntry.get())
    stu_name = str(nameEntry.get())
    stu_gsuite = str(gsuiteEntry.get())
    stu_course = str(courseEntry.get())
    stu_year = str(yearEntry.get())
    if stu_Id == "" or stu_Id == " ":
        print("Invalid ID Entry")
    if stu_name == "" or stu_name == " ":
        print("Invalid Name Entry")
    if stu_gsuite == "" or stu_gsuite == " ":
        print("Invalid Gsuite Entry")
    if stu_course == "" or stu_course == " ":
        print("Invalid Course Entry")
    if stu_year == "" or stu_year == " ":
        print("Invalid Year Entry")
    else:
        insert(str(stu_Id), str(stu_name), str(stu_gsuite), str(stu_course), str(stu_year))

    viewtable()
    clear()
    
    

  



mainLabel = Label(root, text= "BSCS Student Information", font=('Ariel', 15))
mainLabel.grid(row=0, column=0, columnspan=8, padx=20, pady=20)


#Labels-------------------------------------------------------------------------------------------------------------------
idLabel = Label(root, text="Student ID", font=('Ariel', 13))
nameLabel = Label(root, text="Full Name", font=('Ariel', 13))
gsuiteLabel = Label(root, text="Urios Gsuite", font=('Ariel', 13))
courseLabel = Label(root, text="Course", font=('Ariel', 13))
yearLabel = Label(root, text="Year Level", font=('Ariel', 13))
idLabel.grid(row=1, column=0, padx=3, pady=3)
nameLabel.grid(row=2, column=0, padx=3, pady=3)
gsuiteLabel.grid(row=3, column=0, padx=3, pady=3)
courseLabel.grid(row=4, column=0, padx=3, pady=3)
yearLabel.grid(row=5, column=0, padx=3, pady=3)


#Entry--------------------------------------------------------------------------------------------------------------------
idEntry = Entry(root, width=33, font=('Ariel', 13))
nameEntry = Entry(root, width=33, font=('Ariel', 13))
gsuiteEntry = Entry(root, width=33, font=('Ariel', 13))
courseEntry = Entry(root, width=33, font=('Ariel', 13))
yearEntry = Entry(root, width=33, font=('Ariel', 13))
idEntry.grid(row=1, column=1, padx=3, pady=3)
nameEntry.grid(row=2, column=1, padx=3, pady=3)
gsuiteEntry.grid(row=3, column=1, padx=3, pady=3)
courseEntry.grid(row=4, column=1, padx=3, pady=3)
yearEntry.grid(row=5, column=1, padx=3, pady=3)


#Buttons------------------------------------------------------------------------------------------------------------------
addButton = Button(root, text="Add Entry", font=('Ariel', 13), bd=3, width=20)
addButton.grid(row=1, column=2, padx=3, pady=3)

upButton = Button(root, text="Update Entry", font=('Ariel', 13), bd=3, width=20)
upButton.grid(row=2, column=2, padx=3, pady=3)

delButton = Button(root, text="Delete Entry", font=('Ariel', 13), bd=3, width=20)
delButton.grid(row=3, column=2, padx=3, pady=3)


#Display Database-------------------------------------------------------------------------------------------------------------
style=ttk.Style()
style.configure("Treeview.Heading",font=('Ariel bold',13))

display['columns']=("Student ID", "Full Name", "Urios Gsuite", "Course", "Year Level")
display.column("#0", width=0,stretch=NO)
display.column("Student ID", anchor=W,width=100)
display.column("Full Name", anchor=W,width=200)
display.column("Urios Gsuite", anchor=W,width=200)
display.column("Course", anchor=W,width=100)
display.column("Year Level", anchor=W,width=100)
display.heading("Student ID", text="Student ID",anchor=W)
display.heading("Full Name", text="Full Name",anchor=W)
display.heading("Urios Gsuite", text="Urios Gsuite",anchor=W)
display.heading("Course", text="Course",anchor=W)
display.heading("Year Level", text="Year Level",anchor=W)

viewtable()


conn.commit()
conn.close()

root.mainloop()