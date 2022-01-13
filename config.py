"""This is a configuration file for Astro Raiders. 
You can change the settings via the game menus or 
just edit this file itself. Here's a list of options:

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

high_scores = [0]

volume = {
    'music':100,
    'sfx':100
}

ship_color = "red"

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