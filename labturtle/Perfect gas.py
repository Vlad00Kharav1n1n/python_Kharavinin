import turtle as t
from math import sin, cos, pi, sqrt
from random import *

turtles = 10

def vector(unit, move):
    unit.goto(unit.xcor()+move[0], unit.ycor()+move[1])
             
width = 300
height = 300
    
pool = [t.Turtle(shape='circle') for i in range(turtles)]
for unit in pool:
    unit.pu()
    unit.speed(0)
    unit.goto(randint(-width, width), randint(-height, height))
    unit.pd()
    unit.pencolor((random(), random(), random()))

speeds = []
for i in range(turtles):
    speeds.append([randint(-11, 11), randint(-11, 11)])

while True:
    for i in range(turtles):     
        vector(pool[i], speeds[i])
        if abs(pool[i].xcor()) >= width:
            speeds[i][0] = -speeds[i][0]
        if abs(pool[i].ycor()) >= height:
            speeds[i][1] = -speeds[i][1]
