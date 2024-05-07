from modules.sql_table import SqlTable


class UserModule(SqlTable):
    def __init__(self, user_id : int, first_name : str, last_name : str, email : str, password : str, role_id : int):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.role_id = role_id

    
    @staticmethod
    def _dict_converter(dictionary : dict):
        user_id = dictionary["userId"]   
        first_name = dictionary["firstName"]
        last_name = dictionary["lastName"]
        email = dictionary["email"]
        password = dictionary["password"]
        role_id = dictionary["roleName"]
        user = UserModule(user_id, first_name, last_name, email, password, role_id)
        return user


    def __str__(self) -> str:
        return f"user ID: {self.user_id}, name: {self.first_name}, last name: {self.last_name}, email: {self.email}, password: {self.password}, role: {self.role_id}"


        
        