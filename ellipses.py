import turtle
screen = turtle.Screen()

# method to draw ellipse
def draw(rad):
    i=0
  # rad --> radius for arc
    while i<2:
        turtle.circle(rad,90)
        turtle.circle(rad//2,90)
        i+=1
 
# Main Section
# Set screen size
screen.setup(500,500)
 
# Set screen color
screen.bgcolor('black')
 
# Colors
col=['violet','blue','green','yellow','orange','red']
 
# some integers
val=10
ind=0
 
# turtle speed
turtle.speed(100)
 
# loop for multiple ellipse
i=0
while i <36:
     
    # oriented the ellipse at angle = -val
    turtle.seth(-val)
     
    # color of ellipse
    turtle.color(col[ind])
     
    # to access different color
    if ind==5:
        ind=0
    else:
        ind+=1
     
    # calling method
    draw(80)
     
    # orientation change
    val+=10

turtle.done()