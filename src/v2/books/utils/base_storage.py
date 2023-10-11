from abc import ABC, abstractmethod


class BaseStorage(ABC):
    @abstractmethod
    def add_book(self, name, author):
        raise NotImplementedError

    @abstractmethod
    def mark_book_as_read(self, name):
        raise NotImplementedError

    @abstractmethod
    def list_books(self):
        raise NotImplementedError

    @abstractmethod
    def delete_book(self, name):
        raise NotImplementedError
