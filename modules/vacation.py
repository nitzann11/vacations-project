from datetime import date
from modules.sql_table import SqlTable


class VacationModule(SqlTable):
    
    def __init__(self, vacation_id : int, vacation_info : str, country_id : int, vacation_start : date, vacation_end : date, price : int, pic_name : str):
        self.vacation_id = vacation_id
        self.vacation_info = vacation_info
        self.country_id = country_id
        self.vacation_start = vacation_start
        self.vacation_end = vacation_end
        self.price = price
        self.pic_name = pic_name


    @staticmethod
    def _dict_converter(dictionary : dict):
        vacation_id = dictionary["vacationId"]
        vacation_info = dictionary["vacationInfo"]
        country_id = dictionary["countryName"]
        vacation_start = dictionary["vacationStart"]
        vacation_end = dictionary["vacationEnd"]
        price = dictionary["price"]
        pic_name = dictionary["picName"]
        vacation = VacationModule(vacation_id, vacation_info, country_id, vacation_start, vacation_end, price, pic_name)
        return vacation


    def __str__(self) -> str:
        return f"vacation ID: {self.vacation_id}, info: {self.vacation_info}, country id: {self.country_id}, vacation start: {self.vacation_start}, vacation end: {self.vacation_end}, price: {self.price}$, pic: {self.pic_name}.png"    
