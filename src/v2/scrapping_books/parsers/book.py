import re
import logging
from v2.scrapping_books.locators.book_locators import BookLocators

logger = logging.getLogger('scraping.book_parser')

class BookParser:
    RATINGS = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

    def __init__(self, parent):
        logger.debug(f'New book parser created.')
        self.parent = parent

    def __repr__(self) -> str:
        return f"<Book {self.name}, €{self.price}, {self.stars} stars>"

    @property
    def name(self):
        locator = BookLocators.NAME
        return self.parent.select_one(locator).attrs["title"]

    @property
    def link(self):
        locator = BookLocators.LINK
        return self.parent.select_one(locator).attrs["href"]

    @property
    def price(self):
        locator = BookLocators.PRICE
        item_price = self.parent.select_one(locator).string
        expression = r"\£([0-9]+\.[0-9]+)"
        price = re.search(expression, item_price).group(1)
        return float(price)

    @property
    def stars(self):
        locator = BookLocators.STARTS
        stars = self.parent.select_one(locator)
        star_classes = [s for s in stars.attrs["class"] if s != "star-rating"]
        if (
            not star_classes
        ):  # If no specific class found (shouldn't happen, but just in case)
            star_classes = 0
        else:
            star_classes = star_classes[0]
        # @dev: dict.get() returns None or default if key is not found (instead of key error)
        return self.RATINGS.get(star_classes, -1)


"""
Book received as 'parent: 
<article class="product_pod">
        <div class="image_container">
                <a href="catalogue/a-light-in-the-attic_1000/index.html"><img alt="A Light in the Attic"
                                class="thumbnail" src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" /></a>
        </div>
        <p class="star-rating Three">
                <i class="icon-star"></i>
                <i class="icon-star"></i>
                <i class="icon-star"></i>
                <i class="icon-star"></i>
                <i class="icon-star"></i>
        </p>
        <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a>
        </h3>
        <div class="product_price">
                <p class="price_color">£51.77</p>
                <p class="instock availability">
                        <i class="icon-ok"></i>

                        In stock

                </p>
                <form>
                        <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">Add to
                                basket</button>
                </form>
        </div>
</article>
"""
