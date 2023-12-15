#!/usr/bin/python3
"""Script to create a State with a City using SQLAlchemy"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City

if __name__ == "__main__":
    # Setup connection to the database
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, database),
                           pool_pre_ping=True)

    # Create all tables in the engine
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Create the State "California" with the City "San Francisco"
    new_state = State(name="California", cities=[City(name="San Francisco")])

    # Add the new state to the session
    session.add(new_state)

    # Commit the changes
    session.commit()

    # Close the session
    session.close()
