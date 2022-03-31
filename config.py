"""This is a configuration file for Astro Raiders. 
You can change the settings via the game menus or 
just edit this file itself. Here's a list of options:

-FPS: change the frames per second of the game

-volume: change the volume of the music and sounds,
using a value of 1-100

-high_score: records the highest score for the player

-ship_color: changes the color of the ship, red, 
green or blue

-keybinds: changes the keys used for moving and
shooting, full list of keycodes availabe at:
http://www.pygame.org/docs/ref/key.html

-mouse: enable or disable mouse usage for moving and
shooting
"""
FPS = 30
ship_color = "green"
high_scores = [0]
WIDTH = 800
HEIGHT = 600

volume = {
    'music':100,
    'sfx':100
}

keybinds = {
    'left':"K_LEFT",
    'right':"K_RIGHT",
    'shoot':"K_SPACE",
    'special':"K_SHIFT"
}

mouse = {
    'move':True,
    'shoot':True
}