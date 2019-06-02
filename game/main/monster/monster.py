from random import random

import math

from game.main.common.util.math_function import get_direction
from game.main.gun.monster_bullet import MonsterBullet


def get_init_position(random_int, settings):
    position = {}
    random_x = int(random.uniform(0, settings.scree_width))
    random_y = int(random.uniform(0, settings.scree_height))
    if random_int == 1:
        position["init_x"] = random_x
        position["init_y"] = 10
    elif random_int == 2:
        position["init_x"] = settings.scree_width - 10
        position["init_y"] = -1 * random_y
    elif random_int == 3:
        position["init_x"] = random_x
        position["init_y"] = -1 * settings.scree_height + 10
    else:
        position["init_x"] = 10
        position["init_y"] = -1 * random_y
    return position


class BaseMonster:

    def __init__(self, image, init_x, init_y, speed, gun, hero, screen):
        self.image = image
        self.init_x = init_x
        self.init_y = init_y
        self.gun = gun
        self.hero = hero
        self.speed = speed
        self.screen = screen

        self.rect = self.image.get_rect()
        self.rect.centerx = init_x
        self.rect.centery = init_y

    def move(self):
        """小怪看是否带枪，带枪随机移动，不带枪朝人物移动"""
        if self.gun:
            mouse_z = get_direction((self.hero.rect.centerx - self.rect.centerx)
                                    , (self.hero.rect.centery - self.rect.centery))
            move_x = (self.rect.centerx - self.hero.rect.centerx) / mouse_z * self.speed
            move_y = (self.rect.centery - self.hero.rect.centery) / mouse_z * self.speed
        else:
            dircetion = random.uniform(-1 * math.pi, math.pi)
            move_x = math.cos(dircetion) * self.speed
            move_y = math.sin(dircetion) * self.speed
        self.rect.centerx += move_x
        self.rect.centery += move_y
        self.gun.rect.centerx += move_x
        self.gun.rect.centery += move_y

    def shot(self, monster_bullets):
        if self.gun:
            bullet = MonsterBullet(self.gun, self.hero.rect.centerx, self.hero.rect.centery)
            monster_bullets.add(bullet)

    def draw(self):
        self.screen.blit(self.image, self.rect)
        if self.gun:
            self.screen.blit(self.gun.image, self.gun.rect)