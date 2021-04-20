import pygame

from alien import Alien
from abc import ABC, abstractmethod

class Alien_heavy(Alien, ABC):
    @abstractmethod
    def __init__(self, ai_settings, screen):
        self.image = pygame.image.load('images/alien.bmp')
        self.armor = ai_settings.armor
        super().__init__(ai_settings, screen)
        
    
    def computing_hp(self):
        return self.armor + self.armor_plate + self.health

    def get_hit(self, bullet):
        self.hp -= bullet.how_much_dmg()