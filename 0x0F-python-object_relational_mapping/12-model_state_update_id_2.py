#!/usr/bin/python3
"""
This module creates SQLAlchemy engine,
update object that has id=2 to New Mexico
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
        select(State)
        .filter_by(id=2)
    )
    with Session(engine) as session:
        state = session.execute(stmt).scalar_one()
        state.name = "New Mexico"
        session.commit()
