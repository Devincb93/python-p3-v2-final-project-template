#lib/models/Author

from models.__init__ import CONN,CURSOR
import fire

class Author:
    all={}
    written_books=[]
    

    def __init__(self, name, id=None):
        self.id = id
        self.name = name
        
        
        
        
        

    def __repr__(self):
        return (
            f"<Author {self.id}: {self.name}" 
            
        )
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY,
            name TEXT
            )
            
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        
        sql = """
            DROP TABLE IF EXISTS authors;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
                INSERT INTO authors (name)
                VALUES (?)
        """

        CURSOR.execute(sql, (self.name,))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name):
        author = cls(name)
        author.save()
        return author

    def update(self):
        sql = """
            UPDATE authors
            SET name = ?, 
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name,
                              self.id))
        CONN.commit()


    def delete(self):
        sql = """
            DELETE FROM authors
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None


    @classmethod
    def instance_from_db(cls, row):
        author = cls.all.get(row[0])
        if author:
           
            author.name = row[1]
            
        else:
            
            author = cls(row[1], row[2])
            author.id = row[0]
            cls.all[author.id] = author
        return author


    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM authors
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM authors
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None


    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM authors
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None


    def get_books_by_author(self):
        from models.Book import Book
        sql = """
            SELECT * FROM books
            WHERE author_id = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [
            Book.instance_from_db(row) for row in rows
        ]
    

if __name__ == "__main__":
    fire.Fire(Author)
