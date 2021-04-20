import pygame

from alien_heavy import Alien_heavy

class Qheavy(Alien_heavy):
    def __init__(self, ai_settings, screen):
        self.image = pygame.image.load('images/qh.bmp')
        super().__init__(ai_settings, screen)

    def computing_hp(self):
        return int((self.armor_plate * self.armor) * 0.7 + self.health * 0.5)

    def get_hit(self, bullet):
        if self.hp > 0:
            self.hp -=  int(1.3 * bullet.how_much_dmg())