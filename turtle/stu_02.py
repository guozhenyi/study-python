import turtle as t
from random import random

#
# 随机画个图
#

t.pensize(10)
t.color("blue")

for i in range(100):
    steps = int(random() * 100)
    angle = int(random() * 360)
    t.right(angle)
    t.forward(steps)

t.mainloop()
