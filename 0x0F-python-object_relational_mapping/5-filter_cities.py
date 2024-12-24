#!/usr/bin/python3
"""l name of a state as an argument
    and lists all cities of that stat"""

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

    cur.execute("SELECT c.name FROM cities c \
                JOIN states s ON s.id = c.state_id \
                WHERE s.name = %s;", (sys.argv[4],))

    result = cur.fetchall()
    for i in range(len(result)):
        if i == len(result) - 1:
            print(result[i][0])
        else:
            print(result[i][0], end=", ")

    cur.close()
    db.close()
