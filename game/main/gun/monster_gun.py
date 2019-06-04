import time
from threading import Thread

import pygame

from game.main.gun.monster_bullet import MonsterBullet
from game.main.gun.parent_gun import Gun


class MonsterGun(Gun):

    def __init__(self, screen):
        image = pygame.image.load("F:/python/test/game/main/image/monsterGun.jpg")
        super().__init__(speed=2, hurt=1, image=image, capacity=3, total_number=-1, bomb_chang_time=1, screen=screen)

    def shot(self, event, bullets_group):
        if self.current_bom > 0 and (not self.is_changing):
            bullet = MonsterBullet(self, event.rect.centerx, event.rect.centery)
            bullet.move()
            bullets_group.add(bullet)
            self.current_bom -= 1
        elif (not self.is_changing) and self.current_bom <= 0:
            self.change_bomb()


