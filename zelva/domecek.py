from math import sqrt
from random import randint
from turtle import forward, left, right, exitonclick

def domecek(a):
    c = sqrt(2 * a**2)            # uhlopricka
    d = sqrt(2 * a**2) / 2        # strecha
    left(90)
    forward(a)
    right(90)
    forward(a)
    right(135)
    forward(c)
    left(135)
    forward(a)
    left(90)
    forward(a)
    left(45)
    forward(d)
    left(90)
    forward(d)
    left(90)
    forward(c)
    left(45)
for i in range(10):
    domecek(randint(10, 20))
    right(36)
exitonclick()
