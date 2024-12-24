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

    cur.execute("SELECT c.name FROM cities c, states s \
                WHERE s.name = %s \
                AND s.id = c.state_id", (sys.argv[4],))

    result = cur.fetchall()
    for city in result:
        for city_name in city:
            if result.index(city) == len(result) - 1:
                print(city_name, end="")
            else:
                print(city_name, end=", ")

    cur.close()
    db.close()
