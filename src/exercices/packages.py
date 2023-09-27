from turtle import Turtle, Screen
from prettytable import PrettyTable

def test():
    # turtle

    tom = Turtle()
    tom.shape("turtle")
    tom.color("tomato")
    tom.speed(1)
    tom.forward(100)
    tom.left(40)
    tom.forward(60)
    tom.right(90)
    tom.forward(100)
    my_screen = Screen()
    print(my_screen.canvheight)
    my_screen.exitonclick()

    #prettytable -> https://pypi.org/project/prettytable/
    
    table = PrettyTable()
    table.add_column("First Name", ["Sergi", "Marta", "Mike"])
    table.add_column("Second Name", ["Smith", "Allen", "Richmond"])
    table.align = "l"
    table.align["Second Name"] = "c"
    print(table)
