#Makeda Joseph
#03/22?2017



import turtle



def drawStem(tristan):
    tristan.color("blue")
    tristan.left(35)
    tristan.forward(50)

def drawPetal(tristan,c):
    tristan.color(c)
    tristan.lt(55)
    tristan.fd(40)
    tristan.lt(65)
    tristan.fd(50)
    tristan.lt(75)
    tristan.fd(60)
    
 


def main():
	myWin = turtle.Screen()     		#The graphics window
	tristan = turtle.Turtle()		#Tristan will be our turtle for this program
	drawStem(tristan)			#Draw a green stem 	
	for i in range(20):
		drawPetal(tristan,"blue")	#Draws a blue petal for our flower
		drawPetal(tristan,"purple")	#Draws a purple petal for our flower
	myWin.exitonclick()         		#Close the window when clicked	

main()
