#!/usr/bin/python3
"""
This module creates SQLAlchemy engine,
fetches all cities from db
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine, text, select
from sqlalchemy.orm import Session

if __name__ == "__main__":
    user, passwd, db = sys.argv[1:4]
    host = "localhost"
    port = 3306
    engine = create_engine(
        "mysql+mysqldb://{}:{}@{}:{}/{}".format(
            user, passwd, host, port, db
        ),
        pool_pre_ping=True,
    )
    stmt = select(State.name, City.id, City.name).join(City)
    with Session(engine) as session:
        cities = session.execute(stmt).all()
        for city in cities:
            print("{}: ({}) {}".format(*city))
