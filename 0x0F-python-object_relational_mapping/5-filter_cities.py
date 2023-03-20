#!/usr/bin/python3

"""
This module provides script to connect to Mysql database and execute SQL
statements.
It list cities in a state
"""

import sys
import MySQLdb

if __name__ == "__main__":
    host = "localhost"
    port = 3306
    user, passwd, db, state_name = sys.argv[1:5]
    db = MySQLdb.connect(
        host=host, port=port, user=user, passwd=passwd, db=db
    )

    cursor = db.cursor()
    stmt = "SELECT cities.name \
        FROM cities \
        JOIN states ON cities.state_id = states.id \
        WHERE states.name = %s"
    cursor.execute(stmt, (state_name,))
    cities = cursor.fetchall()

    cities_list = [city[0] for city in cities]

    print(", ".join(cities_list))
