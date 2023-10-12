import sqlite3
from typing import Any, Tuple
from v2.books.utils.base_storage import BaseStorage


class DatabaseStorage(BaseStorage):
    def __init__(self):
        self.database = "data.db"
        self.create_book_table()
        super().__init__()

    def _execute_query(
        self, query: str, parameters: Tuple[Any, ...] = ()
    ) -> sqlite3.Cursor:
        # The key aspect of the with statement is that it ensures the __enter__ method is called
        # when entering the block and __exit__ is called when exiting the block.
        # For the sqlite3.connect() function, the __exit__ method handles closing the connection.
        with sqlite3.connect(self.database) as connection:
            cursor = connection.cursor()
            cursor.execute(query, parameters)
            connection.commit()
            return cursor

    def create_book_table(self):
        self._execute_query(
            "CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)"
        )

    def add_book(self, name: str, author: str):
        # don't do this to prevent sql injection attacks
        # self._execute_query(f'INSERT INTO books VALUES("{name}","{author}",0)')
        try:
            self._execute_query("INSERT INTO books VALUES(?,?,0)", (name, author))
        except sqlite3.IntegrityError:
            print(f"Book '{name}' already exists in the database")

    def list_books(self):
        cursor = self._execute_query("SELECT * FROM books")
        # option 1
        books = cursor.fetchall()
        for book in books:
            is_read = "read" if book[2] else "not read"
            print(f"{book[0]} by {book[1]}, {is_read}")
        # option 2 (not showing results because the cursor is already at the end)
        books = [
            {"name": row[0], "author": row[1], "read": row[2]}
            for row in cursor.fetchall()
        ]
        for book in books:
            is_read = "read" if book["read"] else "not read"
            print(f'{book["name"]} by {book["author"]}, {is_read}')

    def mark_book_as_read(self, name: str):
        self._execute_query("UPDATE books SET read = 1 WHERE name = ?", (name,))

    def delete_book(self, name):
        self._execute_query("DELETE FROM books WHERE name = ?", (name,))
