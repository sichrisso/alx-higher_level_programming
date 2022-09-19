#!/usr/bin/python3
'''task 4 script'''

import MySQLdb
import sys


def list_all():
    '''lists all cities from db'''
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    host = 'localhost'
    port = 3306

    db = MySQLdb.connect(host=host, user=username, passwd=password,
                         db=db_name, port=port)
    cur = db.cursor()
    cur.execute('SELECT c.id, c.name, s.name FROM cities c LEFT ' +
                'JOIN states s ON c.state_id = s.id ORDER BY c.id ASC;')
    result = cur.fetchall()
    cur.close()
    db.close()

    if result:
        for row in result:
            print(row)


if __name__ == '__main__':
    list_all()
