import random
from turtle import Turtle, Screen


s = Screen()
s.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
speeds = [random.randint(1, 10) for _ in range(6)]
distances = [0] * len(colors)
turtles = []
END_DISTANCE = 450


def create_turtles():
    for i in range(6):
        turtle = Turtle()
        turtle.shape("turtle")
        turtle.color(colors[i])
        turtle.penup()
        turtle.goto(-200, -130 + i * 50)
        turtles.append(turtle)


def start_race(user_bet):
    while max(distances) < END_DISTANCE:
        for i in range(0, 6):
            t = turtles[i]
            if distances[i] + speeds[i] >= END_DISTANCE:
                _, y = t.pos()
                t.goto(250 - 15, y)
                distances[i] += speeds[i]
                check_winner(user_bet, colors[i])
                break
            t.forward(speeds[i])
            distances[i] += speeds[i]


def check_winner(user_bet, color_winner):
    msg = "you won" if user_bet == color_winner else "you lost"
    print(f"{msg}!!, the {color_winner} turtle was the fastest.")


def test():
    s.setup(width=500, height=400)
    user_bet = s.textinput(title="guess", prompt="who is going to win?")
    create_turtles()
    start_race(user_bet)
    s.exitonclick()
