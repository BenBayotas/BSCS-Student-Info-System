import tkinter
from tkinter import *



# System GUI--------------------------------------------------------------------------------

root = Tk()
title = root.title("BSCS CRUD System")
root.geometry('1000x500')


mainLabel = Label(root, text= "Enter Student Information", font=('Ariel', 15))
mainLabel.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

idLabel = Label(root, text="Student Id", font=('Ariel', 13))
lastnameLabel = Label(root, text="Last Name", font=('Ariel', 13))
firstnameLabel = Label(root, text="First Name", font=('Ariel', 13))
middlenameLabel = Label(root, text="Last Name", font=('Ariel', 13))
courseLabel = Label(root, text="Course", font=('Ariel', 13))
yearLabel = Label(root, text="Year Level", font=('Ariel', 13))

idLabel.grid(row=3, column=0)
lastnameLabel.grid(row=4, column=0)
firstnameLabel.grid(row=5, column=0)
middlenameLabel.grid(row=6, column=0)
courseLabel.grid(row=7, column=0)
yearLabel.grid(row=8, column=0)


root.mainloop()
