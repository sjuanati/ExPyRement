import re
import logging
from bs4 import BeautifulSoup

from v2.scrapping_books.locators.book_locators import BookLocators
from v2.scrapping_books.parsers.book import BookParser

logger = logging.getLogger('scraping.books_page')

class BooksPage:
    def __init__(self, page):
        logger.debug('Parsing page content with BeautifulSoup HTML parser')
        self.soup = BeautifulSoup(page, "html.parser")

    @property
    def books(self):
        logger.debug(f'Finding all books in the page using `{BookLocators.ARTICLE}`')
        return [BookParser(e) for e in self.soup.select(BookLocators.ARTICLE)]

    @property
    def page_count(self):
        logger.debug('Finding all number of catalogue pagers available...')
        content = self.soup.select_one(BookLocators.PAGER).string
        logger.info(f'Found number of catalogue pages available: `{content}`.')
        pattern = 'Page [0-9]+ of ([0-9]+)' 
        matcher = re.search(pattern, content)
        pages = int(matcher.group(1))
        logger.debug(f'Extracted number of pages as integer: `{pages}`')
        return pages
