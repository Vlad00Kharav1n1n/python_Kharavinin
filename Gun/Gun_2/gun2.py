import pygame
import sys
import time
import pygame.font
import math
from random import randint
from pygame.sprite import Group


FPS = 30

RED = 0xFF0000
BLUE = (0, 0, 255)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
DIRTY = (210, 205, 50)


WIDTH = 1200
HEIGHT = 800

rnd_color = (randint(0, 255), randint(0, 255), randint(0, 255))
bg_color = (0, 0, 0)
number_targets = 10
number_enemies = 10


class Gun(pygame.sprite.Sprite):
    """ Класс пушки """
    def __init__(self, screen, x, y):
        """ Инициализация пушки """
        super(Gun, self).__init__()
        self.screen = screen
        self.f_power = 10
        self.f_on = 0
        self.angle = 1
        self.color = DIRTY
        self.image = pygame.image.load('Jaaagan/tank_small.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = x
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.move_right = False
        self.move_left = False
        self.x = self.rect.centerx
        self.y = HEIGHT - 50        
        
    def targetting(self, event):
        """ Прицеливание. Зависит от положения мыши. """
        if event:
            self.angle = math.atan2((event.pos[1]-self.y) , -(event.pos[0] - self.x))
        if self.f_on:
            self.color = RED
        else:
            self.color = DIRTY

    def move(self):
        """ Передвижение пушки """
        if self.move_right and self.rect.right < WIDTH:
            self.center += 2.5
        if self.move_left and self.rect.left > 0:
            self.center -= 2.5
            
        self.rect.centerx = self.center
        self.x = self.rect.centerx
               
    def draw(self):
        """ Рисует пушку """
        self.screen.blit(self.image, self.rect)
        
        pygame.draw.line(self.screen, self.color, (self.x, self.y),
                         (-2 * self.f_power * math.cos(self.angle) + self.x ,
                          2 * self.f_power * math.sin(self.angle) + self.y), 20)
               
    def power_up(self):
        """ Пушка готовится к выстрелу """
        if self.f_on:
            if self.f_power < 100:
                self.f_power += 1.8
            self.color = RED
        else:
            self.color = DIRTY
    
    def fire_start(self, event):
        """ Начало выстрела """
        self.f_on = 1

    def fire_end(self, event):
        """ Выстрел """
        self.f_on = 0
        self.f_power = 10



class Bullet(pygame.sprite.Sprite):
    """ Класс пуль """
    def __init__(self, screen, gun):
        """
        Инициализация пули в позиции пушки
        """
        super(Bullet, self).__init__()
        self.screen = screen

    def move(self):
        """ Перемещение пули по экрану. Движение в поле тяжести """
        self.speedy -= -0.8
        self.y += self.speedy
        self.x -= self.speedx
        self.rect.y = self.y
        self.rect.x = self.x

    def draw(self):
        """ Рисует пулю """
        self.screen.blit(self.image, self.rect)


class Bullet_left(Bullet):
    """ класс левой пули """
    def __init__(self, screen, gun_left):
        """ Инициализация пули в позиции пушки """
        super().__init__(screen, gun_left)
        self.image = pygame.image.load('Jaaagan/bullet_left.png')
        self.rect = self.image.get_rect(center =
                                        (-2 * gun_left.f_power * math.cos(gun_left.angle) + gun_left.x ,
                          2 * gun_left.f_power * math.sin(gun_left.angle) + gun_left.y)  ) 
        self.speedx = gun_left.f_power * math.cos(gun_left.angle) * 0.8
        self.speedy = gun_left.f_power * math.sin(gun_left.angle) * 0.8
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)        


class Bullet_right(Bullet):
    """ класс правой пули """
    def __init__(self, screen, gun_right):
        """ Инициализация пули в позиции пушки """
        super().__init__(screen, gun_right)
        self.image = pygame.image.load('Jaaagan/bullet_right.png')
        self.rect = self.image.get_rect(center =
                                        (-2 * gun_right.f_power * math.cos(gun_right.angle) + gun_right.x ,
                          2 * gun_right.f_power * math.sin(gun_right.angle) + gun_right.y)  ) 
        self.speedx =  gun_right.f_power * math.cos(gun_right.angle) * 0.8
        self.speedy = gun_right.f_power * math.sin(gun_right.angle) * 0.8
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)        


        
       
class Fireball_left(pygame.sprite.Sprite):
    """ класс левых файерболов """
    def __init__(self, screen, gun_left):
        super(Fireball_left, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('Jaaagan/fireball_left.png')
        self.rect = self.image.get_rect(center =
                                        (-2 * gun_left.f_power * math.cos(gun_left.angle) + gun_left.x ,
                          2 * gun_left.f_power * math.sin(gun_left.angle) + gun_left.y)  ) 
        self.speedx = gun_left.f_power * math.cos(gun_left.angle) * 0.8
        self.speedy = gun_left.f_power * math.sin(gun_left.angle) * 0.8
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def move(self):
        """ Перемещение файербола по экрану. Равномерное прямолинейное движение """
        self.y += self.speedy
        self.x -= self.speedx
        self.rect.y = self.y
        self.rect.x = self.x

    def draw(self):
        """ Рисует пулю """
        self.screen.blit(self.image, self.rect)

class Fireball_right(pygame.sprite.Sprite):
    """ класс правых файерболов """
    def __init__(self, screen, gun_right):
        super(Fireball_right, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('Jaaagan/fireball_right.png')
        self.rect = self.image.get_rect(center =
                                        (-2 * gun_right.f_power * math.cos(gun_right.angle) + gun_right.x ,
                          2 * gun_right.f_power * math.sin(gun_right.angle) + gun_right.y)  ) 
        self.speedx =  gun_right.f_power * math.cos(gun_right.angle) * 0.8
        self.speedy = gun_right.f_power * math.sin(gun_right.angle) * 0.8
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def move(self):
        """ Перемещение файербола по экрану. Равномерное прямолинейное движение """
        self.y += self.speedy
        self.x -= self.speedx
        self.rect.y = self.y
        self.rect.x = self.x

    def draw(self):
        """ Рисует пулю """
        self.screen.blit(self.image, self.rect)
    

class Target(pygame.sprite.Sprite):
    """ класс целей """
    def __init__(self, screen):
        super(Target, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('Jaaagan/target.png')
        self.rect = self.image.get_rect()
        self.rect.x = randint(WIDTH//3 + 50, 2 * WIDTH//3 - 50)
        self.rect.y = randint(40, HEIGHT//2 - 40)
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.speedx = randint(-4, 4)
        self.speedy = randint(-4, 4)

    def draw(self):
        """ Рисует цель на экране """
        self.screen.blit(self.image, self.rect)

    def move(self):
        """ Перемещает цели по экрану """
        if self.x + self.rect.width >= 4 * WIDTH//5 or self.x - self.rect.width <= WIDTH//5:
            self.speedx = -self.speedx
            self.x +=  self.speedx
            self.rect.x = self.x
        if self.y + self.rect.height >= HEIGHT//2 or self.y - self.rect.height <=0:
            self.speedy = -self.speedy
            self.y +=  self.speedy
            self.rect.y = self.y
        else:
            self.y += self.speedy
            self.x += self.speedx
            self.rect.x = self.x
            self.rect.y = self.y

class Enemy(pygame.sprite.Sprite):
    """ класс мишеней """
    def __init__(self, screen):
        super(Enemy, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('Jaaagan/enemy.png')
        self.rect = self.image.get_rect()
        self.rect.x = randint(WIDTH//3 + 50, 2 * WIDTH//3 - 50)
        self.rect.y = randint(HEIGHT//2 + 40, HEIGHT - 40)
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.speedx = randint(-4, 4)
        self.speedy = randint(-4, 4)

    def draw(self):
        """ Рисует мишень на экране """
        self.screen.blit(self.image, self.rect)

    def move(self):
        """ Перемещает мишень по экрану """
        if self.x + self.rect.width >= 4 * WIDTH//5 or self.x - self.rect.width <= WIDTH//5:
            self.speedx = -self.speedx
            self.x +=  self.speedx
            self.rect.x = self.x
        if self.y + self.rect.height >= HEIGHT or self.y - self.rect.height <= HEIGHT//2:
            self.speedy = -self.speedy
            self.y +=  self.speedy
            self.rect.y = self.y
        else:
            self.speedy += 0.2
            self.y += self.speedy
            self.x += self.speedx
            self.rect.x = self.x
            self.rect.y = self.y        


class Bomb(pygame.sprite.Sprite):
    """ класс бомб """
    def __init__(self, screen):
        """ Инициализация бомб """
        super(Bomb, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('Jaaagan/bomb.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """ Рисует бомбу """
        self.screen.blit(self.image, self.rect)

    def move(self):
        """ Перемещение бомбы по экрану"""
        self.y += 0.2
        self.rect.y = self.y


class Stats():
    """ Отслеживание статистики """
    def __init__(self):
        self.reset_stats()

    def reset_stats(self):
        """ Статистика, изменяющаяся во время игры. Банк информации """
        self.score_left = 0
        self.score_right = 0
        self.life_left = 100
        self.life_right = 100
        self.finished = False
        
class Score():
    """ Вывод игровой информации """
    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 36)
        self.image_score_left()
        self.image_score_right()
        self.image_life_left()
        self.image_life_right()
        
    def image_score_left(self):
        """ Преобразовывает текст левого счета в слой """
        self.score_left_img = self.font.render("Score: " + str(self.stats.score_left), True, RED, (255, 255, 255))
        self.score_left_rect = self.score_left_img.get_rect()
        self.score_left_rect.left = 20
        self.score_left_rect.top = 20
        
    def image_score_right(self):
        """ Преобразовывает текст правого счета в слой """
        self.score_right_img = self.font.render("Score: " + str(self.stats.score_right), True, BLUE, (255, 255, 255))
        self.score_right_rect = self.score_right_img.get_rect()
        self.score_right_rect.right = self.screen_rect.right - 100
        self.score_right_rect.top = 20

    def image_life_right(self):
        """ Создает шкалу правой жизни """
        self.life_right_img = self.font.render("Health: " + str(self.stats.life_right), True, bg_color, (255, 255, 255))
        self.life_right_rect = self.life_right_img.get_rect()
        self.life_right_rect.right = self.screen_rect.right - 100
        self.life_right_rect.top = 40
        
    def image_life_left(self):
        """ Создает шкалу левой жизни """
        self.life_left_img = self.font.render("Health: " + str(self.stats.life_left), True, bg_color, (255, 255, 255))
        self.life_left_rect = self.life_left_img.get_rect()
        self.life_left_rect.left = 20
        self.life_left_rect.top = 40

    def show(self):
        """ Вывод информации на экран """
        self.screen.blit(self.score_left_img, self.score_left_rect)
        self.screen.blit(self.score_right_img, self.score_right_rect)
        self.screen.blit(self.life_left_img, self.life_left_rect)
        self.screen.blit(self.life_right_img, self.life_right_rect)

def target_army(screen, targets):
    """ Создание армии целей """
    for number in range(number_targets):
        target = Target(screen)
        target.rect.x = target.x
        target.rect.y = target.y
        targets.add(target)
        
def enemy_army(screen, enemies):
    """ Создание армии мишеней """
    for number in range(number_enemies):
        enemy = Enemy(screen)
        enemy.rect.x = enemy.x
        enemy.rect.y = enemy.y
        enemies.add(enemy)
        
def bomb_army(screen, bombs):
    """ Создание армии бомб """
    bomb = Bomb(screen)
    bomb_width = bomb.rect.width
    bomb_height = bomb.rect.height
    for ver_number in range(8):
        for hor_number in range(3):
            bomb = Bomb(screen)
            bomb.x = 2 * bomb_width + bomb_width * hor_number
            bomb.y = bomb_height + bomb_height * ver_number
            bomb.rect.x = bomb.x
            bomb.rect.y = bomb.y
            bombs.add(bomb)
    
    for ver_number in range(8):
        for hor_number in range(3):
            bomb = Bomb(screen)
            bomb.x = WIDTH -(3 * bomb_width + bomb_width * hor_number)
            bomb.y = bomb_height + bomb_height * ver_number
            bomb.rect.x = bomb.x
            bomb.rect.y = bomb.y
            bombs.add(bomb)        


def all_objects_motion(screen, gun_left, gun_right, left_bullets,
                       left_fireballs, right_bullets,
                       right_fireballs, targets, enemies, bombs, score):
    """ Перемещает и отрисовывает все объекты на экране """
    screen.fill(WHITE)
    score.show()
    gun_left.move()
    gun_right.move()
    gun_left.power_up()
    gun_right.power_up()

    gun_left.draw()
    gun_right.draw()    
    
    for bullet in left_bullets:
        if bullet.rect.top >= HEIGHT or bullet.rect.left >= WIDTH:
            left_bullets.remove(bullet)
        else:
            bullet.move()
            bullet.draw()
    for bullet in right_bullets:
        if bullet.rect.top >= HEIGHT or bullet.rect.right <= 0:
            right_bullets.remove(bullet)
        else:
            bullet.move()
            bullet.draw()

    for fireball in right_fireballs:
        if fireball.rect.top >= HEIGHT or fireball.rect.right <= 0:
            right_fireballs.remove(fireball)
        else:
            fireball.move()
            fireball.draw()
    for fireball in left_fireballs:
        if fireball.rect.top >= HEIGHT or fireball.rect.left >= WIDTH:
            left_fireballs.remove(fireball)
        else:
            fireball.move()
            fireball.draw()
            
    for target in targets:
        target.move()
        target.draw()

    for enemy in enemies:
        enemy.move()
        enemy.draw()
    for bomb in bombs:
        if bomb.rect.top >= HEIGHT:
            bombs.remove(bomb)
        else:
            bomb.move()
            bomb.draw()
            
    pygame.display.update()


def external_events(stats, FPS, screen, gun_left, gun_right,
                    left_bullets, right_bullets, left_fireballs,
                    right_fireballs, bombs, targets, enemies):
    """ Обрабатывает внешние события """
    clock = pygame.time.Clock()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stats.finished = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                gun_left.move_right = True
            elif event.key == pygame.K_a:
                gun_left.move_left = True
            elif event.key == pygame.K_LEFT:
                gun_right.move_left = True
            elif event.key == pygame.K_RIGHT:
                gun_right.move_right = True

            elif event.key == pygame.K_LSHIFT:
                gun_left.fire_start(event)
            elif event.key == pygame.K_RSHIFT:
                gun_right.fire_start(event)
       
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                gun_left.move_right = False
            elif event.key == pygame.K_a:
                gun_left.move_left = False
            elif event.key == pygame.K_LEFT:
                gun_right.move_left = False
            elif event.key == pygame.K_RIGHT:
                gun_right.move_right = False

            elif event.key == pygame.K_LSHIFT:
                l_fireball = Fireball_left(screen, gun_left)
                left_fireballs.add(l_fireball)
                gun_left.fire_end(event)
            elif event.key == pygame.K_RSHIFT:
                r_fireball = Fireball_right(screen, gun_right)
                right_fireballs.add(r_fireball)
                gun_right.fire_end(event)
 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                gun_left.fire_start(event)
            if event.button == 3:
                gun_right.fire_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                new_l_bullet = Bullet_left(screen, gun_left)
                left_bullets.add(new_l_bullet)
                gun_left.fire_end(event)
            if event.button == 3:
                new_r_bullet = Bullet_right(screen, gun_right)
                right_bullets.add(new_r_bullet)
                gun_right.fire_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun_left.targetting(event)
            gun_right.targetting(event)

        elif event.type == pygame.USEREVENT:
            target_army(screen, targets)
            enemy_army(screen, enemies)
            bomb_army(screen, bombs)

def collis_target_left_bullet(targets, left_bullets, score, stats):
    """ Обрабатывает столкновения целей и левых пуль """
    collisions = pygame.sprite.groupcollide(targets, left_bullets, True, True)
    if collisions:
        stats.score_left +=10
    score.image_score_left()
        
def collis_target_right_bullet(targets, right_bullets, score, stats):
    """ Обрабатывает столкновения целей и правых пуль """
    collisions = pygame.sprite.groupcollide(targets, right_bullets, True, True)
    if collisions:
        stats.score_right +=10
    score.image_score_right()
        
def collis_enemy_left_bullet(enemies, left_bullets, score, stats):
    """ Обрабатывает столкновения мишеней и левых пуль """
    collisions = pygame.sprite.groupcollide(enemies, left_bullets, True, True)
    if collisions:
        stats.score_left +=15
    score.image_score_left()
        
def collis_enemy_right_bullet(enemies, right_bullets, score, stats):
    """ Обрабатывает столкновения мишеней и правых пуль """
    collisions = pygame.sprite.groupcollide(enemies, right_bullets, True, True)
    if collisions:
        stats.score_right +=15
    score.image_score_right()
        
def collis_bomb_left_bullet(screen, bombs, left_bullets, score, stats):
    """ Обрабатывает столкновения бомб и левых пуль """
    collisions = pygame.sprite.groupcollide(bombs, left_bullets, True, True)
    if collisions:
        stats.score_left +=5
    score.image_score_left()
                
def collis_bomb_right_bullet(bombs, right_bullets, score, stats):
    """ Обрабатывает столкновения бомб и правых пуль """
    collisions = pygame.sprite.groupcollide(bombs, right_bullets, True, True)
    if collisions:
        stats.score_right += 5
    score.image_score_right()
        
def collis_target_left_fireball(targets, left_fireballs, score, stats):
    """ Обрабатывает столкновения целей и левых файерболов """
    collisions = pygame.sprite.groupcollide(targets, left_fireballs, True, False)
    if collisions:
        for targets in collisions.values():
            stats.score_left += 10 * len(targets)
        score.image_score_left()
    
def collis_target_right_fireball(targets, right_fireballs, score, stats):
    """ Обрабатывает столкновения целей и правых файерболов """
    collisions = pygame.sprite.groupcollide(targets, right_fireballs, True, False)
    if collisions:
        for targets in collisions.values():
            stats.score_right += 10 * len(targets)
        score.image_score_right()
    
def collis_enemy_left_fireball(enemies, left_fireballs, score, stats):
    """ Обрабатывает столкновения мишеней и левых файерболов """
    collisions = pygame.sprite.groupcollide(enemies, left_fireballs, True, False)
    if collisions:
        for targets in collisions.values():
            stats.score_left += 15 * len(targets)
        score.image_score_left()
    
def collis_enemy_right_fireball(enemies, right_fireballs, score, stats):
    """ Обрабатывает столкновения мишеней и правых файерболов """
    collisions = pygame.sprite.groupcollide(enemies, right_fireballs, True, False)
    if collisions:
        for targets in collisions.values():
            stats.score_right += 15 * len(targets)
        score.image_score_right()
    
def collis_bomb_left_fireball(bombs, left_fireballs, score, stats):
    """ Обрабатывает столкновения бомб и левых файерболов """
    collisions = pygame.sprite.groupcollide(bombs, left_fireballs, True, False)
    if collisions:
        for targets in collisions.values():
            stats.score_left += 5 * len(targets)
        score.image_score_left()
    
def collis_bomb_right_fireball(bombs, right_fireballs, score, stats):
    """ Обрабатывает столкновения бомб и правых файерболов """
    collisions = pygame.sprite.groupcollide(bombs, right_fireballs, True, False)
    if collisions:
        for targets in collisions.values():
            stats.score_right += 5 * len(targets)
        score.image_score_right()
    
def collis_gun_left_right_bullet(guns_left, right_bullets, score, stats):
    """ Обрабатывает столкновения правых пуль с левой пушкой """
    collisions = pygame.sprite.groupcollide(guns_left, right_bullets, False, True)
    if collisions:
        stats.life_left -= 10
    score.image_life_left()
    
def collis_gun_right_left_bullet(guns_right, left_bullets, score, stats):
    """ Обрабатывает столкновения левых пуль с правой пушкой """
    collisions = pygame.sprite.groupcollide(guns_right, left_bullets, False, True)
    if collisions:
        stats.life_right -= 10
    score.image_life_right()
        
def collis_gun_right_bomb(guns_right, bombs, score, stats):
    """ Обрабатывает столкновения бомб и правой пушки """
    collisions = pygame.sprite.groupcollide(guns_right, bombs, False, True)
    if collisions:
        stats.life_right -= 20
    score.image_life_right()

def collis_gun_left_bomb(guns_left, bombs, score, stats):
    """ Обрабатывает столкновения бомб и левой пушки """
    collisions = pygame.sprite.groupcollide(guns_left, bombs, False, True)
    if collisions:
        stats.life_left -= 20
    score.image_life_left()

def view_score(screen, score, x, y, color):
    """ Отображает счет """
    font = pygame.font.SysFont(None, 45)
    text_score = font.render('Score: ' + str(score) , True, color, (255, 255, 255))
    screen.blit(text_score, (x, y))
    pygame.display.update()
    
def all_collisions(screen, targets, bombs, enemies, left_bullets, right_bullets,
                   left_fireballs, right_fireballs, guns_left, guns_right,
                   score, stats):
    """ Обрабатывает все столкновения """
    collis_target_left_bullet(targets, left_bullets, score, stats)
    collis_target_right_bullet(targets, right_bullets, score, stats)  
    collis_enemy_left_bullet(enemies, left_bullets, score, stats)
    collis_enemy_right_bullet(enemies, right_bullets, score, stats)
    collis_bomb_left_bullet(screen, bombs, left_bullets, score, stats)
    collis_bomb_right_bullet(bombs, right_bullets, score, stats)

    collis_target_left_fireball(targets, left_fireballs, score, stats)
    collis_target_right_fireball(targets, right_fireballs, score, stats)
    collis_enemy_left_fireball(enemies, left_fireballs, score, stats)
    collis_enemy_right_fireball(enemies, right_fireballs, score, stats)
    collis_bomb_left_fireball(bombs, left_fireballs, score, stats)
    collis_bomb_right_fireball(bombs, right_fireballs, score, stats)

    collis_gun_left_right_bullet(guns_left, right_bullets, score, stats)
    collis_gun_right_left_bullet(guns_right, left_bullets, score, stats)
    collis_gun_right_bomb(guns_right, bombs, score, stats)
    collis_gun_left_bomb(guns_left, bombs, score, stats)
    

def run():    
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("JAAAGAN!")

    pygame.time.set_timer(pygame.USEREVENT, 40000)

    bombs = Group()
    enemies = Group()
    targets = Group()
    bombs = Group()
    left_bullets = Group()
    right_bullets = Group()
    left_fireballs = Group()
    right_fireballs = Group()
    guns_left = Group()
    gun_left = Gun(screen, 50, HEIGHT - 50)
    guns_left.add(gun_left)
    guns_right = Group()
    gun_right = Gun(screen, WIDTH - 50, HEIGHT - 50)
    guns_right.add(gun_right)

    stats = Stats()
    score = Score(screen, stats)
    
    target_army(screen, targets)
    enemy_army(screen, enemies)
    bomb_army(screen, bombs)
    score_left =0                 


    
    while not stats.finished:

        external_events(stats, FPS, screen, gun_left, gun_right,
                    left_bullets, right_bullets, left_fireballs,
                    right_fireballs, bombs, targets, enemies)# Проверяет внешние события
        
        all_objects_motion(screen, gun_left, gun_right, left_bullets,
                            left_fireballs, right_bullets,
                            right_fireballs, targets, enemies, bombs, score)#Перемещает и отрисовывает все объекты
        
        all_collisions(screen, targets, bombs, enemies, left_bullets, right_bullets,
                    left_fireballs, right_fireballs, guns_left, guns_right,
                        score, stats )# Проверяет все столкновения
    
    pygame.display.flip()
    
    f = open('text.txt', 'a+')
    print('Enter Your Name: ')
    name = input()
    f.write( 'Name: ' + str(name))
    f.write(', Score_left: ' + str(stats.score_left))
    f.write(', Score_right: ' + str(stats.score_right))
    f.write('\n')
    f.close()

    pygame.quit()
run()    
