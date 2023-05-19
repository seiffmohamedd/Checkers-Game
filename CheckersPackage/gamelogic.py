import pygame
from CheckersPackage.piece import Piece
from AvoidingCircularImport import RED , BLACK , WHITE , SQUARE , PINK , BLUE
from CheckersPackage.CheckersBoard import CheckersBoard 

class Game:
    def __init__(self,win):
        # self.selected_piece = None #if there is a selected piece or not selected yet 
        # self.newBoard=CheckersBoard() #instance of the checkers board 
        # self.turn= RED
        # self.availableMoves={} #dictionary of open list (forienter ) for next available moves 
        # self.s
        self._init()
        self.win = win

    def _init(self):
        self.selected_piece = None
        self.newBoard = CheckersBoard()
        self.turn = RED
        self.available_moves = {}

    def update(self):
        # self.board.createPiecesOnBoard()
        self.newBoard.CreateInitialState(self.win)
        self.   draw_available_moves(self.available_moves)
        pygame.display.update()

    def restart(self):
      self._init()

    def selectAPiece(self, row , column ):
        if self.selected_piece:
            result=self._move(row,column) #awel ma a select ay piece ha3mlha move ll row we column el selected brdu ely na 3ayzo 
            if not result:
                self.selected_piece=None
                self.selectAPiece(row,column) # htb2a haga zy recursuive function akeeny dost 3la piece tanya aslun mynf3sh ados 3leha ma hy re select el piece
       
        piece = self.newBoard.get_piece(row,column)
        if piece != 0: #and piece.color ==self.turn:
            print (piece)
            self.selected_piece=piece
            self.available_moves=self.newBoard.get_valid_moves(piece)
            print(self.available_moves)
            return True

        return False         
    def _move(self, row , column):  #private move function LEHA MOVE AW LAA
        piece = self.newBoard.get_piece(row,column)
        if self.selected_piece and piece==0 and (row,column) in self.availableMoves:
            self.newBoard.movement(self.selected_piece, row,column) #hn3ml hena move l row we el col ll selected piece
            self.turns()
        else :
            return False
        return True

    def turns(self):
        self.available_moves = {}
        if self.turn==RED :
            self.turn = BLACK
        else:
            self.turn = RED

    def draw_available_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE, (col * SQUARE + SQUARE//2, row * SQUARE + SQUARE//2), 20)