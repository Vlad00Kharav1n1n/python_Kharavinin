import pygame
from pygame.draw import *
from math import pi

pygame.init()
FPS=30
BLACK = (  0,   0,   0)
PEACH = (255, 185, 145)
EASY = (50,50,50)
WHITE = (255,255,255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
screen = pygame.display.set_mode((1500, 800))
screen.fill(PEACH)

#Бамбук
def bambuk(x,y,z):
    pygame.draw.line(screen, GREEN, [100*z + x, 150*z + y],[ 122*z + x, 115*z + y], 3*z)
    pygame.draw.polygon(screen, GREEN, [[122*z + x,115*z + y], [128*z + x, 102*z + y], [160*z + x,100*z + y]])
    pygame.draw.polygon(screen, GREEN, [[122*z + x,115*z + y], [132*z + x, 115*z + y], [150*z + x,150*z + y]])
    pygame.draw.line(screen, GREEN, [90*z + x, 200*z + y],[98*z + x, 152*z + y], 4*z)
    pygame.draw.line(screen, GREEN, [88*z + x, 255*z+y], [90*z + x, 202*z + y], 6*z)
    pygame.draw.line(screen, GREEN, [93*z + x, 202*z + y], [130*z + x, 180*z + y], 4*z)
    pygame.draw.line(screen, GREEN, [131*z + x, 180*z + y],[170*z + x, 175*z + y], 3*z)
    pygame.draw.line(screen, GREEN, [97*z + x, 150*z + y], [70*z + x, 120*z + y], 3*z)
    pygame.draw.polygon(screen, GREEN, [[170*z + x,175*z + y], [179*z + x, 177*z + y], [180*z + x,220*z + y]])
    pygame.draw.polygon(screen, GREEN, [[170*z + x, 172*z + y], [173*z + x, 163*z + y], [205*z + x,162*z + y]])
    pygame.draw.polygon(screen, GREEN, [[155*z + x, 178*z + y], [165*z + x, 180*z + y], [162*z + x,219*z + y]])
    pygame.draw.polygon(screen, GREEN, [[70*z + x, 120*z + y], [60*z + x, 153*z + y], [62*z + x,130*z + y]])
    

   
def panda(r,t):
    #Лицо
    pygame.draw.circle(screen, WHITE, [750+r, 400+t], 100)
    pygame.draw.ellipse(screen, EASY, [708+r, 380+t, 25, 40])
    pygame.draw.ellipse(screen, BLACK, [710+r, 385+t, 18, 18])
    pygame.draw.ellipse(screen, EASY, [778+r, 380+t, 25, 40])
    pygame.draw.ellipse(screen, BLACK, [780+r, 385+t, 18, 18])
    pygame.draw.circle(screen, BLACK, [677+r, 305+t], 23)
    pygame.draw.circle(screen, BLACK, [823+r, 305+t], 23)
    pygame.draw.polygon(screen, BLACK, [[753+r, 440+t], [743+r,430+t], [763+r, 430+t]])
    pygame.draw.rect(screen, RED, [740+r, 447+t, 30, 30], 0, border_radius=15, border_top_left_radius=0,
    border_top_right_radius=0)
    #Тело
    pygame.draw.ellipse(screen, WHITE, [600+r, 450+t, 300, 290])
    pygame.draw.ellipse(screen, EASY, [600+r, 520+t, 40, 80])
    pygame.draw.ellipse(screen, EASY, [610+r, 570+t, 90, 40])
    bambuk(605+r,390+t,1)
    pygame.draw.circle(screen, EASY, [702+r, 585+t], 23)
    pygame.draw.circle(screen, EASY, [696+r, 563+t], 10)
    pygame.draw.ellipse(screen, EASY, [925+r, 460+t, 40, 80])
    pygame.draw.ellipse(screen, EASY, [863+r, 510+t, 90, 40])
    pygame.draw.circle(screen, EASY, [943+r, 450+t], 23)
    pygame.draw.circle(screen, EASY, [917+r, 448+t], 10)
    pygame.draw.circle(screen, EASY, [930+r, 426+t], 10)
    pygame.draw.circle(screen, EASY, [955+r, 426+t], 10)
    pygame.draw.circle(screen, EASY, [970+r, 447+t], 10)
    pygame.draw.ellipse(screen, EASY, [660+r, 700+t, 90, 50])
    pygame.draw.ellipse(screen, EASY, [760+r, 700+t, 90, 50])
    pygame.draw.rect(screen, RED, [740+r, 447+t, 30, 30], 0, border_radius=15, border_top_left_radius=0,
    border_top_right_radius=0)

    
panda(500,0)
panda(-560,0)
bambuk(500,520,1)
bambuk(700,230,2)
bambuk(200,0,3)
bambuk(430,-400,4)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
