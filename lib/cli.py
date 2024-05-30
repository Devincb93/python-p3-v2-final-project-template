# lib/cli.py

from models.Book import Book
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
import fire 

from helpers import (
    exit_program,
    menu,
    add_book_menu,
    get_all_books,
    get_all_authors,
    get_by_title
    
)
import pyfiglet

console = Console()

invalid = pyfiglet.figlet_format("Invalid", font="mini",)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "1":
            books_menu()
        elif choice == "2":
            authors_menu()
        elif choice == "3":
            exit_program()
        else:
            console.print("[bold red]*****Invalid choice*****[/bold red]")


def books_menu():
    while True:
        console.print(Panel("Books Menu:", border_style="blue"))
        console.print("1) Add a book")
        console.print("2) List all books")
        console.print("3) Delete a book")
        console.print("4) Search by title")
        console.print("5) Back to main menu")
        choice = input("> ")
        if choice == "1":
            add_book_menu()
        elif choice == "2":
            get_all_books()
        elif choice == "3":
            delete_book()
        elif choice == "4":
            get_by_title()
        elif choice == "5":
            main()
        else:
            print("Invalid choice")


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
                print(f"Book:{book.title} deleted successfuly ")
    else:
        books_menu()

def authors_menu():
    while True:
        console.print(Panel("Authors Menu:", border_style="blue"))
        console.print("1) List all Authors")
        console.print("2) Exit to Main Menu")
        choice = input("> ")
        if choice == "1":
            get_all_authors()
        elif choice == "2":
            main()
        else:
            console.print("[bold red]*****Invalid choice*****[/bold red]")


if __name__ == "__main__":
    fire.Fire(
        main()
    )
