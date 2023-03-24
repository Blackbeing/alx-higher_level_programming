#!/usr/bin/python3
"""
This module creates SQLAlchemy engine,
creates city and state objects and stores them in database
"""
import sys
from relationship_state import State, Base
from relationship_city import City
from sqlalchemy.orm import Session, relationship
from sqlalchemy import select, create_engine, asc

if __name__ == "__main__":
    user, passwd, db = sys.argv[1:4]
    host = "localhost"
    engine = create_engine(
        "mysql+mysqldb://{}:{}@{}/{}".format(user, passwd, host, db),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        state = State(name="California")
        city = City(name="San Francisco")
        state.cities.append(city)

        session.add(state)
        session.commit()
