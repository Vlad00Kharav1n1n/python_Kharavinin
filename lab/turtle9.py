import turtle
turtle.shape('turtle')
turtle.speed(500)
for i in range(5):
   turtle.forward(150)
   turtle.left(720/5)
turtle.penup()
turtle.forward(100)
turtle.pendown() 
turtle.speed(500)
for i in range(11):
  turtle.forward(100)
  turtle.left(180-(180/11))
