#!/usr/bin/python3
import pygame
from random import randint, uniform

# Window stuff
WIDTH = 800
HEIGHT = 600

def main():
    ##############
    # Essentials #
    ##############
    pygame.init()

    # Create a window
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Astro Raiders")
    pygame.display.set_icon("assets/spaceship-blue.png")


# Constrain values to fit within a boundary
def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))


# Wrap values if they go over a boundary
def wrap(val, min_val, max_val):
    if val > max_val:
        val = min_val
    if val < min_val:
        val = max_val
    return val


main()