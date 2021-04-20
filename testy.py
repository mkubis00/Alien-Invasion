import sys
import pygame

import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from alien_heavy import Alien_heavy
from abc import ABC, abstractmethod
from fighter import Fighter
from mheavy import Mheavy
from bullet import Bullet
from qheavy import Qheavy


ai_settings = Settings()
screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
#a = Alien_heavy(ai_settings, screen)
#print(a.get_health())
ship = Ship(ai_settings, screen)
bullet = Bullet(ai_settings, screen, ship)
a = Qheavy(ai_settings, screen)
b = a.hp
print(b)
a.get_hit(bullet)
print(a.hp)
a.get_hit(bullet)
print(a.hp)
a.get_hit(bullet)
print(a.hp)
a.get_hit(bullet)
print(a.hp)
a.get_hit(bullet)
print(a.hp)
a.get_hit(bullet)
print(a.hp)
a.get_hit(bullet)
print(a.hp)
a.get_hit(bullet)
print(a.hp)



