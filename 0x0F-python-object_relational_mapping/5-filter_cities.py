#!/usr/bin/python3
"""
Script to connect to a MySQL server and retrieve cities of a specific state
Results are sorted by cities.id and display the cities as a comma-separated string.
"""

import MySQLdb
from sys import argv

def filter_cities(username, password, database, state_name):
    """
    Connect to MySQL server and fetch cities of a specific state from the hbtn_0e_4_usa database.
    Results are sorted by cities.id and display the cities as a comma-separated string.
    """
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()

    # Execute the query to select cities of the specified state
    query = """
            SELECT name
            FROM cities
            WHERE state_id = (SELECT id FROM states WHERE name = %s)
            ORDER BY id ASC
            """
    cursor.execute(query, (state_name,))

    # Fetch all the rows
    rows = cursor.fetchall()

    # Display the results as a comma-separated string
    cities = ', '.join(city[0] for city in rows)
    print(cities)

    # Close the cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    """
    Script entry point. Retrieve command line arguments and call filter_cities function.
    """
    # Get command line arguments
    username, password, database, state_name = argv[1], argv[2], argv[3], argv[4]

    # Call the filter_cities function
    filter_cities(username, password, database, state_name)
