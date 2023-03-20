#!/usr/bin/python3
import sys
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import select, create_engine

if __name__ == "__main__":
    user, passwd, db = sys.argv[1:4]
    host = "localhost"
    engine = create_engine(
        "mysql+mysqldb://{}:{}@{}/{}".format(user, passwd, host, db),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)

    stmt = select(State.name)
    with Session(engine) as session:
        states = session.execute(stmt).all()
        for idx, state in enumerate(states, start=1):
            print(f"{idx}: {state[0]}")
