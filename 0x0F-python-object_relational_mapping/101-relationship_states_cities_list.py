#!/usr/bin/python3
"""
This module creates an SQLAlchemy engine,
gets all states and list all cities in each state
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
        stmt = (
            select(State)
            .order_by(State.id)
        )
        states = session.execute(stmt).scalars().all()
        for state in states:
            print(f"{state.id}: {state.name}")
            for city in state.cities:
                print(f"    {city.id}: {city.name}")
