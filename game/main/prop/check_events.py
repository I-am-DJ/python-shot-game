import sys

import pygame


def check_event(object_event, hero_bullets):
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                object_event.moving_right = True
            elif event.key == pygame.K_LEFT:
                object_event.moving_left = True
            elif event.key == pygame.K_UP:
                object_event.moving_up = True
            elif event.key == pygame.K_DOWN:
                object_event.moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                object_event.moving_right = False
            elif event.key == pygame.K_LEFT:
                object_event.moving_left = False
            elif event.key == pygame.K_UP:
                object_event.moving_up = False
            elif event.key == pygame.K_DOWN:
                object_event.moving_down = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            object_event.current_gun.shot(event, hero_bullets)

