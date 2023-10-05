"""
Captures colors from a picture and draws a number of circles in random colors on a Hirst style
"""

import os
import colorgram
import random
from turtle import Turtle, Screen


def set_position(t: Turtle, y: int):
    t.penup()
    t.goto(-200, y * 50 - 200)
    t.pendown()


def get_colors_from_image():
    print(os.getcwd())  # show current path
    rgb_colors = []
    colors = colorgram.extract("src/exercices/hirst/image.jpg", 30)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        if r + g + b > 650:  # exclulde whitish colors
            continue
        rgb_colors.append((r, g, b))
    return rgb_colors


def draw_dots_line(t: Turtle, rgb_colors):
    for _ in range(10):
        t.width(0)
        t.hideturtle()
        t.fillcolor(random.choice(rgb_colors))
        t.penup()
        t.begin_fill()
        t.circle(10)
        t.end_fill()
        t.forward(40)
        t.pendown()


def test():
    t = Turtle()
    s = Screen()
    t.speed("fastest")
    s.colormode(255)

    rgb_colors = get_colors_from_image()
    for i in range(10):
        set_position(t, i)
        draw_dots_line(t, rgb_colors)

    s.exitonclick()
