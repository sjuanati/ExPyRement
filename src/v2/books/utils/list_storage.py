from v2.books.utils.base_storage import BaseStorage


class ListStorage(BaseStorage):
    def __init__(self) -> None:
        self.books = []
        super().__init__()

    def add_book(self, name, author):
        if name in [book["name"] for book in self.books]:
            print(f"The book {name} already exists")
            return

        if name and author:
            new_book = {"name": name, "author": author, "read": False}
            self.books.append(new_book)
        else:
            print("Missing data -book not added")

    def list_books(self):
        if len(self.books) == 0:
            print("No books in the list")
        for book in self.books:
            is_read = "read" if book["read"] else "not read"
            print(f'{book["name"]} by {book["author"]}, {is_read}')

    def mark_book_as_read(self, name):
        for book in self.books:
            if book["name"] == name:
                book["read"] = True
                return
        print(f"Book {name} not found")

    def delete_book(self, name):
        self.books = [book for book in self.books if book["name"] != name]
