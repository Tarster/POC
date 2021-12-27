import tkinter
from tkinter import *

# Class RegisterPageUI

class ErroUI:
    def __init__(self):
        # This is root widget
        self.top = tkinter.Tk()
        
        # This is the property of root window
        self.top.title("Error Window") #This is to change the title of the page 
        # TODO: Set resolution depending on screen
        self.top.geometry("300x300") #pick size depending on the screen     
        
        #TODO: MAKE THE TEXT DYNAMIC
        # User label for entering the username
        L1 = Label(self.top, text = "There is some error try again.")
        L1.grid(row = 0,column = 0)       

        # The button to exit the program 
        close_button = tkinter.Button(self.top, text = "OK", command = self.top.destroy) # root.quit
        close_button.grid(row = 1, column = 0)

        self.top.mainloop()


Window = ErrorUI()