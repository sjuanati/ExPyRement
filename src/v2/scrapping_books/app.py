import logging
import requests
from typing import List

from v2.scrapping_books.pages.books_page import BooksPage
from v2.scrapping_books.parsers.book import BookParser
from v2.scrapping_books.menu import (
    print_best_books,
    print_cheapest_books,
    print_best_cheapest_books,
)

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
    datefmt="%d-%m-%Y %H:%M:%S",
    level=logging.INFO,
    filename="logs.txt",
)

logger = logging.getLogger("scraping")

class BookManager:
    URL = "https://books.toscrape.com/"

    def __init__(self):
        self.books = self.retrieve_books()
        self.books_gen = (book for book in self.books)

    def retrieve_books(self) -> List[BookParser]:
        # Fetch the first page to determine the total number of pages
        first_page_content = requests.get(self.URL + "catalogue/page-1.html").content
        print(f"reading page 1")
        first_page = BooksPage(first_page_content)
        total_pages = first_page.page_count

        # Initialize the books list with books from the first page
        _books = first_page.books

        # Fetch books from the remaining pages
        for page in range(2, total_pages + 1):
            url = self.URL + f"catalogue/page-{page}.html"
            page_content = requests.get(url).content
            print(f"reading page {page}")
            page = BooksPage(page_content)
            _books.extend(page.books)

        return _books

    def look_top_books(self):
        top_books = [book for book in self.books if book.stars == 5]
        for book in top_books:
            print(book)

    def look_cheapest_books(self):
        cheapest_books = sorted(self.books, key=lambda x: x.price)[:10]
        for book in cheapest_books:
            print(book)

    def get_next_available_book(self):
        print(next(self.books_gen))

    @property
    def get_user_choice(self) -> str:
        return f"""Enter one of the following:
            - 'b' to look at 5-star books
            - 'c' to look at the cheapest books
            - 'n' to just get the next available book on the catalogue
            - 'q' to exit
        """

    def menu(self):
        user_options = {
            "b": self.look_top_books,
            "c": self.look_cheapest_books,
            "n": self.get_next_available_book,
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
    logger.info('Loading books list...')
    manager = BookManager()
    manager.menu()

    # print('ALL BOOKS')
    # for book in books:
    #     print(book)
    # print('-------- TOP 10 best books --------')
    # print_best_books(books)
    # print('-------- TOP 10 cheapest books --------')
    # print_cheapest_books(books)
    # print('-------- TOP 10 best cheapest books --------')
    # print_best_cheapest_books(books)
