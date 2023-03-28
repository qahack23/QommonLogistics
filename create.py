from app import app, db
from sqlalchemy import create_engine
from pandas import read_csv
# from os import getenv
# from pdb import set_trace

# user = getenv('user')
# password = getenv('password')

# set_trace()

engine = create_engine('sqlite:///projectdb')
# f"mysql+pymysql://{user}:{password}@server:3306/database"

with app.app_context():
    db.create_all()
    with open("db/driver table.csv", "r") as data:
        table=read_csv(data)
        table.to_sql("driver", con=engine, if_exists='replace')

    with open("db/delivery table.csv", "r") as data:
        table=read_csv(data)
        table.to_sql("delivery", con=engine, if_exists='replace')