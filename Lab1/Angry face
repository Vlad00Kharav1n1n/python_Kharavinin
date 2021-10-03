import pygame
from pygame.draw import *
pygame.init()

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
YELLOW = (255,255,0)
FPS = 30
screen = pygame.display.set_mode((700, 700))
screen.fill(WHITE)

pygame.draw.circle(screen, YELLOW, [350, 350], 200)

pygame.draw.line(screen, BLACK, [200, 200], [320,280], 15)
pygame.draw.line(screen, BLACK, [380, 280], [500,200], 15)

pygame.draw.circle(screen, BLACK, [270, 315], 20)
pygame.draw.circle(screen, RED, [270, 315], 45, 25)

pygame.draw.circle(screen, BLACK, [430, 315], 10)
pygame.draw.circle(screen, RED, [430, 315], 45, 35)

pygame.draw.circle(screen, BLACK, [390, 405], 35, 10)
pygame.draw.line(screen, BLACK, [370, 380], [300,410], 10)
pygame.draw.line(screen, BLACK, [410, 425], [350,460], 10)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
