
from tkinter import Tk, Label,Button

# Class RegisterPageUI

class RunUI(object):
    """
    This class is run after we successfully get authenticated.
    """
    def __init__(self):
        # This is root widget
        self.top = Tk()
        
        # This is the property of root window
        self.top.title("Error Window") #This is to change the title of the page 
        self.top.geometry("325x100") #pick size depending on the screen     
        
        # User label for entering the username
        L1 = Label(self.top, text = "Website to Run.")
        L1.grid(row = 0,column = 0)       

        # The button to exit the program 
        close_button = Button(self.top, text = "EXIT", command = self.top.destroy) # root.quit
        close_button.grid(row = 1, column = 0)

        # The button to RUN the program 
        close_button = Button(self.top, text = "RUN", command = None) # root.quit
        close_button.grid(row = 1, column = 1)

        self.top.mainloop()