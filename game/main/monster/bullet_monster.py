import random

import pygame

from game.main.gun.monster_gun import MonsterGun
from game.main.monster.monster import BaseMonster, get_init_position


class BulletMonster(BaseMonster):

    def __init__(self, hero, screen, setting):
        self.speed = 1
        self.image = pygame.image.load("F:/python/test/game/main/image/bulletMonster.jpg")
        self.init_position(setting)
        self.gun = MonsterGun(screen)
        super().__init__(self.image, self.init_x, self.init_y, self.speed, self.gun, hero, screen)

    def init_position(self, setting):
        """小怪出生位置为边框附近"""
        rand_int = random.randint(0, 4)
        position = get_init_position(rand_int, setting)
        self.init_x = position["init_x"]
        self.init_y = position["init_y"]

    def monster_action(self, monster_bullets):
        """simple action"""
        if self.gun.stop:
            pass
        if self.gun.is_changing:
            self.move()
        else:
            self.shot_hero(monster_bullets)



