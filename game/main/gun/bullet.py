import time

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, gun, event):
        super().__init__()
        self.hurt = 1
        self.bullet_width = 4
        self.bullet_high = 4
        self.rect = pygame.Rect(0, 0, self.bullet_width, self.bullet_high)
        self.speed = 1
        self.frequency = 0.5
        self.gun = gun
        self.mouse_event = event
        self.rect.centerx = float(gun.rect.centerx)
        self.rect.centery = float(gun.rect.centery + 10)
        self.color = (0, 0, 255)
        mouse_x, mouse_y = self.mouse_event.pos
        mouse_z = float((mouse_x - self.rect.centerx) ** 2 +
                        (mouse_y - self.rect.centery) ** 2) ** 0.5
        self.speed_x = mouse_x / mouse_z * self.speed
        self.speed_y = mouse_y / mouse_z * self.speed
        if mouse_x < self.rect.centerx:
            self.speed_x *= -1
        if mouse_y > self.rect.centery:
            self.speed_y *= -1

    def move(self):
        self.rect.centery -= self.speed_y
        self.rect.centerx += self.speed_x

    def draw_bullet(self):

        self.move()
        pygame.draw.rect(self.gun.screen, self.color, self.rect)

