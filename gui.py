import tkinter
from tkinter import *



# System GUI--------------------------------------------------------------------------------

root = Tk()
title = root.title("BSCS CRUD System")
root.geometry('1280x720')


mainLabel = Label(root, text= "Enter Student Information", font=('Ariel', 15),)
mainLabel.grid(row=1, column=0, padx=10, pady=10)


root.mainloop()


