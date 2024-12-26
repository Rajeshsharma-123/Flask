from app import app
from model.user_model import user_modal
obj = user_modal()
@app.route("/user/getall")
def user_getall_controller():
    return obj.user_getall_model()