#!/usr/bin/python3
'''script for task 3'''

import MySQLdb
import sys


def secure_fetch():
    ''' a safer way to displays all values in the states table of hbtn_0e_0_usa
        where name matches the argument passed to the script
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
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC;",
                [state_name])

    result = cur.fetchall()
    cur.close()
    db.close()

    if result:
        for row in result:
            print(row)


if __name__ == '__main__':
    secure_fetch()
