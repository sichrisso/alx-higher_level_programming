#!/usr/bin/python3
'''script for task 1'''

import MySQLdb
import sys


def list_N():
    '''lists all states with a name that starts with N'''
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    host = 'localhost'
    port = 3306

    db = MySQLdb.connect(host=host, user=username, passwd=password,
                         db=db_name, port=port)
    cur = db.cursor()
    cur.execute('SELECT * FROM states WHERE name regexp "^N.*" ' +
                'ORDER BY states.id ASC')
    result = cur.fetchall()
    cur.close()
    db.close()
    if result:
        for row in result:
            if row[1][0] == "N":
                print(row)


if __name__ == "__main__":
    list_N()
