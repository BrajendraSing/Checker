import pygame

WIDTH, HEIGHT = 700, 700
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

# Colors rgb
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

# load crown image
CROWN = pygame.image.load('assets/crown.png')
CROWN = pygame.transform.scale(CROWN,(45,25))