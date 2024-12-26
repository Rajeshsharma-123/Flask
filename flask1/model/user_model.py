import mysql.connector
import json
class user_modal():
    def __init__(self):
        try:
            self.con=mysql.connector.connect(host="localhost",user="root",password="Rsharma#123",database="flask_tutorail")
            self.cur=self.con.cursor(dictionary=True)
            print("Connection Successfull")
        except:
            print("some errors!")
         
        
        
    
    
    def user_getall_model(self):
        
        self.cur.execute("SELECT * FROM users ")
        result=self.cur.fetchall()
        if len(result)>0:
            return json.dumps(result)
        else:
            return "No Data found"
        
        