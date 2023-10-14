from bs4 import BeautifulSoup

from v2.scrapping_quotes.locators.quotes_page_locators import QuotesPageLocators
from v2.scrapping_quotes.parsers.quote import QuoteParser

class QuotesPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def quotes(self):
        locator = QuotesPageLocators.QUOTE
        quote_tags = self.soup.select(locator) # find each div that has a quote class
        return [QuoteParser(e) for e in quote_tags] # pass each div to QuoteParser
    
        # Returns a list of quote instances:
        # [
        #     <Quote “The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”, by Albert Einstein>,
        #     <Quote “It is our choices, Harry, that show what we truly are, far more than our abilities.”, by J.K. Rowling>,
        #     <Quote “There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”, by Albert Einstein>,
        #     <Quote “The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”, by Jane Austen>,
        #     <Quote “Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”, by Marilyn Monroe>,
        #     <Quote “Try not to become a man of success. Rather become a man of value.”, by Albert Einstein>,
        #     <Quote “It is better to be hated for what you are than to be loved for what you are not.”, by André Gide>,
        #     <Quote “I have not failed. I've just found 10,000 ways that won't work.”, by Thomas A. Edison>,
        #     <Quote “A woman is like a tea bag; you never know how strong it is until it's in hot water.”, by Eleanor Roosevelt>,
        #     <Quote “A day without sunshine is like, you know, night.”, by Steve Martin>
        # ]
    