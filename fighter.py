import pygame

from alien import Alien

class Fighter(Alien):
    def __init__(self, ai_settings, screen):
        self.image = pygame.image.load('images/alien.bmp')
        super().__init__(ai_settings, screen)
        
    def computing_hp(self):
        return int(self.armor_plate * 0.7 + self.health)

    def get_hit(self, bullet):
        if self.hp > 0:
            self.hp -=  int(1.3 * bullet.how_much_dmg())