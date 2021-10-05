import turtle
a = 0
while a < 10:
  turtle.shape('turtle')
  turtle.speed(1)
  for i in range(4):
    turtle.forward(50+20*a)
    turtle.left(90)
  a += 1
  turtle.penup()
  turtle.goto(-10*a, -10*a)
  turtle.pendown()
