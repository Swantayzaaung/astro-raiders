#!/usr/bin/env python3
import pygame
import config
from random import randint, uniform
from os.path import join, dirname
from sprites import entity, player, enemy, bullet

########
# Game #
########
# Initialize pygame
pygame.init()

# Create a window
window = pygame.display.set_mode((config.WIDTH, config.HEIGHT))

#############
# Functions #
#############
# Load icons
def load_icon(folder, icon):
    print("Loaded icon ", join(folder, icon))
    return pygame.image.load(join(folder, icon))

##############
# Essentials #
##############
# Assets 
assets = join(dirname(__file__), 'assets')

# Set game clock
clock = pygame.time.Clock()

# Load some icons
spaceship_blue = load_icon(assets, 'spaceship-blue.png')
spaceship_green = load_icon(assets, 'spaceship-green.png')
spaceship_red = load_icon(assets, 'spaceship-red.png')
player_bullet = load_icon(assets, 'player-bullet.png')
enemy_1 = load_icon(assets, 'enemy-1.png')
enemy_2 = load_icon(assets, 'enemy-2.png')
enemy_3 = load_icon(assets, 'enemy-3.png')

# Game title and icon
pygame.display.set_caption("Astro Raiders")
pygame.display.set_icon(spaceship_blue)

##########
# Colors #
##########
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

###########
# Sprites #
###########
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()

player = player(370, 490, spaceship_blue)
bullet = bullet(370, 490, player_bullet)

for i in range(10):
    enemy1 = enemy(randint(0, 510), 70, enemy_1)
    all_sprites.add(enemy1)
    enemies.add(enemy1)

all_sprites.add(player, enemies, bullet)

#############
# Game loop #
#############
running = True
while running:
    # Cap the FPS
    clock.tick(config.FPS)

    # Events
    for event in pygame.event.get():
        # Close window
        if event.type == pygame.QUIT:
            running = False

    # Draw on the screen
    window.fill(BLACK)
    all_sprites.update()
    all_sprites.draw(window)

    # Refresh display
    pygame.display.flip()

