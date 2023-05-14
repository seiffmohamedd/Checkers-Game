import pygame
from AvoidingCircularImport import RED , BLACK , SQUARE , BLUE , KINGCROWN

class Piece:
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
 
    def displayThePiece(self,win): #draw
        radius = (SQUARE //2)-10
        pygame.draw.circle(win , self.color, (self.x , self.y),radius) # CIRLCE As a Piece
        if self.king == True:
            win.blit(KINGCROWN, (self.x -KINGCROWN.get_width()//2 , self.y - KINGCROWN.get_height()//2))

    def move(self,row,column):
        self.row = row
        self.column = column
        self.calculate_Cordinates()

    def __repr__(self):
        return str(self.color)
    