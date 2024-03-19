#!/usr/bin/python3
"""Lists all states from the specified database."""
import MySQLdb
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    passw = sys.argv[2]
    db_name = sys.argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306, user=user,
                           passwd=passw, db=db_name)

    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM states WHERE name LIKE BINARY 'N%'
                   ORDER BY states.id""")
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    conn.close()
