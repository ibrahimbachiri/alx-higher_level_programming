#!/usr/bin/python3
"""
Script to connect to a MySQL server and retrieve states from the hbtn_0e_0_usa database
whose names start with an uppercase 'N'.
Results are sorted by id in ascending order.
"""

import MySQLdb
from sys import argv

def filter_states(username, password, database):
    """
    Connect to MySQL server and fetch states from the hbtn_0e_0_usa database
    whose names start with an uppercase 'N'. Display the results sorted by id.
    """
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()

    # Execute the query to select states with names starting with 'N'
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
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
    Script entry point. Retrieve command line arguments and call filter_states function.
    """
    # Get command line arguments
    username, password, database = argv[1], argv[2], argv[3]

    # Call the filter_states function
    filter_states(username, password, database)
