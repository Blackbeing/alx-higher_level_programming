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

    stmt = select(State.id, State.name).order_by(State.id)
    with Session(engine) as session:
        state = session.execute(stmt).first()
        if state is None:
            print("Nothing")
        else:
            print(f"{state[0]}: {state[1]}")
