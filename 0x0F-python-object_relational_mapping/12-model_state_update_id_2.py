#!/usr/bin/python3
'''script for task 12'''

from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    host = 'localhost'
    port = '3306'

    engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.format(
                           username, password, host, port, db_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    local_session = Session()
    state = local_session.query(State).filter(State.id == 2).first()
    state.name = 'New Mexico'
    local_session.commit()

    local_session.close()
    engine.dispose()
