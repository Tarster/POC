import os
import sys
import pandas as pd

global df 

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
            return  True , None

    def login_val(self, email, password):
        s = ""
        if email.strip() == "":
            s = s + 'Email is Empty.\n'
        if password.strip() == "": 
            s = s + 'Password is Empty.\n'
        
        if s != "":
            return False, s
        
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
            create_df.to_excel(path)
            return False

class Registration:
    # def __init__(self):
    #     self.email = ""
    #     self.password = ""
    #     self.confirm_password =""
    
    def register(self, email,password,confirm_password):
        new_task = General_Task()
        
        status, message = new_task.val(email = email, password = password, confirm_password = confirm_password)
        
        if status == False:
            # Throw this error in the frontend
            print(message)
            return False

        if status == True:
           path = os.path.join(os.getcwd(),'Auth\\auth.xlsx')
           #Add email and password to the xlsx file
           df = pd.read_excel(path)
           #creating the list 
           list_var = [email , password] 
           #appending the list to the df
           df_len = len(df)
           print(df_len)
           print(f"df is {df.head()}")
           df.loc[df_len] = list_var

           #delete the previous file
           os.remove(path)
           df.to_excel(path)
           return True


class Login:
    def login(self, email, password):
        task = General_Task()
        status,s =task.login_val(email, password)        
        if status == False:
            print(s)
            #throw it to the UI
        else:
            path = os.path.join(os.getcwd(),'Auth\\auth.xlsx')
            df = pd.read_excel(path)

            #IF email exist in the database 
            if email in df['Email']:
                if password in df['Password']:
                    #Grant access to the user
                    pass
                else:
                    print("You have entered a wrong password.")            
            
            #Email doesn't exist in the database
            else:
                print("Email does not exist in the database. Please do the registration first")

#Calling things here
task = General_Task()
task.file_checker()
