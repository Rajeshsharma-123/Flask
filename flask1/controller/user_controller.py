from app import app
from model.user_model import user_modal
from flask import request
obj = user_modal()

@app.route("/user/getall")
def user_getall_controller():
    return obj.user_getall_model()

@app.route("/user/addone")
def user_addone_controller():
    return obj.user_addone_model(request.form)
    
@app.route("/user/update", methods=["PUT"])
def user_update_controller():
    return obj.user_update_model(request.form)
    