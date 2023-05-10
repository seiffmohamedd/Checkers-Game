import pygame
from AvoidingCircularImport import RED , BLACK , SQUARE , BLUE

class Piece:
    PADDING=10
    BORDER = 2
      
    def __init__(self,row,column,color):

        self.row = row
        self.column = column
        self.color = color
        self.king=False

        if self.color == BLACK:
            self.direction = -1 #red is above # black is down

        else:
            self.direction = 1

        self.xCor=0
        self.yCor=0
        self.calculate_Cordinates()
    
    def calculate_Cordinates(self):
      self.x = SQUARE * self.column + SQUARE // 2
      self.y = SQUARE * self.row + SQUARE // 2
        
    def becomeAKing(self):
        self.king=True    
 
    def displayThePiece(self,win):
        radius = (SQUARE //2) - self.PADDING
        pygame.draw.circle(win , BLUE, (self.x , self.y),radius+ self.OUTLINE) #BIGGER CIRCLE
        pygame.draw.circle(win , self.color, (self.x , self.y),radius) # SMALLER CIRLCE 