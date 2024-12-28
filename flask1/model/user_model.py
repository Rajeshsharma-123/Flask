import mysql.connector
import json
from flask import jsonify
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
            return {"payload":result}
            # return json.dumps(result)
        else:
            return {"message":"No Data found"}
        
    def user_addone_model(self, data):
        
        self.cur.execute(f"INSERT INTO users(name, email, phone, role, password) VALUES('{data['name']}', '{data['email']}', '{data['phone']}', '{data['role']}', '{data['password']}')")
        return jsonify({"message":"User Created Successfully"}), 201                             
       
    def user_update_model(self, data):
        self.cur.execute(f"UPDATE users SET name='{data['name']}', email='{data['email']}' , phone='{data['phone']}' , role='{data['role']}', password='{data['password']}' WHERE idusers={data['idusers']} ")
        if self.cur.rowcount>0:
            return {"message":"User Updated Successfully"}
        else:
            return {"message":"Nothing to Update"}                            
       
        
    def user_delete_model(self, idusers):
        self.cur.execute(f"DELETE FROM users WHERE idusers={idusers} ")
        if self.cur.rowcount>0:
            return {"message":"User Deleted Successfully"}
        else:
            return {"message":"Nothing to Delete"}                            
       
        