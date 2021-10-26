import pygame
import math
import sys
from random import randint
from pygame.draw import *

pygame.init()
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
PEACH = (255, 185, 145)


FPS = 30
Height = 800
Width = 1400
screen = pygame.display.set_mode((Width, Height))
screen.fill(PEACH)
font = pygame.font.Font(None, 60)

n_balls = 10
s_balls = 0

score = 0
missed = 10

class Normal_Ball:
    """
    
    """   
    def __init__(self, x, y, speedx, speedy, color, r):
        self.x = x
        self.y = y
        self.speedx = speedx
        self.speedy = speedy
        self.color = color
        self.r = r
        
    def draw(self):
        """
        Рисует глаз с рандомным цветом
        """
        circle(screen, WHITE, (self.x, self.y), self.r)
        circle(screen, self.color, (self.x, self.y), self.r//2)
        circle(screen, BLACK, (self.x, self.y), self.r//4)

    def move(self):
        """
        Равномерное прямолинейное движение
        """
        self.x += self.speedx
        self.y += self.speedy

    def collision_walls(self):
        """
        Столкновение от стенок со случайным трением
        """
        if self.x + self.r + 10 >= Width or self.x - self.r - 10 <=0 :
            self.speedx = -self.speedx
            self.speedy += randint(-4, 4)
        if self.y + self.r + 10 >= Height or self.y - self.r - 10 <=0 :
            self.speedy = -self.speedy
            self.speedx += randint(-4, 4)

class Special_Ball:
    """

    """
    def __init__(self, x, y, speedx, speedy, color, phi, omega, r):
        self.x = x
        self.y = y
        self.speedx = speedx
        self.speedy = speedy
        self.color = color
        self.phi = phi
        self.omega = omega
        self.r = r

    def draw(self):
        """
        Рисует черный круг
        """
        circle(screen, BLACK, (self.x, self.y), self.r)
    
    def move(self):
        """
        Прецессия
        """
        self.phi += self.omega % 100
        self.speedx += self.r * self.omega % 55 * math.cos(self.phi)
        self.speedy += self.r * self.omega % 55 * math.sin(self.phi)
        self.y += self.speedy//1
        self.x += self.speedx//1

    def collision_walls(self):
        """
        Отражение от стенок с ограничением по скорости
        """
        if self.x + self.speedx >= Width - self.r :
            self.speedx = -self.speedx
            #self.speedy += randint(-3,3)
            self.x += self.speedx + 2*(Width - self.r - self.x)
            if self.speedx > 10:
                self.speedx = 10
            if self.speedy > 10:
                self.speedy = 10

        elif self.y + self.speedy >= Height - self.r :
            self.speedy = -self.speedy
            #self.speedx += randint(-3,3)
            self.y += self.speedy + 2*(Height -self.r - self.y)
            if self.speedx > 10:
                self.speedx = 10
            if self.speedy > 10:
                self.speedy = 10

        elif self.x + self.speedx <= self.r :
            self.speedx = -self.speedx
            #self.speedy += randint(-3, 3)
            self.x += self.speedx + 2*(self.r - self.x)
            if self.speedx > 10:
                self.speedx = 10
            if self.speedy > 10:
                self.speedy = 10
    
        elif self.y + self.speedy <= self.r :
            self.speedy = -self.speedy
            #self.speedx += randint(-3, 3)
            self.y += self.speedy + 2*(self.r - self.y)
            if self.speedx > 10:
                self.speedx = 10
            if self.speedy > 10:
                self.speedy = 10
        
def click_n(score, pos, balls):
    """
    changing the score
    """
    for i in range(len(balls) - 1, -1, -1):
        if (pos[0] - balls[i].x) ** 2 + (pos[1] - balls[i].y) ** 2 <= balls[i].r ** 2:
            score += 1
            normal_balls.pop(i)
    return score

def click_s(score, pos, balls):
    """
    changing the score
    """
    for i in range(len(balls) - 1, -1, -1):
        if (pos[0] - balls[i].x) ** 2 + (pos[1] - balls[i].y) ** 2 <= balls[i].r ** 2:
            score += 10
            special_balls.pop(i)
    return score

normal_balls = [Normal_Ball(randint(100, 1300), randint(100, 700), randint(-4,4), randint(-4,4),
                    (randint(0,255), randint(0, 255), randint(0, 255)), randint(20, 50)) for i in range(n_balls)]

special_balls = [Special_Ball(randint(100, 1200), randint(100, 700), randint(0,0), randint(0,0),
                              (randint(0,255), randint(0, 255), randint(0, 255)),
                              randint(1,2), randint(0,20), randint(30, 40)) for i in range(s_balls)]



end = ''

while end == '':
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            new_score = click_n(score, event.pos, normal_balls) #+ click_s(score, event.pos, special_balls)
            if score < new_score:
                score = new_score
                if score >= n_balls: #+ 10*s_balls:
                    end = 'You Won!'
            else:
                missed -= 1
                if missed == 0:
                    end = 'Wasted!'

    clock.tick(FPS)
    screen.fill(PEACH)

    text_score = font.render('Score: ' + str(score), True, (255, 255, 255))
    text_missed = font.render('Health points: ' + str(missed), True, (255, 255, 255))
    screen.blit(text_score, (10, 10))
    screen.blit(text_missed, (10, 60))

    
    for ball in special_balls:
        ball.draw()
        ball.collision_walls()
        ball.move()
        
    for ball in normal_balls:
        ball.draw()
        ball.collision_walls()
        ball.move()
    pygame.display.update()

text_game_over = font.render(end, True, (255, 0, 0))
screen.blit(text_game_over, (Width // 2 - 80, Height // 2 - 20))


while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
    clock.tick(FPS)

    pygame.display.flip()
    
    f = open('text.txt', 'a+')
    print('Enter Your Name: ')
    name = input()
    f.write( 'Name: ' + str(name))
    f.write(', Score: ' + str(score))
    f.write('\n')
    f.close()   
