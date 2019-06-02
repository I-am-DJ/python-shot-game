import time
from threading import Thread

from game.main.gun.hero_bullet import HeroBullet


class Gun:

    def __init__(self, speed, hurt, image, capacity, total_number, bomb_chang_time, screen):
        self.speed = speed
        self.hurt = hurt
        self.capacity = capacity
        self.total_number = total_number
        self.current_bom = capacity
        self.bomb_change_time = bomb_chang_time
        self.image = image
        self.screen = screen
        self.is_changing = False
        self.rect = self.image.get_rect()

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def shot(self, event, hero_bullets):
        if self.current_bom > 0 and (not self.is_changing):
            bullet = HeroBullet(self, event)
            bullet.move()
            hero_bullets.add(bullet)
            self.current_bom -= 1
        elif (not self.is_changing) and self.current_bom <= 0:
            self.change_bomb()
        else:
            return

    def change_bomb(self):
        Thread(target=self.wait_change_bomb).start()
        self.total_number = self.total_number - self.capacity + self.current_bom
        self.current_bom = self.capacity

    def wait_change_bomb(self):
        self.is_changing = True
        time.sleep(self.bomb_change_time)
        self.is_changing = False
