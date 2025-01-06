from app import app
from model.user_model import user_modal
from model.auth_model import auth_model
from flask import request, send_file
from datetime import datetime
obj = user_modal()
auth = auth_model()

@app.route("/user/getall", methods=["GET"])
@auth.token_auth()
def user_getall_controller():
    return obj.user_getall_model()

@app.route("/user/addone", methods=["GET"])
@auth.token_auth()
def user_addone_controller():
    return obj.user_addone_model(request.form)

@app.route("/user/addmultiple", methods=["POST"])
def user_add_multiple_controller():
    return obj.user_add_multiple_model(request.json)
    
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

@app.route("/user/<uid>/upload/avatar", methods=["PUT"])
def user_upload_avatar_controller(uid):
    file = request.files['avatar']
    
    uniqueFileName = str(datetime.now().timestamp()).replace(".", "") 
    fileNameSplit = file.filename.split(".")
    ext = fileNameSplit[len(fileNameSplit)-1]
    finalFilePath = f"uploads/{uniqueFileName}.{ext}"
    file.save(finalFilePath)
    return obj.user_upload_avatar_model(uid, finalFilePath) 


@app.route("/uploads/<filename>")
def user_getavatar_controller(filename):
    return send_file(f"uploads/{filename}")

@app.route("/user/login", methods=["POST"])
def user_login_controller():
    # request.f
    return obj.user_login_model(request.form)