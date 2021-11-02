import math
from random import randint
import pygame


FPS = 30

RED = 0xFF0000

WHITE = 0xFFFFFF
GREY = 0x7D7D7D

WIDTH = 800
HEIGHT = 600

number_of_targets = 2
targets = []
sc = 0 
class Ball:
    def __init__(self, screen: pygame.Surface, sc):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = 40
        self.y = 450
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.live = 300
    
    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.vy -= 2
        self.x += self.vx
        self.y -= self.vy

    def collision_walls(self):
        """
        Отражение от стенок
        """
        if self.x + self.vx >= WIDTH - self.r :
            self.vx = -0.9 * self.vx
            self.x += self.vx + 2*(WIDTH - self.r - self.x)

        elif self.y + self.vy >= HEIGHT - self.r :
            self.vy = -0.9 * self.vy
            self.y += self.vy + 2*(HEIGHT -self.r - self.y)

        elif self.x + self.vx <= self.r :
            self.vx = -0.9 * self.vx
            self.x += self.vx + 2*(self.r - self.x)
    
        elif self.y + self.vy <= self.r :
            self.vy = -0.9 * self.vy
            self.y += self.vy + 2*(self.r - self.y) 
   
    def draw(self):
        """ Рисует круг """
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r)

    def hittest(self, obj, sc):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (obj.x - self.x)**2 + (obj.y - self.y)**2 < (obj.r + self.r)**2 :
            return True
        else:
            return False

        


class Gun:
    def __init__(self, screen):
        """ Инициализация пушки """
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY

    def fire2_start(self, event):
        """ Начало прицеливания """
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen, sc)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        """ Рисует пушку """
        pygame.draw.line(self.screen, self.color, (20, 450),
                         (2 * self.f2_power * math.cos(self.an) + 30,
                          2 * self.f2_power * math.sin(self.an) + 450), 20)

    def power_up(self):
        """ Пушка готовится к выстрелу """
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target(Ball):
    def __init__(self, screen, sc):
        """
        Инициализация новой цели
        """
        super().__init__(screen, sc)
        self.x = randint(600, 780)
        self.y = randint(300, 550)
        self.r = randint(8, 50)
        self.vx = randint(-4, 4)
        self.vy = randint(-4, 4)
        self.points = 0
        self.live = 1
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
        targets.append(self)

             

pygame.init()
font = pygame.font.SysFont(None, 60)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []

clock = pygame.time.Clock()
gun = Gun(screen)
targets = [Target(screen, sc) for i in range(number_of_targets) ]

finished = False


while not finished:
    screen.fill(WHITE)
    gun.draw()
    for target in targets:
        target.draw()
        target.move()
        target.collision_walls()
    for b in balls:
        b.draw()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
    for b in balls:
        b.draw()
        b.move()
        b.collision_walls()
        for target in targets:
            if b.hittest(target, sc) and target.live:
                target.live = 0
                targets.pop()
                target = Target(screen, sc)
                sc +=1
    text_score = font.render('Score: ' + str(sc), True, (255, 0, 255), (255, 255, 255))
    screen.blit(text_score, (10, 10))
    pygame.display.update()
    gun.power_up()
  
pygame.display.flip()
    
f = open('text.txt', 'a+')
print('Enter Your Name: ')
name = input()
f.write( 'Name: ' + str(name))
f.write(', Score: ' + str(sc))
f.write('\n')
f.close()
    
pygame.quit()
