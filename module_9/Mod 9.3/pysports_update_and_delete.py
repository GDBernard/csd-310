#Written By: Gavin Bernard
#Date: 2/6/2023

import mysql.connector
from mysql.connector import errorcode

#sets up connection to SQL database
config = {
    "user": "root",
    "password": "sqlpass159",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    #attempts to connect to SQL database
    db = mysql.connector.connect(**config)

    cursor = db.cursor()

    #inserts player Smeagol into database; shows results with join query
    player_data = ("Smeagol", "Shire Folk", 1)

    cursor.execute("INSERT INTO player(first_name, last_name, team_id)" "VALUES(%s, %s, %s)", player_data)

    db.commit()

    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    players = cursor.fetchall()

    print("--DISPLAYING PLAYERS AFTER INSERT--")
    
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

    #update player Gollum; set to team 2; show new results using join query
    cursor.execute("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")

    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    players = cursor.fetchall()

    print("--DISPLAYING PLAYERS AFTER UPDATE--")
    
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

    #delete player Gollum; show new results using join query
    cursor.execute("DELETE FROM player WHERE first_name = 'Gollum'")

    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    players = cursor.fetchall()

    print("--DISPLAYING PLAYERS AFTER DELETE--")
    
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

    db.commit()

    input("\n\n  Press any key to continue... ")

except mysql.connector.Error as err: #handles exceptions for user/pass error, or database not existing

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")

    else:
        print(err)

finally: #closes the SQL database connection
    db.close()
