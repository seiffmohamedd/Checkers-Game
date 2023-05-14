import pygame
#define variables for the borders size
WIDTH=500
HEIGHT=500

#define variables for the Standard Rows and Columns
ROWS=8
COLUMNS=8

#SIZE OF THE SQUARE THAT WILL HOLD THE PIECE
SQUARE=WIDTH/COLUMNS

#DEFINE COLORS WE ARE GOING TO USE IN THE BORDER
RED = (255 , 0 , 0 )
WHITE = (255 , 255 , 255)
BLACK=(0,0,0)
BLUE=(0,0,255)
PURPLE=(216,191,216)
PINK = (255,192,203)

#EL CROWN for the king piece
KINGCROWN = pygame.transform.scale(pygame.image.load('CheckersPackage/assets/crown.png'), (44, 25))
