from app import app
from model.user_model import user_modal
from flask import request
obj = user_modal()

@app.route("/user/getall", methods=["GET"])
def user_getall_controller():
    return obj.user_getall_model()

@app.route("/user/addone", methods=["GET"])
def user_addone_controller():
    return obj.user_addone_model(request.form)
    
@app.route("/user/update", methods=["PUT"])
def user_update_controller():
    return obj.user_update_model(request.form)
    
@app.route("/user/delete/<idusers>", methods=["DELETE"])
def user_delete_controller(idusers):
    return obj.user_delete_model(idusers)
    
@app.route("/user/patch/<idusers>", methods=["PATCH"])
def user_patch_controller(idusers):
    return obj.user_patch_model(request.form, idusers)
    
@app.route("/user/getall/limit/<limit>/page/<page>", methods=["GET"])
def user_pagination_controller(limit, page):
    return obj.user_pagination_model(limit, page)
    