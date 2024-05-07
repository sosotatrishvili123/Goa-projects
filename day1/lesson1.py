from turtle import *


# we want to paint hous
#step 1: draw a square
width(7)
color("purple")
speed(20)


forward(200)
left(90)
forward (200)
left(90)
forward(200)

left(90)
forward(200)
left(90)


#end of squre

# drawing a door

forward(70)
color("yellow")
begin_fill
left(90)
forward(120)       #height of thw door
right(90)
forward(60)
right(90)
forward(120)
end_fill

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


# we want to drawing windows

color("purple")
left(30)
forward(60)
left(90)
forward(60)
left(90)
forward(30)
left(90)
forward(60)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(60)
left(90)
forward(30)
left(90)
forward(60)
left(90)
forward(30)

left(90)
left(90)
forward(170)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(30)
right(90)
forward(60)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(60)
right(90)
forward(30)
right(90)
forward(60)
left(90)
forward(150)







exitonclick()