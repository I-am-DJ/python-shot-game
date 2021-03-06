import random

import pygame

from game.main.monster.monster import BaseMonster, get_init_position


class SkeletonMonster(BaseMonster):

    def __init__(self, hero, screen, setting):
        self.speed = 2
        self.image = pygame.image.load("F:/python/test/game/main/image/skeletonMonster.jpg")
        self.init_position(setting)
        super().__init__(self.image, self.init_x, self.init_y, self.speed, None, hero, screen, blood=3)

    def init_position(self, setting):
        """小怪出生位置为边框附近"""
        rand = int(random.random() * 4)
        position = get_init_position(rand, setting)
        self.init_x = position["init_x"]
        self.init_y = position["init_y"]
