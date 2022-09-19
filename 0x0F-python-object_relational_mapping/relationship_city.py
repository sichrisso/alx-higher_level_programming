#!/usr/bin/python3
'''task 15 model script'''

from sqlalchemy.orm import relationship
from relationship_state import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    '''City model for my db'''
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False,
                autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
