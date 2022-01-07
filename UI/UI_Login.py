import os
import sys
import tkinter
from tkinter import *
from UI_Error import StatusUI
from UI_Run import RunUI
#Custom module import from another python file in different folder 
path = os.path.join(os.getcwd(),'Auth')
# path = "D:\TCS\POC\Auth"
sys.path.insert(1, path)
from auth import *

# Class LoginPageUI
class LoginPageUI:
    
    def __init__(self):    
        #Creating Registration object
        log = Login()        
        
        #Method to close the window
        def close(widget):
            widget.destroy()

        #Function to be called when we click on the register button
        def login_callback(widget):
            status, message = log.login(E1.get(), E2.get())
            if status == False:
                err = StatusUI(message=message)
            else:
                # Success and Error windows are showing fine here
                close(widget)
                run = RunUI()

        
        # Function to be called when register button is clicked 
        def register_callback(widget):    
            #Creating registration object
            close(widget)
            reg_window = RegisterPageUI()
           
        # This is root widget
        self.login_widget = tkinter.Tk()
        # This is the property of root window
        self.login_widget.title("Login Window") #This is to change the title of the page 
        # TODO: Set resolution depending on screen
        self.login_widget.geometry("300x500") #pick size depending on the screen     
        
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
        exit_button = tkinter.Button(self.login_widget, text = "EXIT", command = lambda:close(self.login_widget)) # root.quit
        exit_button.grid(row = 2, column = 0)
        
        #The button to login into the program
        login_button = tkinter.Button(self.login_widget, text = "LOGIN", command = lambda:login_callback(self.login_widget))
        login_button.grid(row = 2, column = 1)
        
        #The button to register a new user in the program
        #When we click on this button. Change the current page to Register and close the previous page
        registration_button = tkinter.Button(self.login_widget, text="REGISTER", command = lambda: register_callback(self.login_widget))
        registration_button.grid(row = 2, column = 2)
    
        self.login_widget.mainloop()
        

class RegisterPageUI:
    def __init__(self):
        
        #registration class object
        reg = Registration()
        #Method to close the window
        def close(widget):
            widget.destroy()

        #Function to be called when we click on the register button
        def register_callback(widget):
            status, message = reg.register(E1.get(), E2.get(),E3.get())
            if status == False:
                sta = StatusUI(message=message)
            else:
                # Success and Error windows are showing fine here
                close(widget)
                log_window = LoginPageUI()

        
        # Function to be called when register button is clicked 
        def login_callback(widget):    
            #Creating registration object
            close(widget)
            log_window = LoginPageUI()
           
        # This is root widget
        self.top = tkinter.Tk()
        
        # This is the property of root window
        self.top.title("Registration Window") #This is to change the title of the page 
        # TODO: Set resolution depending on screen
        self.top.geometry("300x500") #pick size depending on the screen     
        
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
        exit_button = tkinter.Button(self.top, text = "EXIT", command = lambda:destroy(self.top)) # root.quit
        exit_button.grid(row = 3, column = 0)

        #The button to login into the program
        #When this button is clicked move to the Login page window.
        login_button = tkinter.Button(self.top, text = "LOGIN",command = lambda:login_callback(self.top))
        login_button.grid(row = 3, column = 1)

        #The button to register a new user in the program
        registration_button = tkinter.Button(self.top, text="REGISTER", command = lambda: register_callback(self.top))
        registration_button.grid(row = 3, column = 2)

        self.top.mainloop()

Window = LoginPageUI()