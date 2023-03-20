#!/usr/bin/python3
"""
This module defines the model for a State.
It is the def of a SQL table in ORM
"""

from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, Column, Integer, String

Base = declarative_base()


class State(Base):
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
