import pygame

# width and height of the window size 
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8 #no of rows and columns of the game 
SQUARE_SIZE = WIDTH//COLS

# rgb colors used
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128,128,128)

#the crown of the piece 
CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (44, 25))

#the 3 levels of difficulty 
EASY = 3
MEDIUM = 5
HARD = 6