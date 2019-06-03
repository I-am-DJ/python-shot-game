import pygame

from game.main.gun.hero_bullet import HeroBullet
from game.main.gun.parent_gun import Gun


class BaseGun(Gun):

    def __init__(self, screen):
        image = pygame.image.load("F:/python/test/game/main/image/baseGun.jpg")
        super().__init__(speed=2, hurt=3, image=image, capacity=5, total_number=-1, bomb_chang_time=1, screen=screen)

    def shot(self, event, bullets_group):
        if self.current_bom > 0 and (not self.is_changing):
            bullet = HeroBullet(self, event)
            bullet.move()
            bullets_group.add(bullet)
            self.current_bom -= 1
        elif (not self.is_changing) and self.current_bom <= 0:
            self.change_bomb()
        else:
            return
