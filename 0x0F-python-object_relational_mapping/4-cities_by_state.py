#!/usr/bin/python3
"""l lists all cities
    from the database hbtn_0e_4_usa"""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )

    cur = db.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name \
                FROM cities JOIN states \
                ON states.id = cities.state_id \
                ORDER BY cities.id ASC")

    result = cur.fetchall()
    for i in result:
        print(i)

    cur.close()
    db.close()
