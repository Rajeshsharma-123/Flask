
import mysql.connector
import json
from flask import make_response,request
import jwt
import re
from functools import wraps
class auth_model():
    def __init__(self):
        try:
            self.con=mysql.connector.connect(host="localhost",user="root",password="Rsharma#123",database="flask_tutorail")
            self.con.autocommit=True
            self.cur=self.con.cursor(dictionary=True)
            print("Connection Successfull")
        except:
            print("some errors!")

    def token_auth(self, endpoint):
        def inner1(func):
            @wraps(func)
            def inner2(*args):
                authorization = request.headers.get("Authorization")
                if re.match("^Bearer *([^ ]+) *$", authorization, flags=0):
                    token = authorization.split(" ")[1]
                    try:
                        jwtdecoded = jwt.decode(token, "rajesh", algorithms= "HS256")
                    except jwt.ExpiredSignatureError:
                        return make_response({"ERROR" : "TOKEN EXPIRED"}, 401)
                    role_id = jwtdecoded['payload']['role_id']
                    self.cur.execute("SELECT roles FROM accesibility_view WHERE endpoint = %s", (endpoint,))
                    result = self.cur.fetchall()
                    if len(result) > 0:
                        allowed_roles = json.loads(result[0]['roles'])
                        if role_id in allowed_roles:
                            return func(*args)
                        else:
                            return make_response({"ERROR": "INVALID ROLE"}, 404)
                        
                    else:
                        return make_response({"ERROR": "UNKNOWN_ENDPOINT"}, 400)
                    return func(*args)
                else:
                    return make_response({"ERROR": "INVALID_TOKEN"}, 401)
                return func(*args)
            return inner2
        return inner1
