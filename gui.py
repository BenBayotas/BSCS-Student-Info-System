import sqlite3
import tkinter
from tkinter import ttk
from tkinter import *




# System GUI--------------------------------------------------------------------------------------------------------------
root = Tk()
title = root.title("BSCS CRUD System")
root.geometry('930x300')
display = ttk.Treeview(root)
sms = "Student Management System"


mainLabel = Label(root, text= "Enter Student Information", font=('Ariel', 15))
mainLabel.grid(row=0, column=0, columnspan=25, padx=5, pady=5)


#CRUD Functions------------------------------------------------------------------------------------------------------------
def reverse(tuples):
    func_tup = tuples[::-1]
    return func_tup

def insert(sidEntry,nameEntry,ugsuiteEntry,courseEntry,yearEntry):
    conn=sqlite3.connect("data.db")
    cursor=conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS Student Information(sidEntry TEXT,nameEntry TEXT,ugsuiteEntry TEXT,courseEntry TEXT,yearEntry TEXT)""")
    cursor.execute("INSERT INTO Student Information VALUES('"+str(sidEntry)+"','"+str(nameEntry)+'","'+str(ugsuiteEntry)+'","'+str(courseEntry)+'","'+str(yearEntry)+"')")
    conn.commit()


def delete(data):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS Student Information(sidEntry TEXT,nameEntry TEXT,ugsuiteEntry TEXT,courseEntry TEXT,yearEntry TEXT)""")
    cursor.execute("DELETE FROM Student Information WHERE sidEntry='"+str(data)+"'")
    conn.commit()


def update(sidEntry,nameEntry,ugsuiteEntry,courseEntry,yearEntry):
    conn=sqlite3.connect("data.db")
    cursor=conn.cursor()
    cursor.execute("UPDATE Student Information SET StudentID='"+str(sidEntry)+"',FullName='"+str(nameEntry)+"',GsuiteEmail='"+str(ugsuiteEntry)+"',Course='"+str(courseEntry)+"',YearLevel='"+str(yearEntry)+"')")
    conn.commit()


def read():
    conn=sqlite3.connect("data.db")
    cursor=conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Student Information(sidEntry TEXT,nameEntry TEXT,ugsuiteEntry TEXT,courseEntry TEXT,yearEntry TEXT)""")
    cursor.execute("SELECT * FROM Student Information")
    results=cursor.fetchall()
    conn.commit()
    return results



#Inserting Data--------------------------------------------------------------------------------------------------------------
def insert_data():
    studentID=str(sidEntry.get())
    fname=str(nameEntry.get())
    ugsuite=str(ugsuiteEntry.get())
    course=str(courseEntry.get())
    yearlvl=str(yearEntry.get())
    if studentID == ""or studentID =="":
        print("Error Inserting Student ID")
    if fname == ""or fname =="":
        print("Error Inserting Full Name")
    if ugsuite == ""or ugsuite =="":
        print("Error Inserting Urios Gsuite")
    if course == ""or course =="":
        print("Error Inserting Course")
    if yearlvl == ""or yearlvl =="":
        print("Error Inserting Year Level")
    else:
        insert(str(studentID),str(fname),str(ugsuite),str(course),str(yearlvl))

    for data in display.get_children():
        display.delete(data)
    
    for result in reverse(read()):
        display.insert(parent='',index='end',iid=0,text="",values=(result),tag="sms")

    












#Labels-------------------------------------------------------------------------------------------------------------------
sidLabel = Label(root, text="Student ID", font=('Ariel', 13))
nameLabel = Label(root, text="Full Name", font=('Ariel', 13))
ugsuiteLabel = Label(root, text="Urios Gsuite", font=('Ariel', 13))
courseLabel = Label(root, text="Course", font=('Ariel', 13))
yearLabel = Label(root, text="Year Level", font=('Ariel', 13))
sidLabel.grid(row=3, column=0)
nameLabel.grid(row=4, column=0)
ugsuiteLabel.grid(row=5, column=0)
courseLabel.grid(row=6, column=0)
yearLabel.grid(row=7, column=0)


#Entry--------------------------------------------------------------------------------------------------------------------
sidEntry = Entry(root, width=33, font=('Ariel', 13))
nameEntry = Entry(root, width=33, font=('Ariel', 13))
ugsuiteEntry = Entry(root, width=33, font=('Ariel', 13))
courseEntry = Entry(root, width=33, font=('Ariel', 13))
yearEntry = Entry(root, width=33, font=('Ariel', 13))
sidEntry.grid(row=3, column=1, columnspan=5, padx=5, pady=5)
nameEntry.grid(row=4, column=1, columnspan=5, padx=5, pady=5)
ugsuiteEntry.grid(row=5, column=1, columnspan=5, padx=5, pady=5)
courseEntry.grid(row=6, column=1, columnspan=5, padx=5, pady=5)
yearEntry.grid(row=7, column=1, columnspan=5, padx=5, pady=5)


#Buttons------------------------------------------------------------------------------------------------------------------
addButton = Button(root, text="Add Entry", font=('Ariel', 11), padx=5, pady=5)
addButton.grid(row=9, column=1)

upButton = Button(root, text="Update Entry", font=('Ariel', 11), padx=5, pady=5)
upButton.grid(row=9, column=2)

delButton = Button(root, text="Delete Entry", font=('Ariel', 11), padx=5, pady=5)
delButton.grid(row=9, column=3)


#Display Database-------------------------------------------------------------------------------------------------------------
style=ttk.Style()
style.configure("Treeview.Heading",font=('Ariel bold',13))
display['columns']=("Student ID","Full Name","Urios Gsuite","Course","Year Level")
display.column("#0", width=0,stretch=NO)
display.column("Student ID", anchor=W,width=100)
display.column("Full Name", anchor=W,width=100)
display.column("Urios Gsuite", anchor=W,width=100)
display.column("Course", anchor=W,width=100)
display.column("Year Level", anchor=W,width=100)
display.heading("Student ID", text="Student ID",anchor=W)
display.heading("Full Name", text="Full Name",anchor=W)
display.heading("Urios Gsuite", text="Urios Gsuite",anchor=W)
display.heading("Course", text="Course",anchor=W)
display.heading("Year Level", text="Year Level",anchor=W)


display.tag_configure('sms',background="#EEEEEE",font=('Arial bold', 13))
display.grid(row=3,column=6,columnspan=8,rowspan=20,padx=10,pady=10)




root.mainloop()