import random
from turtle import Turtle, Screen
from prettytable import PrettyTable


def draw_square(t: Turtle):
    for _ in range(4):
        t.forward(80)
        t.left(90)


def draw_dotted_line(t: Turtle):
    for _ in range(6):
        t.forward(8)
        t.penup()
        t.forward(8)
        t.pendown()


def get_random_color():
    """Return a random RGB color."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def draw_polygons(t: Turtle):
    """Draw triangle, square, pentagon, hexagon, heptagon, octagon, decagon."""
    for i in range(3, 11):
        angle = 360 / i
        t.color(get_random_color())
        for i in range(i):
            t.forward(80)
            t.left(angle)


def draw_random_walk(t: Turtle, iterations: int):
    """Walk colorful randomly."""
    directions = [0, 90, 180, 270]
    t.pensize(10)
    for _ in range(iterations):
        t.color(get_random_color())
        t.forward(30)
        t.setheading(random.choice(directions))


def draw_donut(t: Turtle):
    for i in range(0, 360, 5):
        t.color(get_random_color())
        t.circle(100)
        t.setheading(i)


def test():
    t = Turtle()
    s = Screen()

    t.speed("fastest")
    s.colormode(255)

    # draw_square(t)
    # draw_dotted_line(t)
    # draw_polygons(t)
    # draw_random_walk(t, 150)
    draw_donut(t)

    s.exitonclick()

    """
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
    """
