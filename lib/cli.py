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
    find_books_by_title,
    delete_book,
    add_a_author,
    delete_author,
    select_an_author,
    authors_menu,
    book_menu_text,
    library_menu_text,
    find_books_by_author
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

def library_menu():
    while True:
        authors_menu()
        choice = input("> ")
        if choice == "1":
            library_menus()
        if choice == "2":
            book_menu()


def library_menus():
    while True:
        library_menu_text()
        
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
            select_an_author()


        if choice == "6":
            delete_book()
            
        if choice == "7":
            find_books_by_title()
        if choice == "8":
            find_books_by_author()
        elif choice == "0":
            library_menu()
        else:
            console.print("")

def book_menu():
    while True:
        book_menu_text()
        choice = input("> ")
        if choice == "1":
            find_books_by_title()
            book_menu()
        if choice == "2":
            find_books_by_author()
        else:
            library_menu()






if __name__ == "__main__":
    fire.Fire(
        main()
    )
