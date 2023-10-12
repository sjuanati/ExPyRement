import pandas as pd
from v2.books.managers.base_storage import BaseStorage

BOOK_FILE = "src/v2/books/data/books.csv"


class FileStorage(BaseStorage):
    def add_book(self, name: str, author: str):
        # Check if the book already exists in the db
        with open(BOOK_FILE, "r") as file:
            if any(f"{name},{author}" in line for line in file):
                print("Book already in the database")
                return

        # Write book to the db
        with open(BOOK_FILE, "a") as file:
            file.write(f"{name},{author},False\n")

    def list_books(self):
        # Read the CSV into a DataFrame
        df = pd.read_csv(BOOK_FILE)

        # Iterate over each row in the DataFrame and print it
        for _, row in df.iterrows():
            is_read = "read" if row["read"] else "not read"
            print(f'{row["name"]} by {row["author"]}, {is_read}')

    def mark_book_as_read(self, name: str):
        df = pd.read_csv(BOOK_FILE)
        df.loc[df["name"] == name, "read"] = True
        df.to_csv(BOOK_FILE, index=False)

    def delete_book(self, name: str):
        df = pd.read_csv(BOOK_FILE)
        initial_len = len(df)
        df = df[df["name"] != name]
        deleted_rows = initial_len - len(df)
        if deleted_rows:
            print(f"{deleted_rows} book(s) named '{name}' deleted.")
        else:
            print(f"No book named '{name}' was found to delete.")
        df.to_csv(BOOK_FILE, index=False)
