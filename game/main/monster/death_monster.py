import random
import time
from threading import Thread

import pygame

from game.main.monster.monster import BaseMonster, get_init_position


class DeathMonster(BaseMonster):

    def __init__(self, hero, screen, setting):
        self.speed = 3
        self.image = pygame.image.load("F:/python/test/game/main/image/deathMonster.jpg")
        self.init_position(setting)
        self.move_stop = False
        super().__init__(self.image, self.init_x, self.init_y, self.speed, None, hero, screen, blood=5)

    def init_position(self, setting):
        """小怪出生位置为边框附近"""
        rand = int(random.random() * 4)
        position = get_init_position(rand, setting)
        self.init_x = position["init_x"]
        self.init_y = position["init_y"]

    def monster_action(self, monster_bullets):
        if not self.move_stop:
            self.move()
            Thread(target=self.monster_move_stop).start()

    def monster_move_stop(self):
        self.move_stop = True
        time.sleep(0.01)
        self.move_stop = False
