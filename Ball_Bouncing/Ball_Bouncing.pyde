from random import *

xSpeed = 2
xPos = 80
ySpeed = 2
yPos = 20

def setup():
    size(400, 400)
    x=randrange(400)
    y=randrange(400)
    
    
def draw():
    global xSpeed
    global xPos
    global ySpeed
    global yPos
    background(51)
    fill(100)
    ellipse(xPos, yPos, 60, 60)
    xPos += xSpeed
    yPos += ySpeed
    
    
    if xPos > 370:
        #change the x direction
        xSpeed = -2
        
    if xPos < 30:
        #change in other x direction
        xSpeed = 2
        
    if yPos < 30:
        #change in the other x direction
        ySpeed = 2
        
        
    paddle = rect(mouseX, 340, 90, 50)
    
    
    if xPos > mouseX and xPos < mouseX + 90 and yPos > 340: