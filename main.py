import pygame

# Initialize the game
pygame.init()

# Create a game window
screen = pygame.display.set_mode((800, 600))

# Check if game is running
running = True

# Title and Icon
pygame.display.set_caption("Astro Raider")
# The game loop
while running:
    for event in pygame.event.get():
        # Close the game
        if event.type == pygame.QUIT:
            running = False