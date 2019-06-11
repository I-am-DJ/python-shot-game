

class CheckCollision:

    def __init__(self, obstacles):
        self.obstacles = obstacles

    def change_direction(self, check_object):
        for obstacle in self.obstacles:
            dir = obstacle.is_collision(check_object)
            if dir is not None:
                return dir
