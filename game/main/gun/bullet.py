import pygame
from pygame.sprite import Sprite

from game.main.monster.monster import BaseMonster
from game.main.person.person import Person


class Bullet(Sprite):

    def __init__(self, gun, speed):
        super().__init__()

        self.bullet_width = 4
        self.bullet_high = 4
        self.rect = pygame.Rect(0, 0, self.bullet_width, self.bullet_high)
        self.speed = speed
        self.gun = gun
        # 初始化子弹x,y速度
        self.speed_x = 1
        self.speed_y = 1
        self.rect.centerx = float(gun.rect.centerx)
        self.rect.centery = float(gun.rect.centery + 10)
        self.color = (0, 0, 255)
        # mouse_z = float((mouse_x - self.rect.centerx) ** 2 +
        #                 (mouse_y - self.rect.centery) ** 2) ** 0.5
        self.set_speed()

    def set_speed(self):
        pass

    def move(self):
        self.rect.centery -= self.speed_y
        self.rect.centerx += self.speed_x

    def draw_bullet(self):
        self.move()
        pygame.draw.rect(self.gun.screen, self.color, self.rect)

    def is_hit(self, objects):
        for something in objects:
            if something.rect.contains(self.rect):
                if isinstance(something, Person) or isinstance(something, BaseMonster):
                    if something.is_hurt(self.gun) <= 0:
                        return True, something
                    else:
                        return True, None
        return False, None
