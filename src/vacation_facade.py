from modules.vacation import VacationModule
from logic.bal import Bl
from datetime import datetime
from src.login_facade import LoginFacade

class VacationFacade:

    def __init__(self) -> None:
        self.bl=Bl()

    def create_vacation(self, vacation_info : str, country_id : int, vacation_start : str , vacation_end : str, vacation_price : int, pic_name : str, email : str):
        """Method to create a new vacation"""
        try:
            # Check user permission
            role = LoginFacade.check_permission(email)
            if role == "Admin":

                # Validate input dates and price
                today = datetime.today()
                vacation_start_input = datetime.strptime(vacation_start, '%Y-%m-%d')
                vacation_end_input = datetime.strptime(vacation_end, '%Y-%m-%d')
                if vacation_price <= 0 or vacation_price > 10000:
                    raise ValueError("Vacation price should be between 1 and 10000")
                if vacation_start_input >= vacation_end_input:
                    raise ValueError("Vacation start date should be before vacation end date")
                if vacation_start_input <= today:
                    raise ValueError("Vacation start date should be in the future")
                
                # Create VacationModule object
                # Insert new vacation
                vacation = VacationModule(vacation_id=None, vacation_info=vacation_info, country_id=country_id,
                                           vacation_start=vacation_start, vacation_end=vacation_end,
                                           price=vacation_price, pic_name=pic_name)
                self.bl.insert_vacation(vacation)
                print("Vacation added")
                return vacation
            elif role == "User":
                print("Wrong permission")
        except ValueError as ve:
            print("Error:", ve)
        except Exception as e:
            print("An unexpected error occurred:", e)
            raise


            


    def update_existing_vacation(self, email : str, vacation_id : int, vacation_info : str, country_id : int, vacation_start : str, vacation_end :str, vacation_price : int, pic_name : str = None):
        """Method to update an existing vacation"""
        try:
            # Check user permission
            role = LoginFacade.check_permission(email)
            if role == "Admin":

                # Validate input dates and price
                today = datetime.today()
                vacation_start_input = datetime.strptime(vacation_start, '%Y-%m-%d')
                vacation_end_input = datetime.strptime(vacation_end, '%Y-%m-%d')
                if vacation_price <= 0 or vacation_price > 10000:
                    raise ValueError("Vacation price should be between 1 and 10000")
                if vacation_start_input >= vacation_end_input:
                    raise ValueError("Vacation start date should be before vacation end date")
                if vacation_start_input <= today:
                    raise ValueError("Vacation start date should be in the future")
                
                # Get the old vacation details               
                vacation_search = self.bl.get_vacation_by_id(vacation_id)
                old_vacation = vacation_search[0]

                # Create VacationModule object for the updated vacation                
                vacation = VacationModule(vacation_id=vacation_id, vacation_info=vacation_info, country_id=country_id,
                                           vacation_start=vacation_start, vacation_end=vacation_end,
                                           price=vacation_price, pic_name=pic_name)
                
                # Check if the old picture exists and no new picture is provided
                if old_vacation.pic_name and not vacation.pic_name:
                    print("Note: No new picture provided. The current picture has been deleted.")
                
               # Update the vacation
                self.bl.update_vacation(vacation)
                print("Vacation updated")
                return vacation

            elif role == "User":
                print("Wrong permission")

        except ValueError as ve:
            print("Error:", ve)
        except Exception as e:
            print("An unexpected error occurred:", e)
            raise

        
    def delete_vacation(self, vacation_id : int, email : str):
        """Method to delete a vacation""" 

        try:
            # Check user permission
            role = LoginFacade.check_permission(email)
            if role == "Admin":
                
            # Iterate through vacations to find the specified vacation
                vacations = self.bl.get_all_vacations()
                vacation_exists = False
                for vacation in vacations:
                    if vacation.vacation_id == vacation_id:
                        vacation_exists = True

                        # Delete the vacation
                        self.bl.delete_vacation_by_id(vacation_id)
                        print("vacation has been deleted!")
                        break
                
                # Raise error if the vacation does not exist
                if not vacation_exists:
                    raise ValueError("Vacation not found")
            elif role == "User":
                raise PermissionError("Users cannot delete vacations!")
        except (PermissionError, ValueError) as e:
            print(e)
                
        
    def show_all_vacations(self):
        
        vacations = self.bl.get_all_vacations()
        print("all the vacations:")
        for i in vacations:
            print(i)
            print("---------------------")        
           


    def insert_like(self, user_id : int, vacation_id : int):
        """Method to insert a like for a vacation"""
        try:
            # Check user permission
            role = LoginFacade.check_permission_id(user_id)            
            if role == "User":
                liked_vacations = self.bl.get_liked_vacations()
                like_exists = False
                
                # Iterate through liked vacations to check if the like already exists
                for liked_vacation in liked_vacations:
                    if liked_vacation.user_id == user_id and liked_vacation.vacation_id == vacation_id:
                        like_exists = True
                        break
                if like_exists:
                    print("Like already exists")

                # Add the like if it doesn't exist
                else:
                    self.bl.insert_liked_vacation(user_id=user_id, vacation_id=vacation_id)
                    print("Like has been added")
                
                return liked_vacations
            
            elif role == "Admin":
                print("Admins can't like vacations!")
        
        except Exception as e:
            print("An error occurred while inserting like:", e)
            raise


    def delete_like(self, user_id : int, vacation_id : int):
        """Method to delete a like for a vacation"""
        try:
            # Check user permission
            role = LoginFacade.check_permission_id(user_id)
            if role == "User":
                liked_vacations = self.bl.get_liked_vacations()
                like_found = False
                
                # Iterate through liked vacations to find the specified like               
                for liked_vacation in liked_vacations:
                    if liked_vacation.user_id == user_id and liked_vacation.vacation_id == vacation_id:
                        
                        # Delete the like
                        self.bl.delete_liked_vacation_by_id(user_id=user_id, vacation_id=vacation_id)
                        print("Like has been deleted")
                        like_found = True
                        break
                                    
                if not like_found:
                    print("Like does not exist")
                
                return liked_vacations
            
            elif role == "Admin":
                print("Admins can't like vacations!")
                
        except Exception as e:
            print("An error occurred while deleting like:", e)
            raise



