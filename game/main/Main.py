import sys

import pygame as pygame
from pygame.sprite import Group

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
    while True:
        screen.fill(ai_setting.bg_color)
        check_event(people, hero_bullets)
        people.move()
        blit_flush(people, hero_bullets)

        for bullet in hero_bullets.copy():
            if bullet.rect.centerx <= 0 | bullet.rect.centery <= 0:
                hero_bullets.remove(bullet)

        pygame.display.flip()


def blit_flush(people, hero_bullets):
    people.blitme()
    for bullet in hero_bullets:
        bullet.draw_bullet()


run_game()
