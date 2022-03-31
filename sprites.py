import pygame
import config
from random import randint, uniform

class entity(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = (config.WIDTH / 2, config.HEIGHT / 2)
        self.rect.x = x
        self.rect.y = y
        self.speedX = 0
        self.speedY = 0
    
    def update(self):
        self.speedX = 0
        self.speedY = 0
        

class player(entity):
    def __init__(self, x, y, img):
        super().__init__(x, y, img)
    
    def update(self):
        # Keyboard movement
        key = pygame.key.get_pressed()
        self.speedX = 0
        if key[pygame.K_LEFT]:
            self.speedX = -6
        if key[pygame.K_RIGHT]:
            self.speedX = 6
        self.rect.x += self.speedX
        # Constrain player x
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > config.WIDTH:
            self.rect.right = config.WIDTH
        
class enemy(entity):
    def __init__(self, x, y, img):
        super().__init__(x, y, img)
    
    def clone(self):
        enemy(self.x, self.y, self.img)

    def update(self):
        # Drop down the screen
        self.speedY = randint(5, 10)
        self.rect.y += self.speedY
        # Wrap up once it goes below the screen
        if self.rect.top > config.HEIGHT:
            self.rect.bottom = 0
            self.rect.x = randint(0, config.WIDTH - self.rect.width)


class bullet(entity):
    def __init__(self, x, y, img):
        super().__init__(x, y, img)
    
    def update(self):
        self.speedY = 1
        self.rect.y -= self.speedY