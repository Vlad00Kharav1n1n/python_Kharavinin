import pygame
import sys
from random import randint
from pygame.draw import *
"""
Можно сделать овал на которм будут летать части лица
и по тому как хорошо они лягут при нажатии от идеала
начисляются баллы
"""

pygame.init()
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
PEACH = (255, 185, 145)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255, 0,   0)
YELLOW = (255 ,255 ,0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

FPS = 50
Height = 800
Width = 1400
screen = pygame.display.set_mode((Width, Height))

number_of_eyes = randint(7, 40)

params = []
for i in range(number_of_eyes):
    params.append([randint(200, 1100), randint(200, 600),
    randint(30, 80), COLORS[randint(0, 5)],
    randint(-6, 6), randint(-6, 6)])

##массив переменных для шаров
##Координата по x - params[i][0]
##Координата по y - params[i][1]
##Радиус - params[i][2]
##Цвет - params[i][3]
##Скорость по x - params[i][4]
##Скорость по y - params[i][5]

screen.fill(PEACH)

def new_eye(x, y, r, color):
    '''
    рисует новый шарик
    param: x - положение центра по x
    param: y - положение центра по y
    param: r - радиус
    param: color - цвет
    '''
    circle(screen, WHITE, (x, y), r)
    circle(screen, color, (x, y), r//2)
    circle(screen, BLACK, (x, y), r//4)

run = True

counter = 0
## счетчик очков

while run:
    clock.tick(FPS)
 
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            run = False

        for i in range(number_of_eyes):
            if event.type == pygame.MOUSEBUTTONDOWN and(event.pos[0]-params[i][0])**2 + (event.pos[1]-params[i][1])**2 <=(params[i][2]//4)**2:
                counter +=10
            elif event.type == pygame.MOUSEBUTTONDOWN and(event.pos[0]-params[i][0])**2 + (event.pos[1]-params[i][1])**2 <=(params[i][2]//2)**2:
                counter +=5
            elif event.type == pygame.MOUSEBUTTONDOWN and(event.pos[0]-params[i][0])**2 + (event.pos[1]-params[i][1])**2 <=params[i][2]**2:
                counter +=1

    for i in range(number_of_eyes):
        params[i][0] += params[i][4]
        params[i][1] += params[i][5]
    ##Перемещение на величину скорости

    for i in range(number_of_eyes):
        if params[i][0] + params[i][2] + 10 >= Width or params[i][0] - params[i][2] - 10 <=0:
            params[i][4] = -params[i][4]
            params[i][5] += randint(-4,4)
        if params[i][1] + params[i][2] + 10 >= Height or params[i][1] - params[i][2] - 10<=0:
            params[i][5] = -params[i][5]
            params[i][4] += randint(-4,4)
    ##Сохранение нормальной компоненты скорости при отражении
    ##Случайное трение по тангенциальному направлению
    
    f = pygame.font.SysFont('arial', 30)
    screen_text = f.render('Your score: ' + str(counter), 1, RED)
    pos = screen_text.get_rect(topleft=(Width // 14, Height // 10))
    ##Создание поверхности с общим счетом        
    
    screen.fill(PEACH)
    
    for i in range(number_of_eyes):
        new_eye(params[i][0], params[i][1], params[i][2], params[i][3])
    ##Рисование шариков
    
    screen.blit(screen_text, pos) 
    ##Установка поверхности с текстом

    pygame.display.update()
pygame.quit()

