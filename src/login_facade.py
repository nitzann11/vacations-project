import re
from logic.bal import Bl
from modules.user import UserModule

class LoginFacade:

    @staticmethod
    def validate_password(password : str):
        """Static method to validate the password format""" 
        try:
            # Check if password is empty or None
            if password is None or password == "":
                raise ValueError("Password cannot be empty")
            
            # Regular expression pattern to match password with minimum length of 4 characters           
            pattern = r'^.{4,}$'
            if re.match(pattern, password):
                print(f"Valid password:", password)
                return True
            
            else:
                raise ValueError("Password must be at least 4 characters long")
            
        except ValueError as e:
            print(e)
            return False
        

    @staticmethod
    def validate_email(email : str):
        """Static method to validate the email format""" 
        try:
            # Check if email is empty or None
            if email is None or email == "":
                raise ValueError("Email cannot be empty")
            
            # Regular expression pattern to match email format      
            pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

            if re.match(pattern, email):
                print("Valid email:", email)
                return True
            
            else:
                raise ValueError("Invalid email format")

        except ValueError as ve:
            print(ve)
            return False
        
        except Exception as e:
            print("An error occurred while validating email:", e)
            raise
        
    
    @staticmethod
    def log_in(email_valid : bool, pass_valid : bool):
        """Static method to handle login functionality""" 
        try:
            if email_valid and pass_valid:
                print("Welcome!")
                return True
            elif not email_valid and not pass_valid:
                raise ValueError("Login failed: Email and password are invalid")
            elif not email_valid:
                raise ValueError("Login failed: Email is invalid")
            elif not pass_valid:
                raise ValueError("Login failed: Password is invalid")
        except ValueError as ve:
            print(ve)
            return False


    def register(u_email : str, u_password : str, valid_email : bool, valid_pass : bool, u_first_name : str, u_last_name : str, user_exists : bool):
        """Method to register a new user""" 
        if valid_email==True and valid_pass==True and user_exists==False:
            try:                              
                # Insert new user into the database
                user=Bl().insert_user(UserModule(user_id = None, first_name = u_first_name, last_name = u_last_name, email = u_email, password = u_password, role_id=2))
                print("user registered")
                return user
            
            except ValueError as err:
                print(err)
                     
        
    def check_user_exist(email : str):
        """Method to check if a user exists""" 
        try:
            search_result = Bl().get_all_users()
            for i in search_result:
                if i.email == email:
                    print("email in system")
                    return True
            else:
                print("email not in system")    
                return False
            
        except Exception as e:
            print("An error occurred while checking email existence:", e)
            
            
    @staticmethod
    def check_permission(email : str):
        """Static method to check user's permission based on email""" 
        try:
            fetch = Bl().get_all_users()
            for i in fetch:
                if i.email == email:
                    role = i.role_id
                    print(role)
                    return role                
            else:
                raise ValueError("User not found")
                        
        except Exception as e:
            print("An error occurred:", e)


    @staticmethod
    def check_permission_id(user_id : int):
        """Static method to check user's permission based on user ID""" 
        try:
            fetch = Bl().get_all_users()
            for i in fetch:
                if i.user_id == user_id:
                    role = i.role_id
                    print(role)
                    return role
                
            else:
                raise ValueError("User not found")
            
        except Exception as e:
            print("An error occurred:", e)    
                  