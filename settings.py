from pygame.math import Vector2 as vec

# screen settings
FPS = 60
WIDTH, HEIGHT = 610, 670
TOP_BOTTOM_BUFFER = 50 # espacio arriba y abajo del maze
MAZE_WIDTH, MAZE_HEIGHT = WIDTH - TOP_BOTTOM_BUFFER, HEIGHT - TOP_BOTTOM_BUFFER

# Columnas y filas del grid
ROWS = 30
COLS = 28

# color settings
BLACK = (0,0,0)
RED = (208, 22, 22)
GREY = (107, 107, 107)
WHITE = (255,255,255)
PLAYER_COLOR = (255,238,0)
ORANGE = (255,69,0)

# font settings
START_TEXT_SIZE = 16
START_FONT = 'arial black'

# player settings
# PLAYER_START_POS = 0
