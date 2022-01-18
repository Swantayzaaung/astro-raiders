#!/usr/bin/python3
import pygame

from os.path import join, dirname
from random import randint, uniform
from helpers import constrain, wrap
from ships import player_ship


###########
# Sprites #
###########
all_sprites = pygame.sprite.Group()
player = player_ship()
all_sprites.add(player)

##############
# Essentials #
##############

# Window size 
WIDTH = 800
HEIGHT = 600

# Assets 
assets = join(dirname(__file__), 'assets')

# Initialize pygame
pygame.init()

# Load some icons
spaceship_blue = pygame.image.load(join(assets, 'spaceship-blue.png'))

# Create a window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Astro Raiders")
pygame.display.set_icon(spaceship_blue)

#############
# Game loop #
#############
running = True
while running:
    # Events
    for event in pygame.event.get():
        # Close window
        if event.type == pygame.QUIT:
            running = False
    
    # Draw on the screen
    window.fill((0, 0, 0))
    all_sprites.draw(window)

    # Refresh display
    pygame.display.flip()