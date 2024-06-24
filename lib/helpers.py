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
    console.print("1) Start Program")
    console.print("0) Exit Program")

def authors_menu():
    console.print(Panel("Library Menu:", border_style="blue"))
    console.print("1) Author's Menu")
    console.print("2) Book's Menu")

def book_menu_text():
    console.print(Panel("Book's Menu: ", border_style="blue"))
    console.print("1) Search for book by title")
    console.print("2) Search for books by Author")


def library_menu_text():
    console.print(Panel("Author's Menu:", border_style="blue"))
    console.print("1) List all authors")
    console.print("2) Add an author")
    console.print("3) Delete a author")
    console.print("4) List all books")
    console.print("5) Pick an author and add a book")
    console.print("0) Exit to Main Menu")


def exit_program():
    console.print(Panel("[bold red]Program Terminated[/bold red]", border_style="blue"))
    exit()

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

def select_an_author():
        authors = Author.get_all()
        for i, author in enumerate(authors, start=1):
            console.print(f"{i}) {author.name}")
        choice = input("> ")
        if 0 <= int(choice) <= len(authors):
            selected_author = authors[int(choice) -1]
            add_authors_book(selected_author)
    

def add_authors_book(author):
    # authors = Author.get_all()
    # selected_author = authors[i]
    console.print("Enter the book information:")
    title = input("Title: ")
    genre = input("Genre: ")
    author_id = author.id
    Book.create(title, genre, author_id)
    menu()
    

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
            searches = []
            for book in Book.get_all():
                searched = Table(border_style="blue")
                searched.add_column("Your Search:")
                if search.lower() in book.title.lower():
                    searches.append(book.title)
                for sear in searches:   
                    searched.add_row(sear)
        console.print(searched)

def find_books_by_author():
    found_books = Author.books()
    console.print(found_books)
            
        
        
        
    
    
   
    
        
    

        




    