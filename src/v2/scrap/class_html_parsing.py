import re
from bs4 import BeautifulSoup
# webpage: https://books.toscrape.com/

ITEM_HTML = """
<html>
<head></head>
<body>
    <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
        <article class="product_pod">
            <div class="image_container">
                <a href="catalogue/a-light-in-the-attic_1000/index.html"><img
                        src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic"
                        class="thumbnail"></a>
            </div>
            <p class="star-rating Three">
                <i class="icon-star"></i>
                <i class="icon-star"></i>
                <i class="icon-star"></i>
                <i class="icon-star"></i>
                <i class="icon-star"></i>
            </p>
            <h3>
                <a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">
                    A Light in the ...
                </a>
            </h3>
            <div class="product_price">
                <p class="price_color">£51.77</p>
                <p class="instock availability">
                    <i class="icon-ok"></i>
                    In stock
                </p>
                <form>
                    <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to
                        basket</button>
                </form>
            </div>
        </article>
    </li>
</body>
</html>
"""


class ParsedItemLocators:
    """
    Locators for an item in the HTML page.
    This allows to easily see what our code will be looking at as
    well as change it quickly if we notice it is now different.
    """

    NAME_LOCATOR = "article.product_pod h3 a"
    LINK_LOCATOR = "article.product_pod h3 a"
    PRICE_LOCATOR = "article.product_pod p.price_color"
    RATING_LOCATOR = "article.product_pod p.star-rating"


class ParsedItem:
    """
    A class to take in an HTML page (or part of it), and find properties of an item in it
    """

    def __init__(self, page):
        self.soup = BeautifulSoup(page, "html.parser")

    @property
    def name(self):
        locator = ParsedItemLocators.NAME_LOCATOR  # CSS locator
        item_name = self.soup.select_one(locator).attrs["title"]
        return f"Product: {item_name}"  # Output: A Light in the Attic

    @property
    def link(self):
        locator = ParsedItemLocators.NAME_LOCATOR
        item_link = self.soup.select_one(locator).attrs["href"]
        return f"Link: {item_link}"  # Output: catalogue/a-light-in-the-attic_1000/index.html

    @property
    def price(self):
        locator = ParsedItemLocators.PRICE_LOCATOR
        item_price = self.soup.select_one(locator).string
        expression = r"\£([0-9]+\.[0-9]+)"
        price = float(re.search(expression, item_price).group(1))
        return f"Price: {price}"

    @property
    def stars(self):
        # option 1 -> if it was the amount of icon-stars
        # locator = "article.product_pod p.star-rating i.icon-star"
        # stars = len(soup.select(locator))
        # return f"Stars: {stars}"

        # option 2 -> if it's the "Three"
        locator = ParsedItemLocators.RATING_LOCATOR
        stars = self.soup.select_one(locator)
        star_classes = [s for s in stars.attrs["class"] if s != "star-rating"]
        if (
            not star_classes
        ):  # If no specific class found (shouldn't happen, but just in case)
            star_classes = 0
        else:
            star_classes = star_classes[0]
        return f"Stars: {star_classes}"


def test():
    pi = ParsedItem(ITEM_HTML)
    print(pi.name)
    print(pi.link)
    print(pi.price)
    print(pi.stars)
