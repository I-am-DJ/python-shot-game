import pygame

from game.main.gun.base_gun import BaseGun


class Person:

    def __init__(self, screen):
        self.screen = screen
        self.gun = []
        # 人物出生自带基础武器
        self.gun.append(BaseGun(screen))
        self.gun_index = 0
        self.current_gun = self.gun[0]

        self.image = pygame.image.load("F:/python/test/game/main/image/Person.jpg")
        # 得到图形矩阵区域
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.gun_rect = self.current_gun.rect
        self.blood = 3

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.gun_rect.centerx = self.rect.centerx + 50
        self.gun_rect.centery = self.rect.centery

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        # todo 只有基础部分

    def change_gun(self):
        """切枪只支持单方向"""
        self.gun_index += 1
        self.gun_index = self.gun_index % len(self.gun)
        self.current_gun = self.gun[self.gun_index]

    def blitme(self):

        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.current_gun.image, self.gun_rect)

    def move(self):
        if self.moving_right:
            self.rect.centerx += 1
            self.gun_rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1
            self.gun_rect.centerx -= 1
        if self.moving_up:
            self.rect.centery -= 1
            self.gun_rect.centery -= 1
        if self.moving_down:
            self.rect.centery += 1
            self.gun_rect.centery += 1

    def is_hurt(self, gun):
        self.blood -= gun.hurt
        return self.blood

