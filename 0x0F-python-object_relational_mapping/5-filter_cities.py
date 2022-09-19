#!/usr/bin/python3
'''script for task 5'''

import MySQLdb
import sys


def list_by_state():
    '''lists all cities of a state passed as argument to the script'''
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    host = 'localhost'
    port = 3306

    db = MySQLdb.connect(host=host, user=username, passwd=password,
                         db=db_name, port=port)
    cur = db.cursor()
    cur.execute('SELECT c.name FROM cities c INNER JOIN states s ' +
                'ON s.id = c.state_id WHERE ' +
                'BINARY s.name = %s ' +
                'ORDER BY c.id ASC;', [state_name])
    result = cur.fetchall()
    cur.close()
    db.close()

    print(', '.join(map(lambda x: x[0], result)))


if __name__ == '__main__':
    list_by_state()
