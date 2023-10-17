# Importing libraries
from tkinter import *
import customtkinter

#create CTk window like you do with the Tk window
root = customtkinter.CTk()

#Setting Widow width and Height
root.geometry('300x400')

#Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=root, text='hello world!', font=("Calibry", 14))


#showing at the center of the screen
button.place(relx=0.5, rely=0.5, anchor=CENTER)

#Running the app
root.mainloop()