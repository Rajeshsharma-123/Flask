import mysql.connector
class user_modal():
    def __init__(self):
        try:
            con=mysql.connector.connect(host="localhost",user="root",password="Rsharma#123",database="flask_tutorail")
            print("Connection Successfull")
        except:
            print("some errors!")
         
        
        
    
    
    def user_getall_model(self):
        
        #Query execution code
        return "This is user_signup_model"