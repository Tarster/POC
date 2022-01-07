import os
import sys
import pandas as pd
class General_Task:
    
    #Return 2 value a status and a string to print the error
    def val(self,email, password,confirm_password):
        s = ""
        if email.strip() == "":
            s = s + 'Email is Empty.\n'
        if password.strip() == "": 
            s = s + 'Password is Empty.\n'
        if confirm_password.strip() == "":
            #throw an error here that either email, password and confirm_password
            s = s + 'Confirm Password is Empty.' 
        if s != "":
            return False, s

        if password != confirm_password:
            #throw an error password is not same
            s = "Password and Confirm Password doesn't match"
            return False, s
        
        else:
            return  True, None
    #this is to validate the login details.
    def login_val(self, email, password):
        s = ""
        if email.strip() == "":
            s = s + 'Email is Empty.\n'
        if password.strip() == "": 
            s = s + 'Password is Empty.\n'
        
        if s != "":
            return False, s
        #if condition is true just send True and None
        return True, None
    
#Checking if file exists in  the system
    def file_checker(self):
        path = os.path.join(os.getcwd(),'Auth\\auth.xlsx')
        # print(path)
        if os.path.exists(path):
            # print("File exists")
            # df = pd.read_excel(path)
            # print(df['Email'])
            return True
        else:
            #Create a new file and display the following output.
            print("File doesn't exist here. Either you are running program for the first time or the file is removed.")
            # Create a dataframe to have Email and Password field
            create_df = pd.DataFrame(columns=['Email','Password'])
            print("Creating a new auth file now.")
            create_df.to_excel(path,index=False)
            return False

class Registration:
    
    def register(self, email, password, confirm_password):
        #Creating the general object for validation
        new_task = General_Task()
        status, message = new_task.val(email = email, password = password, confirm_password = confirm_password)
        
        if status == False:
            # Throw this error in the frontend
            # print(message)
            return False, message

        if status == True:
           path = os.path.join(os.getcwd(),'Auth\\auth.xlsx')
           #Add email and password to the xlsx file
           df = pd.read_excel(path)
           #appending the list to the df
           df.loc[len(df.index)] = [email, password] 
        #  print(df.head())
           #Overwriting the excel file
           df.to_excel(path,index = False)
           return True,"User Successfully Registered"


class Login:
    
    def login(self, email, password):
        #Creating General_Task object
        task = General_Task()
        #Checking for validation
        status,s =task.login_val(email, password)        
        
        if status == False:
            return False, s
            #throw it to the UI
        else:
            path = os.path.join(os.getcwd(),'Auth\\auth.xlsx')
            #Reading the excel into the dataframe
            df = pd.read_excel(path)
            # print(list(df['Email']))

            #If email exist in the database 
            if email in list(df['Email']):
                index = df[df['Email'] == email].index[0] 
                if df._get_value(index, 'Password') == password:
                    #Grant access to the user
                    # print("I am in.")
                    return True,None
                else:
                    s = "You have entered a wrong password."            
                    return False, s
            #Email doesn't exist in the database
            else:
                s = "Email does not exist in the database. Please do the registration first."
                return False, s