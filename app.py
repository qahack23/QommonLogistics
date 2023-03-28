from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///projectdb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class driver(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first = db.Column(db.String(50))
    last = db.Column(db.String(50))
    

class delivery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    companyname = db.Column(db.String(255))
    address = db.Column(db.String(255))
    driverid = db.Column(db.Integer, db.ForeignKey('driver.id'))


@app.route('/')
def index():
    return render_template('layout.html')

if __name__ == "__main__":
    #db.create_all()
    app.run(debug=True)