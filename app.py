from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///projectdb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class driver(db.Model):
    DriverID = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(50))
    LastName = db.Column(db.String(50))
    Deliveries = db.relationship("delivery", backref="driver")

    def toDict(self):
        return {
            "first": self.FirstName,
            "last": self.LastName
        }
    

class delivery(db.Model):
    DeliveryID = db.Column(db.Integer, primary_key=True)
    Address = db.Column(db.String(255))
    CompanyName = db.Column(db.String(255))
    ContactName = db.Column(db.String(255))
    DriverID = db.Column(db.Integer, db.ForeignKey('driver.DriverID'))


@app.route('/')
def index():
    unassigned=delivery.query.filter_by(DriverID=None).all()
    assigned = [d for d in delivery.query.all() if d not in unassigned]
    return render_template('layout.html', unassigned=unassigned, assigned=assigned)

@app.route('/test')
def test():
    return list(d.toDict() for d in driver.query.all())

if __name__ == "__main__":
    #db.create_all()
    app.run(debug=True)