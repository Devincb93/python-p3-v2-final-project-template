# lib/cli.py

from models.Book import Book
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
import fire 
import pyfiglet
from models.Author import (Author)
from helpers import (
    exit_program,
    menu,
    list_all_books,
    get_all_authors,
    find_books_by_title
)


console = Console()

invalid = pyfiglet.figlet_format("Invalid", font="mini",)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "1":
            library_menu()
        elif choice == "0":
            exit_program()
        else:
            console.print("[bold red]*****Invalid choice*****[/bold red]")

def delete_book():
    books = Book.get_all()
    table = Table(title="Available Books", border_style="blue")
    table.add_column("Book Titles")
    for book in books:
        table.add_row(book.title)
    console.print(table)
    console.print(Panel("Enter the name of the book you want to Delete:", border_style="blue"))
    delete_selection = input("Title: ")
    if len(delete_selection) > 0:
        for book in books:
            if delete_selection in book.title:
                book.delete()
                console.print(f"Book:{book.title} deleted successfuly ")
    else:
        library_menu()

def library_menu():
    while True:
        console.print(Panel("Library Menu:", border_style="blue"))
        console.print("1) List all authors")
        console.print("2) Add a author")
        console.print("3) Delete a author")
        console.print("4) List all books")
        console.print("5) Add a book by author")
        console.print("6) Delete a book")
        console.print("7) Find books by title")
        console.print("8) Find book by author")
        console.print("0) Exit to Main Menu")
        
        choice = input("> ")
        if choice == "1":
            get_all_authors()
        if choice == "2":
            add_a_author()
        if choice == "3":
            delete_author()
        if choice == "4":
            list_all_books()
        if choice == "5":
            add_book_by_author()
        if choice == "6":
            delete_book()
        if choice == "7":
            find_books_by_title()
        if choice == "8":
            find_books_by_author()
        elif choice == "0":
            main()
        else:
            console.print("")

def add_a_author():
    console.print("Enter the name of the author to add:")
    name = input("Name: ")
    if len(name) > 0:
        if not Author.find_by_name(name):
            Author.create(name)
            console.print(f"{name} has been added successfully")
        else:
            console.print(f"[bold red]{name}, already exists. Please enter a new Author.[/bold red]")
            add_a_author()
    else:
        library_menu()

def delete_author():
    authors = Author.get_all()
    author_table = Table(title="Authors")
    author_table.add_column("Names:")
    if len(authors) > 0:
        for author in authors:
            author_table.add_row(author.name)
        console.print(author_table)
    else:
        console.print("No authors exist, please add one")
        add_a_author()
    console.print("Enter the name of the author you would like to remove:")
    name_to_delete = input("Name: ")
    for author in authors:
        if name_to_delete == author.name:
            author.delete()
            console.print(f"{author.name} was deleted successfully")
        

def add_book_by_author():
    while True:
        selection_number = 1
        authors = Author.get_all()
        console.print(Panel("Select a Author, or press Enter to go back:"))
        for author in authors:
            console.print(f" {author.name}")
            selection_number += 1

        
        
        choice = input("> ")
        if choice == "":
            menu()
        for author in authors:

            if choice == (f"{author.name}"):
                    add_authors_book(author.id)
        else:
            break
        
        
def add_authors_book(id):
    author = Author.find_by_id(id)
    console.print("Enter the book information:")
    title = input("Title: ")
    genre = input("Genre: ")
    author_id = author.id 
    Book.create(title, genre, author_id)
    menu()   


def find_books_by_author():
    authors = Author.get_all()
    books = Book.get_all()
    book_author_table = Table(title="Found books:", border_style="blue")
    book_author_table.add_column("Titles")
    console.print(Panel("Enter the name of the author:"))
    authors_name = input("Name: ")
    if len(authors_name) > 0:
        for author in authors:
            if authors_name in author.name:
                for book in books:
                    if book.author_id == author.id:
                        book_author_table.add_row(book.title)
    else:
        library_menu()
    console.print(book_author_table)


if __name__ == "__main__":
    fire.Fire(
        main()
    )
