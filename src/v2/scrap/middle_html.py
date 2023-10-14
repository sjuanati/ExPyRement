import re
from bs4 import BeautifulSoup

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

soup = BeautifulSoup(ITEM_HTML, "html.parser")


def find_item_name():
    locator = "article.product_pod h3 a"  # CSS locator
    item_name = soup.select_one(locator).attrs["title"]
    print(f"Product: {item_name}")  # Output: A Light in the Attic


def find_item_link():
    locator = "article.product_pod h3 a"
    item_link = soup.select_one(locator).attrs["href"]
    print(
        f"Link: {item_link}"
    )  # Output: catalogue/a-light-in-the-attic_1000/index.html


def find_item_price():
    locator = "article.product_pod p.price_color"
    item_price = soup.select_one(locator).string
    expression = r"\£([0-9]+\.[0-9]+)"
    price = float(re.search(expression, item_price).group(1))
    print(f"Price: {price}")


def find_item_stars():
    # option 1 -> if it was the amount of icon-stars
    # locator = "article.product_pod p.star-rating i.icon-star"
    # stars = len(soup.select(locator))
    # print(f"Stars: {stars}")

    # option 2 -> if it's the "Three"
    locator = "article.product_pod p.star-rating"
    stars = soup.select_one(locator)
    star_classes = [s for s in stars.attrs['class'] if s != "star-rating"]
    if not star_classes:  # If no specific class found (shouldn't happen, but just in case)
        star_classes = 0
    else:
        star_classes = star_classes[0]
    print(f'Stars: {star_classes}')


def test():
    find_item_name()
    find_item_link()
    find_item_price()
    find_item_stars()
