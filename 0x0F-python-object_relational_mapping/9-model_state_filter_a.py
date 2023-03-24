#!/usr/bin/python3
"""
This module creates SQLAlchemy engine,
fetches all object that contains "a" in the name
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import select, create_engine, asc

if __name__ == "__main__":
    user, passwd, db = sys.argv[1:4]
    host = "localhost"
    engine = create_engine(
        "mysql+mysqldb://{}:{}@{}/{}".format(user, passwd, host, db),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)

    stmt = (
        select(State.id, State.name)
        .filter(State.name.like("%a%"))
        .order_by(asc(State.id))
    )
    with Session(engine) as session:
        states = session.execute(stmt).all()
        for state in states:
            print("{}: {}".format(*state))
