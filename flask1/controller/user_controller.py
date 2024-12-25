from app import app
from model.user_model import user_modal
obj = user_modal()
@app.route("/user/signup")
def user_signup_controller():
    return obj.user_signup_model()