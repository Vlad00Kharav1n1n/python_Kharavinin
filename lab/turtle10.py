import turtle
turtle.shape('turtle')
turtle.speed(500)
turtle.color('black','yellow')
turtle.begin_fill()
for i in range(36):
  turtle.left(10)
  turtle.forward(20)
turtle.end_fill()
turtle.penup()
turtle.goto(50,150)
turtle.pendown()
turtle.color('black','blue')
turtle.begin_fill()
for i in range(36):
  turtle.left(10)
  turtle.forward(3)
turtle.end_fill()
turtle.penup()
turtle.goto(-65,150)
turtle.pendown()
turtle.color('black','blue')
turtle.begin_fill()
for i in range(36):
  turtle.left(10)
  turtle.forward(3)
turtle.end_fill()
turtle.penup()
turtle.forward(57)
turtle.right(90)
turtle.pendown()
turtle.width(10)
turtle.color('red')
turtle.forward(57)
turtle.penup()
turtle.left(90)
turtle.forward(57)
turtle.pendown()
turtle.right(90)
for i in range(17):
  turtle.right(10)
  turtle.forward(10)
turtle.penup()
turtle.left(90)
turtle.forward(157)
turtle.pendown()