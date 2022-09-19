#!/usr/bin/python3
''' script for task 2
    script should take 4 arguments: mysql username,
    mysql password, database name and state name searched
'''

import MySQLdb
import sys


def list_with_name():
    ''' displays all values in the states table in hbtn db where name
        matches the argument passed to the script
    '''
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    host = 'localhost'
    port = 3306

    db = MySQLdb.connect(host=host, user=username, passwd=password,
                         db=db_name, port=port)
    cur = db.cursor()
    cur.execute(('SELECT * FROM states WHERE BINARY name = \'{}\'\
                 ORDER BY id ASC;').format(state_name))
    result = cur.fetchall()
    cur.close()
    db.close()

    if result:
        for row in result:
            print(row)


if __name__ == '__main__':
    list_with_name()
