#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.Book import Book
from models.Author import Author

def create_database():
    Book.drop_table()
    Author.drop_table()
    Book.create_table()
    Author.create_table()

   

create_database()
