"""
===============================================================================
Library Management System (Python OOP Exercise)
===============================================================================

Author       : Shahroze
Date         : 21-Dec-2025
Purpose      : 
    - Demonstrates Python classes, inheritance, and instance variables
    - Create a library, add books, print all books, get number of books
    - Shows that data does not persist after the program stops

Usage        :
    1. Run the script to create a default library
    2. Use 'management()' method to add new books
    3. Use 'print_all_books()' to list all books
    4. Use 'get_number_of_books()' to get total count of books

Notes        :
    - This is an in-memory demonstration; data is lost when program ends
    - Designed for educational purposes and Python OOP practice

===============================================================================
"""

# Exercise 6 : Library Management System
"""
Write a Library class with no_of_books and books are 2 instance variables. Write a program to create a library from
this library class and show how you can print all books, add a book and get the number of books using different 
methods. Show that your program doesn't persist the books after the program is stopped !
(“persist” here just means keep the data saved permanently)
"""
import os
os.system('cls')
class Library :
    def __init__(self, no_of_books, books):
        self._no_of_books = no_of_books
        self._books = books
    def Create_Library(self):
        self._books = [ "The Alchemist",
    "Into the Wild",
    "Atomic Habits",
    "The Mountain Is You",
    "Life of Pi",
    "Man’s Search for Meaning",
    "The Call of the Wild",
    "Can’t Hurt Me",
    "Think Like a Monk", 
    "Rich Dad Poor Dad"]
        self._no_of_books = len(self._books)
        print(f'Books in Library : {self._books}','\n', 'No of Books : ', {len(self._books)})
    # Method to print all books
    def print_all_books(self):
        print("Books in Library:")
        for book in self._books:
            print("-", book)

    # Method to get the number of books
    def get_number_of_books(self):
        print("Total number of books:", len(self._books))
        return len(self._books)
class Manage_Library(Library):
    def management(self):
        self._add_book = input('Enter name of book you want : ')
        if self._add_book.strip() != "":  # checks that input is not empty :
            self._books.append(self._add_book)  # just append, no assignment
            self._no_of_books = len(self._books)
            print(self._add_book, 'has been added successfully')
            print(f'Now total books in Library are : {self._books} and new number of books is {len(self._books)}')
        else :
            print(self._books)

library = Manage_Library(10, [ "The Alchemist",
    "Into the Wild",
    "Atomic Habits",
    "The Mountain Is You",
    "Life of Pi",
    "Man’s Search for Meaning",
    "The Call of the Wild",
    "Can’t Hurt Me",
    "Think Like a Monk", 
    "Rich Dad Poor Dad"])
library.Create_Library()
library.management()