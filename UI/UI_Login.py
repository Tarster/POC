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


# Class LoginPageUI
class LoginPageUI:
    def __init__(self):
        
        #Creating Registration object
        log = Login()

        #Function to be called when we click on the register button
        def login_callback():
        # print(type(E1.get()), type(E2.get()), type(E3.get()))
            status, message = log.login(E1.get(), E2.get())
            if status == False:
                err = ErrorUI(message=message)
            else:
                # Success and Error windows are showing fine here
                login_widget.destroy()
            
        
        # This is root widget
        self.login_widget = tkinter.Tk()
        # This is the property of root window
        self.login_widget.title("Login Window") #This is to change the title of the page 
        # TODO: Set resolution depending on screen
        self.login_widget.geometry("1280x720") #pick size depending on the screen     
        
        # User label for entering the username
        L1 = Label(self.login_widget, text = "User Name")
        L1.grid(row = 0,column = 0)
        
        # The actual text field where we are entering the username
        E1 = Entry(self.login_widget, bd = 5)
        E1.grid(row = 0, column = 1) 
        
        # The label for the Password Field 
        L2 = Label(self.login_widget, text="Password")
        L2.grid(row = 1, column = 0)

        # The actual textfield for the password field
        E2 = Entry(self.login_widget, bd = 5)
        E2.grid(row = 1, column = 1)

        # The button to exit the program 
        exit_button = tkinter.Button(self.login_widget, text = "EXIT", command = self.login_widget.destroy) # root.quit
        exit_button.grid(row = 2, column = 0)

        #The button to login into the program
        login_button = tkinter.Button(self.login_widget, text = "LOGIN", command = login_callback)
        login_button.grid(row = 2, column = 1)

        #The button to register a new user in the program
        #When we click on this button. Change the current page to Register and close the previous page
        registration_button = tkinter.Button(self.login_widget, text="REGISTER")#, command = register_callback)
        registration_button.grid(row = 2, column = 2)

        self.login_widget.mainloop()


Window = LoginPageUI()
