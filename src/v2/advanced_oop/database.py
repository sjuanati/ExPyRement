class Database:
    # class var, not instance var -> all instances will share the same data
    content = {"users": []}

    @classmethod
    def insert(cls, data):
        cls.content["users"].append(data)

    @classmethod
    def remove(cls, finder):  # finder -> lambda x:x['username'] == 'Sergi'
        cls.content["users"] = [
            user for user in cls.content["users"] if not finder(user)
        ]

    @classmethod
    def find(cls, finder):
        return [user for user in cls.content["users"] if finder(user)]
