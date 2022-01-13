#!/usr/bin/python3
import pygame
import config
from random import randint, uniform


def main():
    pygame.init()

    ###################
    # Essential Stuff #
    ###################

    # Game window
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    # Icons
    WINDOW_ICON = pygame.image.load('assets/spaceship-blue.png')
    PLAYER_ICON = pygame.image.load('assets/spaceship-blue.png')
    PLAYER_BULLET_ICON = pygame.image.load('assets/player-bullet.png')
    ENEMY1_ICON = pygame.image.load('assets/enemy-1.png')

    # Game title
    pygame.display.set_caption("Astro Raider")
    pygame.display.set_icon(WINDOW_ICON)

    # Player 
    PLAYER_X = 363
    PLAYER_Y = 500
    PLAYER_SPEED = 0.1

    # Enemies
    ENEMY_X = randint(0, WINDOW_WIDTH - 70)
    ENEMY_Y = 0
    ENEMY_SPEED = 0.1

    ###################
    # The game itself #
    ###################

    # Check if game is running
    running = True

    # The game loop
    while running:
        # RGB values for the window background
        WINDOW.fill((30, 34, 43))
        for event in pygame.event.get():
            # Close the game
            if event.type == pygame.QUIT:
                running = False

        # Move the player
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            PLAYER_X -= PLAYER_SPEED
            PLAYER_X = constrain(PLAYER_X, 0, WINDOW_WIDTH - 74)
        
        if keys[pygame.K_RIGHT]:
            PLAYER_X += PLAYER_SPEED
            PLAYER_X = constrain(PLAYER_X, 0, WINDOW_WIDTH - 74)

        # Keyboard controls
        if keys[pygame.K_SPACE]:
            create_entity(WINDOW, PLAYER_BULLET_ICON, PLAYER_X + 34, PLAYER_Y)
        
        ENEMY_Y += ENEMY_SPEED
        ENEMY_Y = wrap(ENEMY_Y, 0, WINDOW_HEIGHT)
        print(ENEMY_Y)

        create_entity(WINDOW, PLAYER_ICON, PLAYER_X, PLAYER_Y)
        create_entity(WINDOW, ENEMY1_ICON, ENEMY_X, ENEMY_Y)
        pygame.display.update()


# Draw entities on the screen
def create_entity(display, icon, x, y):
    display.blit(icon, (x, y))


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