import os
import pandas as pd
import traceback

class General_Task(object):
    """
    This class will provide general functionality for login.
    """

    def val(self, email:str, password:str, confirm_password:str)-> bool|str:
        """
        This method validates the input that are being passed to the 

        email (str): The email address of the user
            password (str): The password of the user
            confirm_password (str): Confirm password for the user

        Returns:
            bool,str: bool for a status and str for the message
        """
        # Return 2 value a status and a string to print the error
        s = ""
        if email.strip() == "":
            s = s + 'Email is Empty.\n'
        
        if password.strip() == "":
            s = s + 'Password is Empty.\n'
        if confirm_password.strip() == "":
            # throw an error here that either email, password and confirm_password
            s = s + 'Confirm Password is Empty.'
        if s != "":
            return False, s

        if password != confirm_password:
            # throw an error password is not same
            s = "Password and Confirm Password doesn't match"
            return False, s

        else:
            return True, None

    # this is to validate the login details.
    def login_val(self, email, password):
        """
        This method will validate the login credentials 
         Args:
            email (str): Pass the email
            password (str): Pass the password

        Returns:
            bool, string: This will return a bool and a string.
        """
        s = ""
        if email.strip() == "":
            s = s + 'Email is Empty.\n'
        if password.strip() == "":
            s = s + 'Password is Empty.\n'

        if s != "":
            return False, s
        # if condition is true just send True and None
        return True, None

    # Checking if file exists in  the system
    def file_checker(self):
        """
        This method will check for the file in the specified path

        Returns:None
        """
        # Create the path and check if file exists at that path
        path = os.path.join(os.getcwd(), 'Auth\\auth.xlsx')
        if os.path.exists(path):
            return True
        else:
            # Create a new file and display the following output.
            print("File doesn't exist here. Either you are running program for the first time or the file is removed.")
            # Create a Data Frame to have Email and Password field
            create_df = pd.DataFrame(columns=['Email', 'Password'])
            print("Creating a new auth file now.")
            create_df.to_excel(path, index=False)
            return False


class Registration(object):
    """
    This class is for registering the user into the program.
    """

    def register(self, email:str, password:str, confirm_password:str)->bool|str:
        """
        This method is being used to register the user into the application
        Args:
            email (str): The email address of the user
            password (str): The password of the user
            confirm_password (str): Confirm password for the user

        Returns:
            bool,str: bool for a status and str for the message
        """
        # Creating the general object for validation
        new_task = General_Task()
        status, message = new_task.val(email=email, password=password, confirm_password=confirm_password)

        if status == False:
            # Throw this error in the frontend
            return False, message

        if status == True:
            try:
                path = os.path.join(os.getcwd(), 'Auth\\auth.xlsx')
                print(path)
                # Add email and password to the xlsx file
                df = pd.read_excel(path)
                # appending the list to the df
                df.loc[len(df.index)] = [email, password]
                # Overwriting the excel file
                df.to_excel(path, index=False)
                return True, "User Successfully Registered"
            except Exception:
                traceback.print_exc()
                return False,"Something went wrong!!!"

class Login:
    """
    This class helps in logging in to the application.
    """
    def login(self, email:str, password:str)->bool|str:
        """
        Args:
            email (str): Pass the email
            password (str): Pass the password

        Returns:
            bool, string: This will return a bool and a string. 
        """
        # Creating General_Task object
        task = General_Task()
        # Checking for validation
        status, s = task.login_val(email, password)

        if status == False:
            return False, s
            # throw it to the UI
        else:
            try:
                path = os.path.join(os.getcwd(), 'Auth\\auth.xlsx')
                # Reading the excel into the data frame
                df = pd.read_excel(path)
                # print(list(df['Email']))

                # If email exist in the database
                if email in list(df['Email']):
                    index = df[df['Email'] == email].index[0]
                    if df._get_value(index, 'Password') == password:
                        # Grant access to the user
                        return True, None
                    else:
                        s = "You have entered a wrong password."
                        return False, s
                # Email doesn't exist in the database
                else:
                    s = "Email does not exist in the database. Please do the registration first."
                    return False, s
            except Exception:
                traceback.print_exc()
                return False, "Something went wrong!!!!"