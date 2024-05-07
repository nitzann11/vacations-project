from modules.sql_table import SqlTable


class LikeModule(SqlTable):

    def __init__(self, user_id : int, vacation_id : int):
        self.user_id = user_id
        self.vacation_id = vacation_id


    @staticmethod
    def _dict_converter(dictionary : dict):
        user_id = dictionary["userId"]   
        vacation_id = dictionary["vacationId"]
        like = LikeModule(user_id, vacation_id)
        return like


    def __str__(self) -> str:
        return f"user ID: {self.user_id}, Vacation ID: {self.vacation_id}"
    