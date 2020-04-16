from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app2 = Flask(__name__)
app2.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:yogikadikar@localhost/height_collector'
db=SQLAlchemy(app2)

class data(db.Model):
    __tablename__="data"
    id= db.Column(db.Integer, primary_key=True)
    email_ = db.Column(db.String(120), unique = True)
    height_ = db.Column(db.Integer)

    def __init__(self, email_,height_):
        self.email_ = email_
        self.height_ = height_


@app2.route("/")
def index():
    return render_template("index.html")

@app2.route("/success", methods = ['POST'])
def success():
    if request.method == 'POST':
        email = request.form["email_name"]
        height = request.form["height_name"]
        return render_template("success.html")

if __name__ == "__main__":
    app2.debug = True
    app2.run()