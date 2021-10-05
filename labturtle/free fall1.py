import turtle as t
from math import sin, cos, pi, sqrt

g=0.25
def vector(move):
    t.goto(t.xcor()+move[0], t.ycor()+move[1])
def dspeed(speed):
    speed[1]-=g
    return speed

width=600
height=300
t.shape('circle')
t.speed(7)
t.pu()
t.goto(-200,-height)
t.pd()
speed = [1,10]
cor = [t.xcor(),t.ycor()]

while True:
    speed=dspeed(speed)
    cor[0]+=speed[0]
    cor[1]+=speed[1]
    t.goto(cor[0],cor[1])
    if t.ycor()<=-height:
        speed[1]=-speed[1]
    if abs(t.xcor())>=width:
        speed[0]=-speed[0]
    if t.ycor()<-height:
        t.exitonclick()
