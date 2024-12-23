#!/usr/bin/python3
"""l lists all cities from the database hbtn_0e_4_usa"""

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

    cur.execute("SELECT c.name, s.name \
        FROM cities c \
        JOIN states s ON s.id = c.state_id \
        ORDER BY c.id ASC")

    states = cur.fetchall()

    result = cur.fetchall()
    for i in result:
        print(i)

    cur.close()
    db.close()
