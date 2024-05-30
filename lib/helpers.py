# lib/helpers.py
from rich import print
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
import pyfiglet
from models.Book import (Book)
from models.Author import(Author)



console = Console()

all_authors = []

ascii_art = pyfiglet.figlet_format("The Library", font="standard" )
invalid = pyfiglet.figlet_format("Invalid", font="small",)

def menu():
    console.print(Panel(ascii_art, border_style="blue"))
    console.print(Panel("[bold]Please select an option:[/bold]", border_style="blue"))
    console.print("1) Book's Menu")
    console.print("2) Author's Menu")
    console.print("3) Exit Program")


def exit_program():
    console.print(Panel("Program Terminated", border_style="blue"))
    exit()


def add_book_menu():
    print("Enter your book details:")
    title = input("Title: ")
    genre = input("Genre: ")
    author = input("Author: ")
    if len(title) > 0 and len(genre) > 0 and len(author) > 0:
        author = Author.create(author)
        Book.create(title, genre, author.id)
        if not title in Author.written_books:
            Author.written_books.append(title)
        console.print(f"{title}, has been added to the books list")
    else:
        console.print("[bold red]Book was unable to be added, please check with administrator[/bold red]")
        add_book_menu()

def get_all_books():
    books = Book.get_all()
    all_table = Table(title="Available Books", border_style="blue")
    all_table.add_column("Book Titles", justify="left", style="cyan")
    for book in books:
        all_table.add_row(book.title)
    console.print(all_table)

def get_all_authors():
    authors = Book.get_all()
    author_table = Table( border_style="blue")
    author_table.add_column("Authors")
    for each in authors:
        if not each.author.id in all_authors:
            all_authors.append(each.author.id)
    for each in all_authors:
        author_table.add_row(each)
    console.print(author_table)

def get_by_title():
    console.print(Panel("Enter the title of the book you are searching for", border_style="blue"))
    search = input(str("Title: "))
    if len(Book.get_all()) > 0 and len(search) > 0:
        for book in Book.get_all():
            if search in book.title:
                searched = Table(border_style="blue")
                searched.add_column("Your Search:")
                searched.add_row(book.title)
                console.print(searched)
    else:
        menu()
    

        




    