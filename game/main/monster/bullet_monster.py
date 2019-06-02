from random import random

import pygame

from game.main.monster.monster import BaseMonster, get_init_position


class BulletMonster(BaseMonster):

    def __init__(self, gun, hero, screen, setting):
        self.speed = 1
        self.image = pygame.image.load("F:/python/test/game/main/image/bulletMonster.jpg")
        self.init_position(setting)
        super().__init__(self.image, self.init_x, self.init_y, self.speed, gun, hero, screen)

    def init_position(self, setting):
        """小怪出生位置为边框附近"""
        rand = int(random.random() * 4)
        position = get_init_position(rand, setting)
        self.init_x = position["init_x"]
        self.init_y = position["init_y"]
