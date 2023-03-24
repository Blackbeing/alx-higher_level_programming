#!/usr/bin/python3
"""
This module creates and SQLAlchemy engine,
fetches states from specified database and prints them
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

    stmt = select(State.id, State.name).order_by(asc(State.id))
    with Session(engine) as session:
        states = session.execute(stmt).all()
        for state in states:
            print(f"{state[0]}: {state[1]}")
