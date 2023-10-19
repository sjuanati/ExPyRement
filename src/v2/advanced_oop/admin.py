from user import User
from saveable import Saveable
# from database import Database


class Admin(User, Saveable):
    def __init__(self, username, password, access):
        super().__init__(username, password)
        self.access = access

    def __repr__(self) -> str:
        return f"<Admin {self.username}, access {self.access}>"

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "access": self.access,
        }

    # def save(self):
    #     Database.insert(self.to_dict())
    """
    self.save() will be searched:
    1) in Admin
    2) then in User
    3) then in Saveable, where it will be found
    """