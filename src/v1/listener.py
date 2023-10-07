from turtle import Turtle, Screen


# t = Turtle()
# s = Screen()


def move_forwards(t):
    t.forward(10)


def move_backwards(t):
    t.backward(10)


def turn_left(t):
    t.left(10)


def turn_right(t):
    t.right(10)


def clear(t, s):
    t.clear()
    t.penup()
    t.home()
    t.pendown()
    s.reset()  # This will clear the screen and reset everything to its default state.


def test():
    # if 't' and 's' are declared globally
    """
    s.listen()
    s.onkey(key="w", fun=move_forwards)
    s.onkey(key="s", fun=move_backwards)
    s.onkey(key="a", fun=turn_left)
    s.onkey(key="d", fun=turn_right)
    s.onkey(key="c", fun=clear)
    """
    # if 't' and 's' are declared locally
    t = Turtle()
    s = Screen()
    s.listen()
    s.onkey(key="w", fun=lambda: move_forwards(t))
    s.onkey(key="s", fun=lambda: move_backwards(t))
    s.onkey(key="a", fun=lambda: turn_left(t))
    s.onkey(key="d", fun=lambda: turn_right(t))
    s.onkey(key="c", fun=lambda: clear(t, s))
    s.exitonclick()
