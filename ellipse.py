import turtle
     
# rad 
rad= int (input ('Nhập bán kính hình elip: '))
i=0

while i<2:
    turtle.circle(rad,90)
    turtle.circle(rad//2,90)
    i+=1
 
turtle.done()