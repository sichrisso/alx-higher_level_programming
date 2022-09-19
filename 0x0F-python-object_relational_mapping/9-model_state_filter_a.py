#!/usr/bin/python3
'''script for task 9'''

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
    a_states = local_session.query(State).filter(
               State.name.op('regexp')('.*a+.*')
               ).order_by(State.id)
    local_session.close()
    engine.dispose()

    if a_states:
        for state in a_states:
            print('{}: {}'.format(state.id, state.name))
