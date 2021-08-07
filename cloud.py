import pygame
import random

class Cloud(pygame.sprite.Sprite):

    def __init__(self, image, start_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.y = start_y
        self.speed = random

    def update(self):
        self.rect.x += self.speed