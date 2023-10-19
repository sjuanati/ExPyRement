"""
ABC: Abstract Base Class
"""
from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    def walk(self):
        print("Walking...")

    # the child classes (dog, monkey) to implement this method
    # If so, class Animal can't be created, but only children classes
    @abstractmethod
    def num_legs(self):
        """Return the number of legs this animal has."""


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def num_legs(self):
        return 4


class Human(Animal):
    def __init__(self, name):
        self.name = name

    def num_legs(self):
        return 2



animals = [Dog('rudolph'), Human('mike')]
for animal in animals:
    print(isinstance(animal, Animal))
    print(animal.num_legs()) # we know all child classes will have legs