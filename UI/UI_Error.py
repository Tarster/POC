from tkinter import Tk,Label, Button

# Class RegisterPageUI

class StatusUI(object):
    """
    This is a class to show the pop up status message.
    """
    def __init__(self,message:str)->None:
        """
        This will take a message and make the UI to display it

        Args:
            message(str): The message that needs to be displayed.
        """
        # This is root widget
        self.top = Tk()
        
        # This is the property of root window
        self.top.title("status Window") #This is to change the title of the page 
        
        self.top.geometry("400x100") #pick size depending on the screen     
        
        # User label for entering the username
        L1 = Label(self.top, text = message)
        L1.grid(row = 0,column = 0)       

        # The button to exit the program 
        close_button = Button(self.top, text = "OK", command = self.top.destroy) # root.quit
        close_button.grid(row = 1, column = 0)

        self.top.mainloop()
