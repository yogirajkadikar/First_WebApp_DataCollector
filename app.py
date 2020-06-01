from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func

app = Flask(__name__)
# 'postgresql://postgres:yogikadikar@localhost/height_collector'
app.config['SQLALCHEMY_DATABASE_URI']='postgres://kuepnncviuqvjg:355d74c8eeb934f635443a23866cfd220cdfedb42d93a907665beae633cedc29@ec2-3-222-150-253.compute-1.amazonaws.com:5432/dej144uihuteba?sslnode=require'
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="data"
    id= db.Column(db.Integer, primary_key=True)
    email_ = db.Column(db.String(120), unique = True)
    height_ = db.Column(db.Integer)

    def __init__(self, email_,height_):
        self.email_ = email_
        self.height_ = height_


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods = ['POST'])
def success():
    if request.method == 'POST':
        email = request.form["email_name"]
        height = request.form["height_name"]
        if db.session.query(Data).filter(Data.email_==email).count() == 0:
            data=Data(email,height)
            db.session.add(data)
            db.session.commit()
            average_height = db.session.query(func.avg(Data.height_)).scalar()
            average_height=round(average_height)
            count = db.session.query(Data.height_).count()
            send_email(email, height, average_height,count)
            return render_template("success.html")
    return render_template("index.html",  text="Seems like some data is already logged in using that email address. <br>Please try another!")
   
if __name__ == "__main__":
    app.debug = True
    app.run()