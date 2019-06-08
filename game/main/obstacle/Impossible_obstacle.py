import pygame


class ImpossibleObstacle:

    def __init__(self, image, center_x, center_y):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.centerx = center_x
        self.rect.centery = center_y

    def is_contain(self, body):
        return body.rect.contain(self.rect)

