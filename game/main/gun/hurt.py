
from game.main.monster.monster import BaseMonster
from game.main.person.person import Person


def judge_bullet_group(group, obstacle):
    for bullet in group.copy():
        bullet_hit, obstacle_kill = bullet.is_hit(obstacle)
        if bullet_hit:
            group.remove(bullet)
        if obstacle_kill is not None and isinstance(obstacle_kill, Person):
            return False
        if obstacle_kill and isinstance(obstacle_kill, BaseMonster):
            obstacle.remove(obstacle_kill)
