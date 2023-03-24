#!/usr/bin/python3
"""
This module creates SQLAlchemy engine,
fetches all object with name passed as argument and prints its id
or Not found when object doesn't exist
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, text, select
from sqlalchemy.orm import Session

if __name__ == "__main__":
    user, passwd, db, state_name = sys.argv[1:5]
    host = "localhost"
    port = 3306
    engine = create_engine(
        "mysql+mysqldb://{}:{}@{}:{}/{}".format(
            user, passwd, host, port, db
        ),
        pool_pre_ping=True,
    )
    stmt = select(State.id).where(State.name == str(text(state_name)))
    with Session(engine) as session:
        state = session.execute(stmt).one_or_none()
        if state is None:
            print("Not found")
        else:
            print(*state)
