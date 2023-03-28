from flask import Flask, render_template, url_for, request, redirect
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


@app.before_first_request
def reset():
    for deliv in delivery.query.all():
        deliv.DriverID = None
        db.session.commit()

@app.route('/', methods=['GET', 'POST'])
def index():
    unassigned = delivery.query.filter_by(DriverID=None).all()
    assigned = [d for d in delivery.query.all() if d not in unassigned]
    drivers = driver.query.all()
    if request.method == 'POST':
        delivery_to_assign = delivery.query.get(request.form['del_id'])
        delivery_to_assign.DriverID = request.form['driver-list']
        db.session.commit()
        return redirect(url_for('bounce'))
    return render_template('layout.html', unassigned=unassigned, assigned=assigned, drivers=drivers)

@app.route('/bounce')
def bounce():
    return redirect(url_for('index'))

if __name__ == "__main__":
    #db.create_all()
    app.run(debug=True)