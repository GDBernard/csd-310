/*
    Title: db_init.sql
    Author: Gavin Bernard
    Date: 3/1/2023
    Description: whatabook database initialization script
*/

DROP USER IF EXISTS 'whatabook_user'@'localhost';

CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id));

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id));

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id));

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id));


INSERT INTO store(locale)
    VALUES('735 Haywood Rd, Greenville, SC 29607');

INSERT INTO book(book_name, author, details)
    VALUES('Shadows of Carcosa', 'Edgar Allan Poe', 'A collection of short stories, centering around the themes of costmic horror.');

INSERT INTO book(book_name, author, details)
    VALUES('The Call of Cthulhu and Other Weird Stories', 'H.P. Lovecraft', 'A collection of horro stories.');

INSERT INTO book(book_name, author, details)
    VALUES('Songs of a Dead Dreamer', 'Thomas Ligotti', 'A short story collection named after different types of dreams.');

INSERT INTO book(book_name, author, details)
    VALUES('The Ballad of Black Tom', 'Victor LaValle', 'A horror story depicting a character manipulating a powerful and mysterious force.');

INSERT INTO book(book_name, author, details)
    VALUES('The Fisherman', 'John Langan', 'A horror story involving two widowers who bond over their shared grief and enjoyment of fishing.');

INSERT INTO book(book_name, author, details)
    VALUES('Pathfinder Core Rulebook', 'Jason Bulmahn', 'A guide to the Pathfinder roleplaying game.');

INSERT INTO book(book_name, author, details)
    VALUES('Music Theory for Dummies', 'Michael Pilhofer', 'A guide to music theory for all levels of musical understanding.');

INSERT INTO book(book_name, author, details)
    VALUES('Musical Composition for Dummies', 'Scott Jarrett', 'Teaches about the history of composition.');

INSERT INTO book(book_name, author, details)
    VALUES('D&D Players Handbook', 'James Wyatt', 'A guide to the Dungeons and Dragons Fifth Edition roleplaying game.');


INSERT INTO user(first_name, last_name) 
    VALUES('Alice', 'Antoinette');

INSERT INTO user(first_name, last_name)
    VALUES('Bob', 'Brown');

INSERT INTO user(first_name, last_name)
    VALUES('Candice', 'Camidge');


INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Alice'), 
        (SELECT book_id FROM book WHERE book_name = 'D&D Players Handbook'));

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Bob'),
        (SELECT book_id FROM book WHERE book_name = 'The Fisherman'));

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Candice'),
        (SELECT book_id FROM book WHERE book_name = 'Music Theory for Dummies'));
