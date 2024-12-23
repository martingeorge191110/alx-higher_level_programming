#!/usr/bin/python3
"""lists takes in arguments and displays all values
    in the states table of hbtn_0e_0_usa
    where name matches the argument.
    But this time, write one that
    is safe from MySQL injections!"""

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

    cur.execute("SELECT * FROM states WHERE name = %s;", (sys.argv[4],))

    states = cur.fetchall()

    for i in range(len(states)):
        print(f"{states[i]}")

    cur.close()
    db.close()
