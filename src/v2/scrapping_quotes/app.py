import requests

from v2.scrapping_quotes.pages.quotes_page import QuotesPage

def test():
    # get the entire httml content of the page
    page_content = requests.get('https://quotes.toscrape.com/').content
    page = QuotesPage(page_content)
    for quote in page.quotes:
        print(quote)