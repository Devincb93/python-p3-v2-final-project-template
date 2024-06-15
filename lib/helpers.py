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
    console.print("1) Library Terminal")
    console.print("0) Exit Program")


def exit_program():
    console.print(Panel("[bold red]Program Terminated[/bold red]", border_style="blue"))
    exit()




def list_all_books():
    books = Book.get_all()
    all_table = Table(title="Available Books", border_style="blue")
    all_table.add_column("Book Titles", justify="left", style="cyan")
    for book in books:
        all_table.add_row(book.title)
    console.print(all_table)

def get_all_authors():
    authors = Author.get_all()
    author_table = Table( border_style="blue")
    author_table.add_column("Authors")
    if len(authors) > 0:
        for author in authors:
            author_table.add_row(author.name)
        console.print(author_table)
    else:
        console.print("[bold red]*****No authors found*****[/bold red]")

def find_books_by_title():

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
    

        




    