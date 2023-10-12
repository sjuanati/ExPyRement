"""
Iterator = used to get the next value
Iterable = used to go over all the values of an iterator

__iter__ = returns an iterator object, which defines a __next__ method
__next__ = gets the next value from an iterator object. E.g.: when using a loop
__len__ = returns the number of items in the object when called by the built-in len() function on an instance of the class
__getitem__ = allows an object to be indexed with the square bracket notation. E.g.: obj[3] 
"""


class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    # iterator
    def __next__(self):
        if self.number < 5:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()

    # iterable
    def __iter__(self):
        return self


class AnotherIterable:
    def __init__(self):
        self.cars = ["Cupra", "Audi"]

    # A class with just __len__ and without __getitem__ is not considered iterable.
    def __len__(self):
        return len(self.cars)

    # A class with __getitem__ (and without __iter__) is considered iterable, even without __len__
    def __getitem__(self, i):
        return self.cars[i]


def test():
    gen = FirstHundredGenerator()
    print(next(gen))  # prints 0
    print(next(gen))  # prints 1
    print("---")
    for num in gen:  # prints 2 to 4. It would fail without the __iter__ method
        print(num)

    iter = AnotherIterable()
    print(len(iter))  # prints the length of the list
    print(iter[0])  # prints item 0 of the list

    # this is a list comprehension
    nums_list = [x for x in [1, 2, 3, 4]]

    # this is a generator comprehension, NOT a tuple comprehension
    nums_gen = (x for x in [1, 2, 3, 4])
    print(next(nums_gen))

    # this is a tuple (there is no "tuple comprehension" per se in Python)
    nums_tuple = tuple(x for x in [1, 2, 3, 4])
    print(nums_tuple)

    # FILTER returns a generator!
    # filters are useful if we have the function implemented (and can't be done with lambda)
    friends = ["Sergi", "Mat", "Sara", "Lola"]
    friends_with_s = filter(lambda friend: friend.startswith("S"), friends)
    print(friends_with_s)  # returns a filter object
    print(list(friends_with_s))  # returns ['Sergi', 'Sara']
    print(list(friends_with_s))  # returns [] !!! generator already iterated

    # the same generator with comprehension
    # in this case it's faster than the filter, because doesn't need the lambda function
    also_friends_with_s = (friend for friend in friends if friend.startswith("S"))
    print(list(also_friends_with_s))  # returns ['Sergi', 'Sara']
    print(list(also_friends_with_s))  # returns []

    # MAP returns a generator
    friends_lower = map(lambda friend: friend.lower(), friends)
    print(list(friends_lower))

    # the same generator with comprehension
    also_friends_lower = (friend.lower() for friend in friends)
    print(list(also_friends_lower))

