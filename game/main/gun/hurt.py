from game.main.monster.monster import BaseMonster
from game.main.person.person import Person


def judge_bullet_group(group, obstacle):
    for bullet in group.copy():
        bullet_hit, obstacle_kill = is_hit(bullet, obstacle)
        if bullet_hit:
            group.remove(bullet)
        if obstacle_kill is not None and isinstance(obstacle_kill, Person):
            return False
        if obstacle_kill and isinstance(obstacle_kill, BaseMonster):
            obstacle.remove(obstacle_kill)


def is_hit(bullet, objects):
    for something in objects:
        if something.rect.contains(bullet.rect):
            if isinstance(something, Person) or isinstance(something, BaseMonster):
                if something.is_hurt(bullet.gun) <= 0:
                    return True, something
                else:
                    return True, None
    return False, None
