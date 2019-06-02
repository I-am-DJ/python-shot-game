import pygame

from game.main.gun.parent_gun import Gun


class BaseGun(Gun):

    def __init__(self, screen):
        image = pygame.image.load("F:/python/test/game/main/image/baseGun.jpg")
        super().__init__(speed=2, hurt=3, image=image, capacity=5, total_number=-1, bomb_chang_time=3, screen=screen)
