"""
Create constants from enumerators.
"""
import screeninfo

# Screen related
SCREEN_W = screeninfo.get_monitors()[0].width
SCREEN_H = screeninfo.get_monitors()[0].height
GAME_W = int(SCREEN_W / 2)
GAME_H = int(SCREEN_H - 80)

# Frame related
TARGET_FPS = 60

# Colors
BLUE_D = "#23243b"
BLUE_S = "#131320"
GREY_B = "#cad4e3"
GREY_R = "#8aa0c1"
