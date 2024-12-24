#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa"""


from model_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine



if __name__ == "__main__":
    connection = f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    eng = create_engine(connection)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State)

    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))