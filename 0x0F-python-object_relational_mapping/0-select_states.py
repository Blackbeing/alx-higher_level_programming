#!/usr/bin/python3
"""
This module provides script to connect to Mysql database and execute SQL
statements.
It selects all states from database specified and list them in
ascending order by id.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    host = "localhost"
    port = 3306
    user, passwd, db = sys.argv[1:4]
    db = MySQLdb.connect(
        host=host, port=port, user=user, passwd=passwd, db=db
    )

    cursor = db.cursor()
    stmt = "SELECT id, name FROM states ORDER BY id"
    cursor.execute(stmt)
    states = cursor.fetchall()

    for state in states:
        print(state)
