#Written By: Gavin Bernard
#Date: 2/21/2023

import mysql.connector
from mysql.connector import errorcode

#sets up connection to database
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

#displays the menu; shows each time user makes a choice
def show_menu():
    print("\u0332".join("\nMain Menu "))
    print("1. Show Books")
    print("2. Show Locations")
    print("3. Your Account")
    print("4. Exit")

#displays the available books
def show_books(_cursor):
    _cursor.execute("SELECT book_name, author, details from book")

    books = _cursor.fetchall()

    print("")
    print("\n--- Displaying Books ---")

    #displays name, author, and details of each book
    for book in books:
        print("Name: " + book[0])
        print("Author: " + book[1])
        print("Details: " + book[2] + "\n")

#displays the available locations
def show_locations(_cursor):
    _cursor.execute("SELECT store_id, locale from store")

    locations = _cursor.fetchall()

    print("\n--- Displaying Locations ---")

    #displays location of location
    for location in locations:
        print("Location: " + location[1] + "\n")

#validates the user; provides error if incorrect
def validate_user(cust_id):
    if (0 < int(cust_id) < 4):
        print("Welcome, Customer #" + str(cust_id) + "!")
        return 1
    else:
        print("Invalid Customer #. Please try again.")
        return 0

#displays the account menu
def show_account_menu():
    print("\u0332".join("\nCustomer Menu "))
    print("1. Wishlist")
    print("2. Add Book")
    print("3. Return")

#shows the user's wishlist using their ID
def show_wishlist(_cursor, _user_id):
    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))

    wishlist = _cursor.fetchall()

    print("\n--- Displaying Books in Wishlist---")

    #displays name and author of books in wishlist
    for book in wishlist:
        print("Name: " + book[4])
        print("Author: " + book[5] + "\n")

#shows available books to add to user's wishlist using their ID
def show_books2add(_cursor, _user_id):
    query = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))
    
    _cursor.execute(query)

    books2add = _cursor.fetchall()

    print("\n--- Displaying Books to Add---")

    #displays ID and book name of available wishlist books
    for book in books2add:
        print("Book ID: " + str(book[0]))
        print("Name: " + book[1] + "\n")

#adds book to user's wishlist
def add_book2list(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))

def main():
    try:
        db = mysql.connector.connect(**config)

        cursor = db.cursor()
        
        print("Database user {} connected to MySQL on host {} with database {}.".format(config["user"], config["host"], config["database"]))

        print(". . .")

        print("--- Welcome to WhatABook ---")

        select = 0;

        #main menu of program; allows user to choose 1-4 from menu
        '''
            1 - runs show_books(), showing the user all available books
            2 - runs show_locations(), showing user all locations
            3 - validates the user before providing the customer menu
            4 - closes program

            <0 or >4 - invalid inputs; program checks for this error
            "example" - program does not allow non-ints, checks for this error
        '''
        while select != 4:
            show_menu()

            try:
                select = int(input("Select an option: "))
                
            except ValueError:
                #resets the select value, notes user of error, and passes
                print("Error in value entered. Please try again.")
                select = 0
                pass

            if select == 1:
                show_books(cursor)

            if select == 2:
                show_locations(cursor)

            if select == 3:
            #attempts to validate user; if validated, enter customer menu
                try:
                    cust_id = int(input("Please enter your Customer ID: "))
                    
                except ValueError:
                    #resets the cust_id value, notes user of error, and passes
                    print("Error in value entered. Please try again.")
                    cust_id = 0
                    pass
                    
                if (validate_user(cust_id) == 1):
                    cust_option = 0

                    while cust_option != 3:
                        '''
                            1 - shows the user's wishlist
                            2 - displays a list of available books; user may add one to their wishlist; also checks for errors
                            3 - exists the customer menu and returns to the main menu

                            <0 or >4 - invalid inputs; program checks for this error
                            "example" - program does not allow non-ints, checks for this error
                        '''
                        show_account_menu()

                        try:
                            cust_option = int(input("Select an option: "))
                            
                        except ValueError:
                            #resets the option value, notes user of error, and passes
                            print("Error in value entered. Please try again.")
                            cust_option = 0
                            pass

                        if cust_option == 1:
                            show_wishlist(cursor, cust_id)

                        if cust_option == 2:
                            show_books2add(cursor, cust_id)

                            book = int(input("Enter the ID of the book: "))

                            add_book2list(cursor, cust_id, book)

                            db.commit()

                            print("Book #" + str(book) + " was added to your wishlist!")

                        if cust_option == 3:
                            pass
                        
                        if (cust_option < 0 or cust_option > 3):
                            print("Input is incorrect. Please try again.")

            if select == 4:
                pass

            if (select < 0 or select > 4):
                print("Input is incorrect. Please try again.")

    finally:
        #if you made it this far, have a good day, reader :)
        print("Closing Whatabook. Have a nice day.")
        db.close()

main()
