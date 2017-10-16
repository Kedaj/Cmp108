#Makeda Joseph
#03/15/2017



import turtle

chloe = turtle.Turtle()

x = int(input('Please enter a number:'))
if x %2==0:
    chloe.color("blue")
    chloe.backward(100)
    
else:
    chloe.color("red")
    chloe.forward(100)
