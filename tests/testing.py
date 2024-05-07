from src.login_facade import LoginFacade
from src.vacation_facade import VacationFacade

class Test:

    def test_validate_email():
        LoginFacade().validate_email("baalzedaka@gmail.com")
        print("---------------------------------------------------------------")


    def test_validate_password():
        LoginFacade().validate_password("1234")
        print("---------------------------------------------------------------") 


    def test_log_in():
        LoginFacade().log_in(True, True)
        print("---------------------------------------------------------------") 
    
    def test_check_user_exists():
        LoginFacade.check_user_exist("baalzedaka@gmail.com")
        print("---------------------------------------------------------------") 


    def test_register():
        test_email="baalz@gmail.com"
        test_password="12345"
        user_name="nitz"
        userlast_name="bz"
        LoginFacade.register(u_email=test_email, u_password=test_password ,valid_email=LoginFacade.validate_email(test_email), valid_pass=LoginFacade.validate_password(test_password), u_first_name=user_name, u_last_name=userlast_name, user_exists=LoginFacade.check_user_exist(test_email))


    def test_check_permission():
        LoginFacade.check_permission('nitzadmin@gmail.com')
        print("---------------------------------------------------------------") 


    def test_check_permission_id():
        LoginFacade.check_permission_id(2)
        print("---------------------------------------------------------------") 



    def test_create_vacation():

        VacationFacade().create_vacation(vacation_info="test info", country_id=58, vacation_start="2025-1-1",vacation_end="2025-1-5",vacation_price=100,pic_name="testpic",email="nitzadmin@gmail.com")    
        print("---------------------------------------------------------------") 
    

    def test_update_existing_vacation():

        VacationFacade().update_existing_vacation(vacation_id=2,vacation_info="update",country_id=83,vacation_start="2024-8-8",vacation_end="2024-8-12",vacation_price=99,pic_name=None,email="nitzadmin@gmail.com")
        print("---------------------------------------------------------------") 
    
    
    def test_delete_vacation():

        VacationFacade().delete_vacation(vacation_id=3,email="nitzadmin@gmail.com")
        print("---------------------------------------------------------------") 
    

    def test_insert_like():
        
        VacationFacade().insert_like(user_id=1,vacation_id=4)
        VacationFacade().insert_like(user_id=1,vacation_id=5)
        print("---------------------------------------------------------------") 
    

    def test_delete_like():
        
        VacationFacade().delete_like(user_id=1,vacation_id=4)
        print("---------------------------------------------------------------") 

    def test_show_all_vacations():
        VacationFacade().show_all_vacations()

def test_all():
    Test.test_show_all_vacations()
    Test.test_validate_email()
    Test.test_validate_password()
    Test.test_log_in()
    Test.test_check_user_exists()
    Test.test_register()
    Test.test_check_permission()
    Test.test_check_permission_id()
    Test.test_create_vacation()
    Test.test_update_existing_vacation()
    Test.test_delete_vacation()
    Test.test_insert_like()
    Test.test_delete_like()
            

