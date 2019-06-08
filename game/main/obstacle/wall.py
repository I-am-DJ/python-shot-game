import pygame

from game.main.obstacle.Impossible_obstacle import ImpossibleObstacle


class Wall(ImpossibleObstacle):

    def __init__(self, center_x, center_y):
        image = pygame.image.load("F:/python/test/game/main/image/wall.jpg")
        super().__init__(image, center_x, center_y)
