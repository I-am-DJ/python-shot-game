import time
from threading import Thread

import pygame

from game.main.gun.monster_bullet import MonsterBullet
from game.main.gun.parent_gun import Gun


class MonsterGun(Gun):

    def __init__(self, screen):
        image = pygame.image.load("F:/python/test/game/main/image/monsterGun.jpg")
        self.frequency = 1
        self.stop = True
        super().__init__(speed=2, hurt=1, image=image, capacity=10, total_number=-1, bomb_chang_time=1, screen=screen)

    def shot(self, event, bullets_group):
        if self.stop:
            Thread(target=self.monster_stop).start()
            return
        if self.current_bom > 0 and (not self.is_changing):
            bullet = MonsterBullet(self, event.rect.centerx, event.rect.centery)
            bullet.move()
            bullets_group.add(bullet)
            self.current_bom -= 1
            self.stop = True
        elif (not self.is_changing) and self.current_bom <= 0:
            self.change_bomb()
            self.stop = True

    def monster_stop(self):
        time.sleep(self.frequency)
        self.stop = False
