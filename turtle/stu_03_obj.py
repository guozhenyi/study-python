from turtle import Turtle
from random import random

t = Turtle()

t.pensize(10)
t.color("red")

t.screen.title("turtle demo")
t.screen.bgcolor("orange")

for i in range(100):
    steps = int(random() * 100)
    angle = int(random() * 360)
    t.right(angle)
    t.forward(steps)

# t.screen 是 Turtle 实例所在的 Screen 的实例；它是与海龟一起自动创建的。
t.screen.mainloop()
