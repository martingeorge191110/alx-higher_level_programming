#!/usr/bin/python3
"""script that prints all City objects from the database hbtn_0e_14_usatou"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
        )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    newState = State(name='California')
    newCity = City(name='San Francisco')
    newState.cities.append(newCity)

    session.add(newState)
    session.add(newCity)
    session.commit()
