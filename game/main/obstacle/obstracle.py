

class Obstacle:

    def __init__(self, image, center_x, center_y):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.centerx = center_x
        self.rect.centery = center_y

    def is_collision(self, body):
        if self.rect.left <= body.rect.left <= self.rect.rigth or \
                self.rect.left <= body.rect.right <= self.rect.rigth:
            if self.rect.up >= body.rect.up >= self.rect.down:
                return 'UP'
            elif self.rect.up >= body.rect.down >= self.rect.down:
                return 'DOWN'
        elif self.rect.up >= body.rect.up >= self.rect.down or \
                self.rect.up >= body.rect.down >= self.rect.down:
            if self.rect.left <= body.rect.left <= self.rect.rigth:
                return 'LEFT'
            elif self.rect.left <= body.rect.right <= self.rect.rigth:
                return 'RIGHT'
