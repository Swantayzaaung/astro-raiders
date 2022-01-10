import pygame
import json

# Initialize the game
pygame.init()

# Create a game window
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Astro Raider")
icon = pygame.image.load('assets/spaceship-blue.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('assets/spaceship-blue.png')
playerX = 363
playerY = 480

def main():
    # Check if game is running
    running = True

    # The game loop
    while running:
        # RGB values for the screen background
        screen.fill((30, 34, 43))

        for event in pygame.event.get():
            # Close the game
            if event.type == pygame.QUIT:
                running = False
        
        player(playerX, playerY)
        pygame.display.update()


def player(x, y):
    screen.blit(playerImg, (x, y))


main()