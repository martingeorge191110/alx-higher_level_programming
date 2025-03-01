#!/usr/bin/python3
"""script that prints all City objects from the database hbtn_0e_14_usatou"""

import sys
from model_city import Base, City
from model_state import State
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

    data = session.query(City, State) \
                  .filter((City.state_id == State.id)) \
                  .order_by(City.id).all()

    for city, state in data:
        print(f"{state.name}: ({city.id}) {city.name}")
