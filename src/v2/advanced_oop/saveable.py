from abc import ABCMeta, abstractmethod
from database import Database


# quite equivalent to Interface in TypeScript, except that it's
# defining the save() function
class Saveable(metaclass=ABCMeta):
    """force subclass to implement to_dict"""

    def save(self):
        Database.insert(self.to_dict())

    @abstractmethod
    def to_dict(self):
        pass
