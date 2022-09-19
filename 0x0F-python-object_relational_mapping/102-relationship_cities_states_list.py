#!/usr/bin/python3
'''script for task 17'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City
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
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    loc_session = Session()
    cities = loc_session.query(City).order_by(City.id.asc()).all()

    for city in cities:
        print('{}: {} -> {}'.format(city.id, city.name, city.state.name))

    loc_session.close()
    engine.dispose()
