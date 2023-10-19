from admin import Admin
from user import User
from database import Database

a = Admin("Sergi", "1234", 3)
b = User("Mat", 'abcd')

# both classes have method save() forced by the abstract class Saveable
users = [a, b]
for user in users:
    user.save()

print(Database.find(lambda x:x['username'] == 'Mat'))
print('----')
print(Database.content)