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
    cursor.execute("""SELECT cities.id, cities.name, states.name FROM cities
                   INNER JOIN states ON states.id=cities.state_id""")
    cities = cursor.fetchall()

    for city in cities:
        print(city)

    cursor.close()
    conn.close()
