#!/usr/bin/python3
'''task 14 model script'''

from model_state import Base
from sqlalchemy import Column, String, Integer, ForeignKey


class City(Base):
    '''City model for my db'''
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False,
                autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
