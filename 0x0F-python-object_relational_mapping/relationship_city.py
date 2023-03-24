#!/usr/bin/python3
"""
This module defines the model for a City.
It is the def of a SQL table in ORM
"""

from relationship_state import Base
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """
    This class defines an SQLAlchemy table City
    Has id and name column
    """
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
