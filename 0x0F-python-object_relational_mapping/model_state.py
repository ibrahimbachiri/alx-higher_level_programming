#!/usr/bin/python3
"""
Contains the class definition of a State and an instance Base = declarative_base()
"""

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# Create an instance of the declarative base
Base = declarative_base()

class State(Base):
    """
    Class definition of a State
    """
    __tablename__ = 'states'

    # Class attribute id representing a column of an auto-generated, unique integer, can't be null, and is a primary key
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    # Class attribute name representing a column of a string with a maximum of 128 characters, can't be null
    name = Column(String(128), nullable=False)
