import random
import time
from threading import Thread

import pygame

from game.main.gun.monster_gun import MonsterGun
from game.main.monster.monster import BaseMonster, get_init_position


class BulletMonster(BaseMonster):

    def __init__(self, hero, screen, setting):
        self.speed = 1
        self.image = pygame.image.load("F:/python/test/game/main/image/bulletMonster.jpg")
        self.init_position(setting)
        self.gun = MonsterGun(screen)
        self.frequency = 0.5
        self.stop = False
        self.move_stop = False
        super().__init__(self.image, self.init_x, self.init_y, self.speed, self.gun, hero, screen, blood=10)

    def init_position(self, setting):
        """小怪出生位置为边框附近"""
        rand_int = random.randint(0, 4)
        position = get_init_position(rand_int, setting)
        self.init_x = position["init_x"]
        self.init_y = position["init_y"]

    def monster_action(self, monster_bullets):
        """simple action"""
        if self.stop:
            return
        if self.gun.is_changing and self.move_stop is False:
            self.move()
            Thread(target=self.monster_move_stop).start()
        elif self.gun.is_changing is not True:
            self.shot_hero(monster_bullets)
            Thread(target=self.monster_stop).start()

    def monster_stop(self):
        self.stop = True
        time.sleep(self.frequency)
        self.stop = False

    def monster_move_stop(self):
        self.move_stop = True
        time.sleep(0.01)
        self.move_stop = False
