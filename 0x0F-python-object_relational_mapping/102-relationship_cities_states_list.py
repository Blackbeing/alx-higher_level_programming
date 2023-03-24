#!/usr/bin/python3
"""
This module creates an SQLAlchemy engine,
list all city objects from database
"""
import sys
from relationship_state import State, Base
from relationship_city import City
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select


if __name__ == "__main__":
    user, passwd, db = sys.argv[1:4]
    host = "localhost"
    engine = create_engine(
        "mysql+mysqldb://{}:{}@{}/{}".format(user, passwd, host, db),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        stmt = select(City, State).join(State).order_by(City.id)
        cities = session.execute(stmt).all()
        for city, state in cities:
            print(f"{city.id}: {city.name} -> {state.name}")
