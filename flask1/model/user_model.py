import mysql.connector
import json
from flask import make_response
class user_modal():
    def __init__(self):
        try:
            self.con=mysql.connector.connect(host="localhost",user="root",password="Rsharma#123",database="flask_tutorail")
            self.con.autocommit=True
            self.cur=self.con.cursor(dictionary=True)
            print("Connection Successfull")
        except:
            print("some errors!")
         
        
        
    
    
    def user_getall_model(self):
        
        self.cur.execute("SELECT * FROM users ")
        result=self.cur.fetchall()
        if len(result)>0:
            return make_response({"payload":result},200)
            # return json.dumps(result)
        else:
            return make_response({"message":"No Data found"},204)
        
    def user_addone_model(self, data):
        
        self.cur.execute(f"INSERT INTO users(name, email, phone, role, password) VALUES('{data['name']}', '{data['email']}', '{data['phone']}', '{data['role']}', '{data['password']}')")
        return make_response({"message":"User Created Successfully"},201)                             
       
    def user_update_model(self, data):
        self.cur.execute(f"UPDATE users SET name='{data['name']}', email='{data['email']}' , phone='{data['phone']}' , role='{data['role']}', password='{data['password']}' WHERE idusers={data['idusers']} ")
        if self.cur.rowcount>0:
            return make_response({"message":"User Updated Successfully"},201)
        else:
            return make_response({"message":"Nothing to Update"},202)                            
       
        
    def user_delete_model(self, idusers):
        self.cur.execute(f"DELETE FROM users WHERE idusers={idusers} ")
        if self.cur.rowcount>0:
            return make_response({"message":"User Deleted Successfully"},200)
        else:
            return make_response({"message":"Nothing to Delete"},202)                            
       
        