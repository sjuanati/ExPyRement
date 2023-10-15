

def print_best_books(books):
    # show 10 books sorted by starts attribute in descending order (*-1)
    best_books = sorted(books, key=lambda x: x.stars * -1)[:10]
    for book in best_books:
        print(book)

def print_cheapest_books(books):
    # show 10 books sorted by price in ascending order
    cheapest_books = sorted(books, key=lambda x:x.price)[:10]
    for book in cheapest_books:
        print(book)

def print_best_cheapest_books(books):
    # show 10 books sorted by starts (desc) and price (asc)
    # @dev: first sorts by starts, then sorts by price
    best_cheapest_books = sorted(books, key=lambda x: (x.stars * -1, x.price))[:10]
    for book in best_cheapest_books:
        print(book)
