MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
# movies = []
movies = [
    {"title": "Alien", "director": "Ridley Scott", "year": "1979"},
    {"title": "Asteroid City", "director": "Wes Anderson", "year": "2023"},
    {"title": "Gattaca", "director": "Andrew Niccol", "year": "1997"},
    {"title": "Trainspotting", "director": "Danny Boyle", "year": "1996"},
]


def add_movie():
    """adding movies"""
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")
    movies.append({"title": title, "director": director, "year": year})


def list_movies(_movies):
    """listing all movies"""
    for movie in _movies:
        print(f'{movie["title"]} by {movie["director"]}, {movie["year"]}')


def list_movies_by_attribute(attr, value):
    """listing all movies by a given attribute"""
    movies_by_attribute = [
        movie for movie in movies if movie[attr].lower() == value.lower()
    ]
    if len(movies_by_attribute) > 0:
        list_movies(movies_by_attribute)
    else:
        print(f"No movies found where {attr} is {value}")


def find_movie():
    """finding movies"""
    if len(movies) > 0:
        available_attributes = movies[0].keys()
        attr = input(
            f"Choose an attribute to find a movie ({', '.join(available_attributes)}): "
        ).lower()
        if attr in available_attributes:
            value = input(f"Choose a value for attribute {attr}: ")
            list_movies_by_attribute(attr, value)
        else:
            print(f"Attribute {attr} not available")
    else:
        print("No movies found")


def test():
    user_options = {"a": add_movie, "l": lambda: list_movies(movies), "f": find_movie}
    selection = input(MENU_PROMPT).lower()
    while selection != "q":
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print("Unknown command. Please try again.")
        selection = input(MENU_PROMPT)
