#!/usr/bin/python3
'''script for task 8'''

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
import sys


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    host = 'localhost'
    port = '3306'

    engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.format(
                           username, password, host, port, db_name),
                           pool_pre_ping=True, poolclass=NullPool)
    Session = sessionmaker(bind=engine)
    local_session = Session()
    result = local_session.query(State).order_by(State.id).first()
    local_session.close()

    if result:
        print('{}: {}'.format(result.id, result.name))
    else:
        print('Nothing')
