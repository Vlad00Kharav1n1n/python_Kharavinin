import turtle
import numpy as np
turtle.shape('turtle')
turtle.speed(5)
r=30
b=3
while b<14:
  turtle.left(180-0.5*(180-360/b))
  for i in range(b):
    turtle.forward(2*(r+(b-3)*10)*np.sin(np.pi/b))
    turtle.left(360/b)
  turtle.right(180-0.5*(180-360/b))
  b +=1
  turtle.penup()
  turtle.forward(10)
  turtle.pendown()
