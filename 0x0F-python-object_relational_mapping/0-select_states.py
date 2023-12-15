#!/usr/bin/python3
"""
Script to connect to a MySQL server and retrieve states from the hbtn_0e_0_usa database.

Usage: ./0-select_states.py <username> <password> <database>
"""

import MySQLdb
from sys import argv


def select_states(username, password, database):
    """
    Connect to MySQL server and fetch states from the hbtn_0e_0_usa database.
    Display the results sorted by id in ascending order.
    """
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()

    # Execute the query to select all states sorted by id
    query = "SELECT * FROM states ORDER BY id ASC"
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
    Script entry point. Retrieve command line arguments and call select_states function.
    """
    # Get command line arguments
    username, password, database = argv[1], argv[2], argv[3]

    # Call the select_states function
    select_states(username, password, database)
