import turtle
import numpy as np
turtle.shape('turtle')
turtle.speed(500)
for i in range(3):
  for i in range(360):
    turtle.forward(1)
    turtle.left(1)
  for i in range(360):
    turtle.forward(1)
    turtle.right(1)
  turtle.left(120)
