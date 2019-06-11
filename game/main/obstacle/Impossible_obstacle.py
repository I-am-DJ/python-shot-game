import pygame

from game.main.obstacle.obstracle import Obstacle


class ImpossibleObstacle(Obstacle):

    def __init__(self, image, center_x, center_y):
        super().__init__(image, center_x, center_y)

    def is_collision(self, body):
        pass
