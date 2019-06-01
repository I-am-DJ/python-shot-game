import time

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

        self.rect = self.image.get_rect()

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def shot(self, event, hero_bullets):
        bullet = HeroBullet(self, event)
        bullet.move()
        hero_bullets.add(bullet)

    def change_bomb(self):
        time.sleep(self.bomb_change_time)
        self.total_number = self.total_number - self.capacity + self.current_bom
        self.current_bom = self.capacity
