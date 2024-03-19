#!/usr/bin/python3
"""Lists all states from the specified database."""
import MySQLdb
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    passw = sys.argv[2]
    db_name = sys.argv[3]
    state_nm = sys.argv[4]

    conn = MySQLdb.connect(host="localhost", port=3306, user=user,
                           passwd=passw, db=db_name)

    cursor = conn.cursor()
    cursor.execute("""SELECT cities.name FROM cities
                   INNER JOIN states ON states.id=cities.state_id
                   WHERE states.name = %s ORDER BY cities.id ASC""",
                   (state_nm,))
    cities = cursor.fetchall()

    city_names = [city[0] for city in cities]

    cities_string = ", ".join(city_names)

    """ for city in cities:
        print(city)"""

    print(cities_string)

    cursor.close()
    conn.close()
