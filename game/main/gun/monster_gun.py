import pygame

from game.main.gun.parent_gun import Gun


class MonsterGun(Gun):

    def __init__(self, screen):
        image = pygame.image.load("F:/python/test/game/main/image/monsterGun.jpg")
        super().__init__(speed=2, hurt=1, image=image, capacity=None, total_number=-1, bomb_chang_time=1, screen=screen)
