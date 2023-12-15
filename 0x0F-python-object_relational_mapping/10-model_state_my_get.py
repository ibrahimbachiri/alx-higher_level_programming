#!/usr/bin/python3
"""
Script that prints the State object with the name passed as an argument
from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
import sys

if __name__ == "__main__":
    # Create the SQLAlchemy engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a configured "Session" class
    Session = Session(bind=engine)

    # Create a Session
    session = Session()

    # Query the State with the given name
    state_name = sys.argv[4]
    result = session.query(State).filter_by(name=state_name).first()

    # Print the result or "Not found" if no state is found
    if result:
        print(result.id)
    else:
        print("Not found")

    # Close the session
    session.close()
