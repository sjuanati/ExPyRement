from v2.books.managers.base_storage import BaseStorage
from v2.books.managers.file_storage import FileStorage
from v2.books.managers.list_storage import ListStorage
from v2.books.managers.db_storage import DatabaseStorage


class StorageFactory:
    @staticmethod
    def get_storage(storage_type: str) -> BaseStorage:
        if storage_type == "file":
            return FileStorage()
        elif storage_type == "list":
            return ListStorage()
        elif storage_type == "db":
            return DatabaseStorage()
        else:
            raise ValueError(f"Unknown storage type: {storage_type}")


class BookManager:
    def __init__(self, storage_type: str = "file"):
        self.storage = StorageFactory.get_storage(storage_type)
        self.storage_type = storage_type

    @property
    def get_user_choice(self) -> str:
        return f"""
        Enter:
        - 'a' to add a new book
        - 'l' to list all books
        - 'r' to mark a book as read
        - 'd' to delete a book
        - 's' to change data storage ({self.storage_type})
        - 'q' to quit

        Your choice: """

    def prompt_add_book(self):
        name = input("Enter the name of the book: ").capitalize()
        author = input("Enter the author: ").capitalize()
        self.storage.add_book(name, author)

    def list_books(self):
        self.storage.list_books()

    def prompt_read_book(self):
        name = input("Enter the name of the book: ").capitalize()
        self.storage.mark_book_as_read(name)

    def prompt_delete_book(self):
        name = input("Enter the name of the book: ").capitalize()
        self.storage.delete_book(name)

    def prompt_storage(self) -> None:
        new_storage_type = input("Enter data storage (list,file,db): ")
        if new_storage_type not in ["list", "file", "db"]:
            print("Unknown storage")
        else:
            self.storage = StorageFactory.get_storage(new_storage_type)
            self.storage_type = new_storage_type

    def menu(self) -> None:
        user_options = {
            "a": self.prompt_add_book,
            "l": self.list_books,
            "r": self.prompt_read_book,
            "d": self.prompt_delete_book,
            "s": self.prompt_storage,
        }
        user_input = input(self.get_user_choice)
        while user_input != "q":
            if user_input in user_options:
                selected_function = user_options[user_input]
                selected_function()
            else:
                print("Unknown command. Please try again.")
            user_input = input(self.get_user_choice)


def test():
    manager = BookManager("db")  # Default
    manager.menu()
