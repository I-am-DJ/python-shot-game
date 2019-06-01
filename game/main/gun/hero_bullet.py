from game.main.gun.bullet import Bullet


class HeroBullet(Bullet):

    def __init__(self, gun, event):
        self.speed = 1
        self.mouse_event = event
        self.hurt = 1
        self.frequency = 0.5
        super().__init__(gun, self.speed)

    def set_speed(self):
        mouse_x, mouse_y = self.mouse_event.pos
        tmp_x = mouse_x - self.rect.centerx
        tmp_y = mouse_y - self.rect.centery
        if abs(tmp_x) > abs(tmp_y):
            self.speed_x = abs(float(tmp_x) / float(tmp_y) * self.speed)
            self.speed_y = self.speed
        else:
            self.speed_x = self.speed
            self.speed_y = abs(float(tmp_y) / float(tmp_x) * self.speed)
        if abs(self.speed_x) > 3:
            self.speed_x = self.speed_x / abs(self.speed_x) * 3
        if abs(self.speed_y) > 3:
            self.speed_y = self.speed_y / abs(self.speed_y) * 3
        if tmp_x < 0:
            self.speed_x *= -1
        if tmp_y > 0:
            self.speed_y *= -1
