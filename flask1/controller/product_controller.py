from app import app
@app.route("/about/address")
def address():
    return "this is address department"