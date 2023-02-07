# Written By: Gavin Bernard
# Date: 2/6/2023

import mysql.connector
from mysql.connector import errorcode

# setup for SQL database'''
config = {
    "user": "root",
    "password": "sqlpass159",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try: # attempts to connect to the database
    db = mysql.connector.connect(**config)

    cursor = db.cursor()

    '''select statement for tables; uses inner join'''
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    players = cursor.fetchall()

    print("\n  -- DISPLAYING PLAYER RECORDS --")

    '''prints out information based on select statement above'''
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

    input("\n\n  Press any key to continue... ")

except mysql.connector.Error as err: # provides errors if username or password are wrong, or database doesn't exist

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid.")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist.")

    else:
        print(err)

finally: # closes the database connection
    db.close()
