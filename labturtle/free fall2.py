import turtle as t

g=0.5
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
    if speed[1] <= -10:
        speed[1]=10
        cor[1] = - height
    if abs(t.xcor())>=width:
        speed[0]=-speed[0]
