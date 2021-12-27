import tkinter
from tkinter import *

# Class LoginPageUI

class LoginPageUI:
    def __init__(self):
        # This is root widget
        self.top = tkinter.Tk()
        # This is the property of root window
        self.top.title("Login Window") #This is to change the title of the page 
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

        # The button to exit the program 
        exit_button = tkinter.Button(self.top, text = "EXIT", command = self.top.destroy) # root.quit
        exit_button.grid(row = 2, column = 0)

        #The button to login into the program
        login_button = tkinter.Button(self.top, text = "LOGIN")#command = login_callback)
        login_button.grid(row = 2, column = 1)

        #The button to register a new user in the program
        #When we click on this button. Change the current page to Register and close the previous page
        registration_button = tkinter.Button(self.top, text="REGISTER")#, command = register_callback)
        registration_button.grid(row = 2, column = 2)

        self.top.mainloop()


Window = LoginPageUI()


