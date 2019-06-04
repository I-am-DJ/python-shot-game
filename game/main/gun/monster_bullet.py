from game.main.common.util.math_function import get_direction
from game.main.gun.bullet import Bullet


class MonsterBullet(Bullet):

    def __init__(self, gun, hero_init_x, hero_init_y):
        self.speed = 2
        self.hurt = 0.5
        self.frequency = 0.5
        self.hero_x = hero_init_x
        self.hero_y = hero_init_y
        super().__init__(gun, self.speed)

    def set_speed(self):
        """小怪子弹射击可以相对不精确"""
        tmp_x = self.hero_x - self.rect.centerx
        tmp_y = self.hero_y - self.rect.centery
        mouse_z = get_direction(tmp_x, tmp_y)
        self.speed_x = tmp_x / mouse_z * self.speed
        self.speed_y = -1 * tmp_y / mouse_z * self.speed
