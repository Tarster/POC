import os
import sys
import tkinter
from tkinter import *
path = os.path.join(os.getcwd(),'Auth')
# print(path)
sys.path.insert(1, path)
from auth import *
from UI_Error import *
from UI_Login import *
# Class RegisterPageUI

class RegisterPageUI:
    def __init__(self):

        # This is root widget
        self.top = tkinter.Tk()
        
        # This is the property of root window
        self.top.title("Registration Window") #This is to change the title of the page 
        # TODO: Set resolution depending on screen
        self.top.geometry("1280x720") #pick size depending on the screen     
        
        # User label for entering the username
        L1 = Label(self.top, text = "User Name")
        L1.grid(row = 0,column = 0)
        
        # The actual text field where we are entering the username
        E1 = Entry(self.top, bd = 5)
        E1.grid(row = 0, column = 1) 
        
        # The label for the Password Field 
        L2 = Label(self.top, text="Password")
        L2.grid(row = 1, column = 0)

        # The actual textfield for the password field
        E2 = Entry(self.top, bd = 5)
        E2.grid(row = 1, column = 1)

        # The label for the Confirm Password Field 
        L3 = Label(self.top, text="Confirm Password")
        L3.grid(row = 2, column = 0)

        # The actual textfield for the Confirm password field
        E3 = Entry(self.top, bd = 5)
        E3.grid(row = 2, column = 1)

        # The button to exit the program 
        exit_button = tkinter.Button(self.top, text = "EXIT", command = self.top.destroy) # root.quit
        exit_button.grid(row = 3, column = 0)

        #The button to login into the program
        #When this button is clicked move to the Login page window.
        login_button = tkinter.Button(self.top, text = "LOGIN")#command = login_callback)
        login_button.grid(row = 3, column = 1)

        #The button to register a new user in the program
        registration_button = tkinter.Button(self.top, text="REGISTER", command = register_callback)
        registration_button.grid(row = 3, column = 2)

        self.top.mainloop()
         

Window = RegisterPageUI()

