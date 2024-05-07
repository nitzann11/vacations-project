
from dal.dal_file import DAL
from modules.user import UserModule
from modules.vacation import VacationModule
from modules.like import LikeModule

class Bl:
    def __init__(self):
        self.dal=DAL()

    def insert_user(self, user : object):
        """Method to insert a new user into the database"""
        try:
            sql="INSERT INTO project1.users (userId , firstName , lastName , email , password , roleId) VALUES(%s,%s,%s,%s,%s,%s);"
            result=self.dal.insert(sql,(user.user_id, user.first_name, user.last_name, user.email, user.password, user.role_id))
            return result
        except Exception as e:
            print(f"An error occurred while inserting user: {e}")
           
    
    def get_user_by_credentials(self,email : str ,password :str ):
        """Method to fetch a user by email and password"""
        try:
            sql="SELECT u.userId, u.firstName, u.lastName, u.email, u.password,r.roleName FROM project1.users AS u INNER JOIN project1.roles AS r ON u.roleId = r.roleId WHERE email = %s AND password = %s;"
            result=self.dal.get_table(sql,(email,password))
            class_result=UserModule.dicts_converter(UserModule, result)
            return class_result
        except Exception as e:
            print(f"An error occurred while fetching user by credentials: {e}")
    
    def get_vacation_by_id(self, vacation_id : int):
        """Method to fetch a vacation by its ID"""
        try:
            sql="SELECT v.vacationId, v.vacationInfo, c.countryName, v.vacationStart, v.vacationEnd, v.price, v.picName FROM project1.vacations AS v INNER JOIN project1.countries AS c ON v.countryId = c.countryId WHERE vacationId = %s LIMIT 1;"
            result=self.dal.get_table(sql,(vacation_id,))
            class_result= VacationModule.dicts_converter(VacationModule, result)
            return class_result
        except Exception as e:
            print(f"An error occurred while fetching vacation by ID: {e}")
    
    
    
    def get_all_vacations(self):
        """Method to fetch all vacations from the database"""
        try:
            sql="SELECT v.vacationId, v.vacationInfo, c.countryName, v.vacationStart, v.vacationEnd, v.price, v.picName FROM project1.vacations AS v INNER JOIN project1.countries AS c ON v.countryId = c.countryId ORDER BY vacationStart ASC;"
            result=self.dal.get_table(sql)
            class_result= VacationModule.dicts_converter(VacationModule, result)
            return class_result
        except Exception as e:
            print("An error occurred while retrieving all vacations:", e)
    
    
    def get_all_users(self):
        """Method to fetch all users from the database"""
        try:
            sql="SELECT u.userId, u.firstName, u.lastName, u.email, u.password,r.roleName FROM project1.users AS u INNER JOIN project1.roles AS r ON u.roleId = r.roleId;"
            result=self.dal.get_table(sql,)
            class_result= UserModule.dicts_converter(UserModule, result)
            return class_result
        except Exception as e:
            print("An error occurred while retrieving all users:", e)
    
    def insert_vacation(self, vacation : object):
        """Method to insert a new vacation into the database"""
        try:
            sql="INSERT INTO project1.vacations (vacationId, vacationInfo, countryId, vacationStart, vacationEnd, price, picName) VALUES(%s,%s,%s,%s,%s,%s,%s);"
            result=self.dal.insert(sql,(vacation.vacation_id, vacation.vacation_info, vacation.country_id, vacation.vacation_start, vacation.vacation_end, vacation.price, vacation.pic_name))
            return result
        except Exception as e:
            print("An error occurred while inserting vacation:", e)
    
    def update_vacation(self, vacation : object):
        """Method to update an existing vacation in the database"""
        try:
            sql="UPDATE project1.vacations SET vacationInfo = %s,  countryId = %s ,  vacationStart = %s,  vacationEnd = %s , price = %s ,  picName = %s WHERE vacationId = %s;"
            result=self.dal.update(sql,(vacation.vacation_info, vacation.country_id, vacation.vacation_start, vacation.vacation_end, vacation.price, vacation.pic_name, vacation.vacation_id))
            return result
        except Exception as e:
            print("An error occurred while updating vacation:", e)

    def delete_vacation_by_id(self, vacation_id : int):
        """Method to delete a vacation by its ID from the database"""
        try:
            sql="DELETE FROM project1.vacations WHERE vacationId = %s;"
            result=self.dal.delete(sql,(vacation_id,))
            return result
        except Exception as e:
            print("An error occurred while deleting vacation by ID:", e)


    def get_liked_vacations(self):
        """Method to fetch all liked vacations from the database"""
        try:
            sql="SELECT * FROM project1.likes;"
            result=self.dal.get_table(sql,)
            class_result=LikeModule.dicts_converter(LikeModule, result)
            return class_result
        except Exception as e:
            print("An error occurred while getting liked vacations:", e)
    

    def insert_liked_vacation(self, user_id : int, vacation_id : int):
        """Method to insert a new liked vacation into the database"""
        try:
            sql="INSERT INTO project1.likes (userId,vacationId) VALUES(%s,%s);"
            result=self.dal.insert(sql,(user_id, vacation_id))
            return result
        except Exception as e:
            print("An error occurred while inserting liked vacation:", e)

    def delete_liked_vacation_by_id(self, user_id : int, vacation_id : int):
        """Method to delete a liked vacation by user ID and vacation ID from the database"""
        try:
            sql="DELETE FROM project1.likes WHERE userId=%s AND vacationId=%s;"
            result=self.dal.delete(sql,(user_id, vacation_id))
            return result
        except Exception as e:
            print("An error occurred while deleting liked vacation:", e)
    



    

                                   

    

    
