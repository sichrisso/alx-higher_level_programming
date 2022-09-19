#!/usr/bin/python3
'''script for task 14'''

from model_state import State, Base
from model_city import City
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
                           username, password, host, port, db_name
                           ), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    local_session = Session()
    result = local_session.query(City, State).filter(
                           City.state_id == State.id
                           ).order_by(City.id).all()

    for row in result:
        print('{}: ({}) {}'.format(row[1].name, row[0].id, row[0].name))

    local_session.close()
    engine.dispose()
