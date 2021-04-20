import pygame

from alien_heavy import Alien_heavy

class Mheavy(Alien_heavy):
    def __init__(self, ai_settings, screen):
        super().__init__(ai_settings, screen)
        self.image = pygame.image.load('images/mh.bmp')

    def computing_hp(self):
        return int((self.health + self.armor_plate) * 0.3 * self.armor)

    def get_hit(self, bullet):
        
        if self.hp > 0:
            self.hp -= int((bullet.how_much_dmg()/self.hp) * 400)