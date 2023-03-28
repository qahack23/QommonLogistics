from app import app, db
from sqlalchemy import create_engine
from pandas import read_csv
# from pdb import set_trace

# set_trace()

engine = create_engine('sqlite:///projectdb')

with app.app_context():
    db.create_all()
    with open("db/driver table.csv", "r") as data:
        table=read_csv(data)
        table.to_sql("driver", con=engine, if_exists='replace')

    with open("db/delivery table.csv", "r") as data:
        table=read_csv(data)
        table.to_sql("delivery", con=engine, if_exists='replace')