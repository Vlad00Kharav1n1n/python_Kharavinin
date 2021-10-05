import turtle
import numpy as np
turtle.shape('turtle')
turtle.speed(500)
b=10
turtle.left(90)
while b<20:
  for i in range(36):
    turtle.forward(0.5*b)
    turtle.left(10)
  for i in range(36):
    turtle.forward(0.5*b)
    turtle.right(10)
  b+=1
