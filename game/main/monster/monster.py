import random

import math
from pygame.sprite import Sprite

from game.main.common.util.math_function import get_direction


def get_init_position(random_int, settings):
    position = {}
    random_x = int(random.uniform(0, settings.scree_width))
    random_y = int(random.uniform(0, settings.scree_height))
    if random_int == 1:
        position["init_x"] = random_x
        position["init_y"] = 50
    elif random_int == 2:
        position["init_x"] = settings.scree_width - 50
        position["init_y"] = random_y
    elif random_int == 3:
        position["init_x"] = random_x
        position["init_y"] = settings.scree_height + 50
    else:
        position["init_x"] = 50
        position["init_y"] = random_y
    return position


class BaseMonster(Sprite):

    def __init__(self, image, init_x, init_y, speed, gun, hero, screen):
        super().__init__()
        self.image = image
        self.init_x = init_x
        self.init_y = init_y
        self.gun = gun
        self.hero = hero
        self.speed = speed
        self.screen = screen

        self.rect = self.image.get_rect()
        self.rect.centerx = self.init_x
        self.rect.centery = self.init_y
        self.gun.rect.centerx = self.rect.centerx - 10
        self.gun.rect.centery = self.rect.centery

    def move(self):
        """小怪看是否带枪，带枪随机移动，不带枪朝人物移动"""
        if self.gun is not None:
            mouse_z = get_direction((self.hero.rect.centerx - self.rect.centerx)
                                    , (self.hero.rect.centery - self.rect.centery))
            if mouse_z == 0:
                mouse_z = 1
            move_x = (self.hero.rect.centerx - self.rect.centerx) / mouse_z * self.speed
            move_y = (self.hero.rect.centery - self.rect.centery) / mouse_z * self.speed
        else:
            dircetion = random.uniform(-1 * math.pi, math.pi)
            move_x = math.cos(dircetion) * self.speed
            move_y = math.sin(dircetion) * self.speed
        if abs(move_x) < 1:
            if move_x < 0:
                move_x = -1
            else:
                move_x = 1
        if abs(move_y) < 1:
            if move_y < 0:
                move_y = -1
            else:
                move_y = 1
        self.rect.centerx += move_x
        self.rect.centery += move_y
        self.meet_obstacle()

    def shot_hero(self, monster_bullets):
        if self.gun:
            self.gun.shot(self.hero, monster_bullets)

    def draw(self):
        self.screen.blit(self.image, self.rect)
        if self.gun:
            self.screen.blit(self.gun.image, self.gun.rect)

    def monster_action(self, monster_bullets):
        pass

    def meet_obstacle(self):
        if self.rect.centerx > self.screen.get_width() - 10:
            self.rect.centerx = self.screen.get_width() - 10
        elif self.rect.centerx < 10:
            self.rect.centerx = 10
        if self.rect.centery > self.screen.get_height():
            self.rect.centery = self.screen.get_height() - 10
        elif self.rect.centery < 10:
            self.rect.centery = 10
        self.gun.rect.centerx = self.rect.centerx - 10
        self.gun.rect.centery = self.rect.centery
