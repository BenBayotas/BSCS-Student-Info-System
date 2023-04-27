import sqlite3
import pymysql
from tkinter import *
from tkinter import tkt
from tkinter import messagebox
import tkinter as tk



#Connection Later








# System GUI--------------------------------------------------------------------------------


root = Tk()
title = root.title("BSCS CRUD System")
root.geometry('880x300')
mt_tree = ttk.Treeview(root)


#Functions Later
mainLabel = Label(root, text= "Enter Student Information", font=('Ariel', 15))
mainLabel.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

idLabel = Label(root, text="Student ID", font=('Ariel', 13))
lastnameLabel = Label(root, text="Last Name", font=('Ariel', 13))
firstnameLabel = Label(root, text="First Name", font=('Ariel', 13))
middlenameLabel = Label(root, text="Middle Name", font=('Ariel', 13))
courseLabel = Label(root, text="Course", font=('Ariel', 13))
yearLabel = Label(root, text="Year Level", font=('Ariel', 13))

idLabel.grid(row=3, column=0)
lastnameLabel.grid(row=4, column=0)
firstnameLabel.grid(row=5, column=0)
middlenameLabel.grid(row=6, column=0)
courseLabel.grid(row=7, column=0)
yearLabel.grid(row=8, column=0)


#Text Variable Later
idEntry = Entry(root, width=33, font=('Ariel', 13))
lastnameEntry = Entry(root, width=33, font=('Ariel', 13))
firstnameEntry = Entry(root, width=33, font=('Ariel', 13))
middlenameEntry = Entry(root, width=33, font=('Ariel', 13))
courseEntry = Entry(root, width=33, font=('Ariel', 13))
yearEntry = Entry(root, width=33, font=('Ariel', 13))

idEntry.grid(row=3, column=1, columnspan=5, padx=5, pady=5)
lastnameEntry.grid(row=4, column=1, columnspan=5, padx=5, pady=5)
firstnameEntry.grid(row=5, column=1, columnspan=5, padx=5, pady=5)
middlenameEntry.grid(row=6, column=1, columnspan=5, padx=5, pady=5)
courseEntry.grid(row=7, column=1, columnspan=5, padx=5, pady=5)
yearEntry.grid(row=8, column=1, columnspan=5, padx=5, pady=5)


#Command Later
addButton = Button(root, text="Add Entry", font=('Ariel', 11), padx=5, pady=5)
addButton.grid(row=9, column=1)

upButton = Button(root, text="Update Entry", font=('Ariel', 11), padx=5, pady=5)
upButton.grid(row=9, column=2)

delButton = Button(root, text="Delete Entry", font=('Ariel', 11), padx=5, pady=5)
delButton.grid(row=9, column=3)

searchButton = Button(root, text="Search Entry", font=('Ariel', 11), padx=5, pady=5)
searchButton.grid(row=9, column=4)

resetButton = Button(root, text="Reset Entry", font=('Ariel', 11), padx=5, pady=5)
resetButton.grid(row=9, column=5)

selectButton = Button(root, text="Select Entry", font=('Ariel', 11), padx=5, pady=5)
selectButton.grid(row=9, column=6)


addButton.grid(row=3, column=1, columnspan=5, padx=5, pady=5)
upButton.grid(row=4, column=1, columnspan=5, padx=5, pady=5)
delButton.grid(row=5, column=1, columnspan=5, padx=5, pady=5)
searchButton.grid(row=6, column=1, columnspan=5, padx=5, pady=5)
resetButton.grid(row=7, column=1, columnspan=5, padx=5, pady=5)
selectButton.grid(row=8, column=1, columnspan=5, padx=5, pady=5)

style=ttk.Style()
style.configure("Treeview.Heading",font=('Arial Bold',15))
my_tree['columns']=("StudentID", "Firstname", "Lastname", "Address", "Phone")

my_tree.column("#0",width=0,stretch=NO)


root.mainloop()


#CRUD Functions-----------------------------------------------------------------------------

