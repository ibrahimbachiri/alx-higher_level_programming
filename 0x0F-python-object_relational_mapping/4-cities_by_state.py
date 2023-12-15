#!/usr/bin/python3
"""
Script to connect to a MySQL server and retrieve cities from the hbtn_0e_4_usa database
Results are sorted by cities.id and display the city, state, and state name.
"""

import MySQLdb
from sys import argv

def cities_by_state(username, password, database):
    """
    Connect to MySQL server and fetch cities from the hbtn_0e_4_usa database.
    Results are sorted by cities.id and display the city, state, and state name.
    """
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()

    # Execute the query to select cities with their corresponding state names
    query = """
            SELECT cities.id, cities.name, states.name
            FROM cities
            INNER JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC
            """
    cursor.execute(query)

    # Fetch all the rows
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    """
    Script entry point. Retrieve command line arguments and call cities_by_state function.
    """
    # Get command line arguments
    username, password, database = argv[1], argv[2], argv[3]

    # Call the cities_by_state function
    cities_by_state(username, password, database)
