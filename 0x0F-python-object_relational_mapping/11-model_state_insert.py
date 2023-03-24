#!/usr/bin/python3
"""
This module creates SQLAlchemy engine,
creates a new state and save it to database and print its id
"""
import sys
from model_state import Base, State
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
    with Session(engine) as session:
        new_state = State(name="Louisiana")
        session.add(new_state)
        session.commit()
        print(new_state.id)
