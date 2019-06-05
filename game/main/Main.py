
import pygame as pygame
from pygame.sprite import Group

from game.main.gun.hurt import judge_bullet_group
from game.main.monster.bullet_monster import BulletMonster
from game.main.person.person import Person
from game.main.prop.check_events import check_event
from game.main.prop.settings import Settings


def run_game():
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.scree_width, ai_setting.scree_height))
    pygame.display.set_caption("new game")
    people = Person(screen)
    hero_bullets = Group()
    monster_group = Group()
    monster_bullets = Group()
    add_monster(monster_group, people, screen, ai_setting)
    while True:
        screen.fill(ai_setting.bg_color)
        check_event(people, hero_bullets)
        people.move()
        blit_flush_hero(people, hero_bullets)
        bit_flush_monster(monster_group, monster_bullets)
        # judge_bullet_group(monster_bullets, people)
        judge_bullet_group(hero_bullets, monster_group)
        for bullet in hero_bullets.copy():
            if bullet.rect.centerx <= 0 or bullet.rect.centery <= 0:
                hero_bullets.remove(bullet)
        for bullet in monster_bullets.copy():
            if bullet.rect.centerx <= 0 or bullet.rect.centery <= 0:
                monster_bullets.remove(bullet)
        pygame.display.flip()


def add_monster(monster_group, hero, screen, setting):
    i = 0
    while i < 2:
        bullet_monster = BulletMonster(hero, screen, setting)
        monster_group.add(bullet_monster)
        i += 1


def blit_flush_hero(people, hero_bullets):
    people.blitme()
    for bullet in hero_bullets:
        bullet.draw_bullet()


def bit_flush_monster(monster_group, monster_bullets):
    for monster in monster_group:
        monster.monster_action(monster_bullets)
        monster.draw()
    for bullet in monster_bullets:
        bullet.draw_bullet()


run_game()
