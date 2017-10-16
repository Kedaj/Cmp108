#Makeda Joseph
#02/15/2017



import turtle
import random

chloe = turtle.Turtle()
for i in range(100):
    chloe.forward(25)
    a = random.randrange(180)
    chloe.right(a)
