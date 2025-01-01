#!/usr/bin/python3
"""City class"""

from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """class City (cities table)"""

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
