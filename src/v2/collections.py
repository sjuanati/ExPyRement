from collections import Counter, defaultdict, OrderedDict, namedtuple, deque


def counter():
    device_temperatures = [23.5, 23.0, 23.0, 24.0, 23.5, 23.0, 23.5]
    temperature_counter = Counter(
        device_temperatures
    )  # Counter({23.5: 3, 23.0: 3, 24.0: 1})
    print(temperature_counter[23.5])  # counts how many records has 23.5º


def default_dict():
    coworkers = [("Marc", "MIT"), ("John", "ESADE"), ("Marc", "IESE")]
    alma_maters = defaultdict(list)

    for coworker, university in coworkers:
        alma_maters[coworker].append(university)

    print(
        alma_maters
    )  # defaultdict(<class 'list'>, {'Marc': ['MIT', 'IESE'], 'John': ['ESADE']})
    print(alma_maters["Marc"])  # ['MIT', 'IESE']


def default_dict2():
    my_company = "Olivetti"
    coworkers = ["Anna", "Albert", "Oriol"]
    other_coworkers = [("Marc", "Apple Inc"), ("Lea", "Google Inc")]
    coworker_companies = defaultdict(lambda: my_company)

    for person, company in other_coworkers:
        coworker_companies[person] = company

    print(coworker_companies[coworkers[0]])  # Olivetti
    print(coworker_companies["Marc"])  # Apple Inc


def ordered_dict():
    """Items will keep the order in which they were added"""
    """Since Python 3.7 dictionaries keep the order"""

    od = OrderedDict()
    od["Sergi"] = 10
    od["Mat"] = 8
    od["Lucy"] = 7
    print(od)  # Output: OrderedDict({'Sergi': 10, 'Mat': 8, 'Lucy': 7})

    od.move_to_end("Sergi")
    print(od)  # Output: OrderedDict({'Mat': 8, 'Lucy': 7, 'Sergi': 10})

    od.popitem()
    print(od)  # Output: OrderedDict({'Mat': 8, 'Lucy': 7})


def names_tuple():
    # Defining and Using a namedtuple
    Person = namedtuple("Person", ["name", "age"])
    alice = Person(name="Alice", age=25)
    print(alice)  # Output: Person(name='Alice', age=25)
    print(alice.name)  # Output: Alice
    print(alice.age)  # Output: 25

    # Converting a namedtuple to a Dictionary
    bob = Person(name="Bob", age=30)
    bob_dict = bob._asdict()
    print(bob_dict)  # Output: OrderedDict([('name', 'Bob'), ('age', 30)])

    # Replacing fields
    charlie = bob._replace(name="Charlie")
    print(charlie)  # Output: Person(name='Charlie', age=30)


def de_que():
    friends = deque(('Sergi', 'Mat', 'Gemma'))
    friends.append('Marc')
    friends.appendleft('Lucy')
    print(friends)
    friends.pop()
    friends.popleft()
    print(friends)

def test():
    counter()
    default_dict()
    default_dict2()  # maybe not too common
    ordered_dict()
    names_tuple()  # bah
    de_que()
