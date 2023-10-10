from typing import Any

# advice: include __repr__ & __str__ on every class


class Garage:
    def __init__(self) -> None:
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, index):
        return self.cars[index]

    # when coding or debugging (code oriented description)
    def __repr__(self) -> str:
        return f"<Garage {self.cars}>"

    # for printing the object (user oriented description)
    def __str__(self) -> str:
        return f"Garage with {len(self)} cars"

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)
    
class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

def test():
    my_student = {"name": "Sergi Juanati", "grades": [70, 88, 90, 99, 100]}

    cupra = Garage()
    cupra.cars.append("Leon")
    cupra.cars.append("Formentor")

    print(len(cupra))
    print(cupra[1])
    print(cupra)
