import pygame 
from AvoidingCircularImport import SQUARE , ROWS , WHITE , RED ,BLACK , BLUE , COLUMNS


class CheckersBoard:
    def __init__(self):
        self.board =[] 
        self.selected_piece = None #if there is a selected piece or not selected yet 
        self.red_left = 12  #red pieces are left (initially once game starts) red is the above
        self.black_left = 12 # black pieces are left (initially once game starts) black is down
        self.red_kings=0
        self.black_kings=0

    def displayBackground(self,win): #win -> window
        win.fill(WHITE) 
        for row in range(ROWS):
            for column in range(row%2 , ROWS, 2): # here enna hn color el squares en el row initially 0 fa mod el 2 yb2a brdu 0 yb2a hn start mn col 0 we nemshy 2 by 2
             pygame.draw.rect(win,BLACK,(row*SQUARE, column*SQUARE , SQUARE , SQUARE))

    def createPiecesOnBoard(self):
       pass         
             