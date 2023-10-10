import json

path = "src/v2/filez/"


def rw():
    """read & write files"""
    # read filez
    my_read_file = open(path + "filez.txt", "r")
    file_content = my_read_file.read()
    print(file_content)
    my_read_file.close()

    # (over)write filez
    msg = input("Write smtg to the file: ")
    my_write_file = open(path + "filez.txt", "w")
    my_write_file.write(msg)
    my_write_file.close()


def friends_list():
    """
    Ask the user for a list of 3 friends
    For each friend, we'll tell the user whether they are nearby (from people.txt)
    For each nearby friend (from people.txt), we'll save their name to 'nearby_friends.txt'
    """
    friends_nearby = [input(f"Enter friend {i+1}: ").title() for i in range(3)]

    with open(path + "people.txt", "r") as file:
        people = [line.strip() for line in file.readlines()]

    with open(path + "friends_nearby.txt", "w") as file:
        for person in people:
            # if person in friends_nearby:
            if person.lower() in (friend.lower() for friend in friends_nearby):
                file.write(person + "\n")


def friends_set():
    """same as friends_list() but using sets"""
    friends_nearby = set(
        [
            name.strip().title()
            for name in input(f"Enter 3 friends separated by commas: ").split(",")
        ]
    )

    with open(path + "people.txt", "r") as file:
        people = set([line.strip() for line in file.readlines()])

    with open(path + "friends_nearby.txt", "w") as file:
        friends = friends_nearby.intersection(people)
        for friend in friends:
            file.write(friend + "\n")


def csv_filez():
    """read csv file and show contents"""
    # open csv file ignoring the 1st line
    with open(path + "filez.csv", "r") as file:
        lines = file.readlines()
        students = [line.strip().split(",") for line in lines[1:]]
        for student in students:
            name = student[0].title()
            age = int(student[1])
            university = student[2].title()
            degree = student[3].capitalize()
            print(f"{name} is {age}, {degree} at {university}")


def read_json():
    """read json file"""
    try:
        with open(path + "friends1.json", "r") as file:
            file_contents = json.load(file)
            print(file_contents)
            print(file_contents["friends"][0]["name"])
    except FileNotFoundError as e:
        print(f"File name {e.filename} not found")


def write_json():
    """write to json file"""
    # convert string into json
    new_car = '[{"make": "BMW", "model": "M3"}]'
    new_car_json = json.loads(new_car)

    # add json element into existing json list
    # @dev: an object such as ["key":"value"] is considered a JSON element
    cars = [{"make": "Cupra", "model": "Formentor"}, {"make": "Audi", "model": "RS3"}]
    cars.extend(new_car_json)

    # write to json file
    with open(path + "cars.json", "w") as file:
        json.dump(cars, file)


def test():
    # friends_list()
    # friends_set()
    # csv_filez()
    read_json()
    # write_json()
