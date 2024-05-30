#lib/Book.py

from models.__init__ import CONN,CURSOR
from models import Author
import fire


class Book:
    
    
    all = {}

    def __init__(self, title, genre, author, id=None):
        self.id = id
        self.title = title
        self.genre = genre
        self.author = author
        
    
        

    def __repr__(self):
        return (
            f"<Book {self.id}: {self.title}, {self.genre} " 
            
        )
    
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT,
            genre TEXT,
            author INTEGER,
            FOREIGN KEY (author) REFERENCES authors(id))
        """
        CURSOR.execute(sql)
        CONN.commit()
        

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS books;
        """
        CURSOR.execute(sql)
        CONN.commit()

    
    def save(self):
        sql = """
                INSERT INTO books (title, genre, author)
                VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.title, self.genre, self.author))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self


    @classmethod
    def create(cls, title, genre, author):
        book_id = cls(title, genre, author)
        book_id.save()
        return book_id
    

    def update(self):
        sql = """
            UPDATE books
            SET title = ?, genre = ?, author = ?,
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.title, self.genre, self.author,
                              self.id))
        CONN.commit()


    def delete(self):
        sql = """
            DELETE FROM books
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None


    @classmethod
    def instance_from_db(cls, row):
        book = cls.all.get(row[0])
        if book:
            book.title = row[1]
            book.genre = row[2]
            book.author = row[3]
        else:
            book = cls(row[1], row[2], row[3])
            book.id = row[0]
            cls.all[book.id] = book
        return book
    

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM books
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM books
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    

    @classmethod
    def find_by_title(cls, title):
        sql = """
            SELECT *
            FROM books
            WHERE title is ?
        """
        row = CURSOR.execute(sql, (title,)).fetchone()
        return cls.instance_from_db(row) if row else None


    def books(self):
        from models.Author import Author
        sql = """
            SELECT * FROM authors
            WHERE book.id = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [
            Author.instance_from_db(row) for row in rows
        ]

if __name__ =="__main__":
    fire.Fire(
        Book
    )    




