import mysql.connector
import json
from flask import make_response
from datetime import datetime,timedelta
import jwt
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
            res = make_response({"payload":result},200)
            res.headers['Access-Control-Allow-Origin'] = "*"
            return res
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
       

    def user_patch_model(self, data, idusers):
        qry = "UPDATE users SET "
        for key in data:
           qry += f"{key}='{data[key]}',"
        
        qry = qry[:-1] + f" WHERE idusers={idusers}"

        self.cur.execute(qry)

        if self.cur.rowcount>0:
            return make_response({"message":"User Updated Successfully"},201)
        else:
            return make_response({"message":"Nothing to Update"},202)

        # UPDATE users SET col=  val, col=val WHERE id={id}

    def user_pagination_model(self, limit, page):
         limit  = int(limit)
         page = int(page)
         start = (page * limit) - limit
         qry = f"SELECT * FROM users LIMIT {start}, {limit}"
         self.cur.execute(qry)
         result=self.cur.fetchall()
         if len(result)>0:
            res = make_response({"payload":result, "page_no":page, "limit": limit} ,200)
            
            return res
          
         else:
            return make_response({"message":"No Data found"},204)
        
        
    def user_upload_avatar_model(self, uid, filepath):
        self.cur.execute("UPDATE users SET avatar=%s WHERE idusers=%s",(filepath, uid))
        if self.cur.rowcount>0:
            return make_response({"message":"FILE UPLOADED Successfully"},201)
        else:
            return make_response({"message":"Nothing to Update"},202)
                 
    def user_login_model(self, data):
        self.cur.execute(f"SELECT idusers, name, email, phone, avatar, role_id FROM users WHERE email='{data['email']}' and password='{data['password']}'")
        result = self.cur.fetchall()
        userdata = result[0]
        exp_time = datetime.now() + timedelta(minutes=15)
        exp_epoch_time = int(exp_time.timestamp())
        payload = {
            "payload" : userdata,
            "exp": exp_epoch_time
        }
        jwtoken = jwt.encode(payload, "rajesh", algorithm="HS256")
        return make_response({"token":jwtoken}, 200)



    
                                
       
  
    