import pygame
from CheckersPackage.piece import Piece
from AvoidingCircularImport import RED , BLACK , WHITE 
from CheckersPackage.CheckersBoard import CheckersBoard 

class Game:
    def __init__(self,win):
        self.selected_piece = None #if there is a selected piece or not selected yet 
        self.newBoard=CheckersBoard() #instance of the checkers board 
        self.turn= RED
        self.availableMoves={} #dictionary of open list (forienter ) for next available moves 
        self.win = win

    def update(self):
        # self.board.createPiecesOnBoard()
        self.newBoard.CreateInitialState(self.win)
        pygame.display.update()

    def restart(self):
        self.turn=RED
        self.newBoard.CheckersBoard() #instance of the checkers board
        self.selected_piece=None
        self.availableMoves={}

    def selectAPiece(self, row , column ):
        if self.selected_piece:
            result=self.move(row,column)
            if not result:
                self.selected_piece=None
                self.select(row,column)

        piece = self.newBoard.get_piece(row,column)
        if piece != 0 and piece.color ==self.turn:
            self.selected_piece=piece
            self.availableMoves=self.newBoard.get_available_moves(piece)
            return True

        return False         
    def move(self, row , column):
        piece = self.newBoard.get_piece(row,column)
        if self.selected_piece and piece==0 and (row,column) in self.availableMoves:
            self.newBoard.movement(self.selected_piece, row,column)
            self.turns()
        else :
            return False
        return True

    def turns(self):
        if self.turn==RED :
            self.turn = BLACK
        else:
            self.turn = RED