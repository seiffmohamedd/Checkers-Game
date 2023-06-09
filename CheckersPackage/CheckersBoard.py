import pygame , math
from AvoidingCircularImport import SQUARE , ROWS , WHITE , RED ,BLACK , BLUE , COLUMNS,PINK
from CheckersPackage.piece import Piece


class CheckersBoard:
    def __init__(self):
        self.board =[] 
        self.red_left = 12  #red pieces are left (initially once game starts) red is the above
        self.black_left = 12 # black pieces are left (initially once game starts) black is down
        self.red_kings=0
        self.black_kings=0
        self.createPiecesOnBoard() #creating a board once an instance is created

    def displayBackground(self,win): #win -> window
        win.fill(WHITE) 
        for row in range(ROWS):
            for column in range(row%2 , ROWS, 2): # here enna hn color el squares en el row initially 0 fa mod el 2 yb2a brdu 0 yb2a hn start mn col 0 we nemshy 2 by 2
             pygame.draw.rect(win,BLACK,(row*SQUARE, column*SQUARE , SQUARE , SQUARE))

    def createPiecesOnBoard(self):
        for row in range(ROWS):
            self.board.append([])
            for column in range(COLUMNS):
                if column % 2 == ((row +1)%2):   # lw kont 3ayz abdaa2 ely fo2 ya5ood aweel column 3ady msh ha7oot el +1 fel row
                   if row < 3: #3shan 3ayzen ne3ml awel 3 foo2 bs ely homa btoo3 el red
                       self.board[row].append(Piece(row,column,RED))
                   elif row > 4:
                        self.board[row].append(Piece(row,column,BLACK))   
                   else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def CreateInitialState(self,win):
        self.displayBackground(win)
        for row in range(ROWS):
            for column in range(COLUMNS):
                piece = self.board[row][column]
                if piece != 0:
                    piece.displayThePiece(win)

    
    def get_piece(self, row, column):
       return self.board[row][column]
       
    
    def movement(self,piece, row , column):
        self.board[piece.row][piece.column] , self.board[row][column] = self.board[row][column] , self.board[piece.row][piece.column] 
        # swap the two pieces
        piece.move(row , column)

        if row==ROWS -1 or row == 0:
            piece.becomeAKing()
            if piece.color == RED:
                self.red_kings +=1

            else:
                self.black_kings +=1

    def get_valid_moves(self, piece):
        moves = {}
        left = piece.column - 1
        right = piece.column + 1
        row = piece.row

        if piece.color == RED or piece.king:
            moves.update(self._traverse_left(row -1, max(row-3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row -1, max(row-3, -1), -1, piece.color, right))
        if piece.color == BLACK or piece.king:
            moves.update(self._traverse_left(row +1, min(row+3, ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row +1, min(row+3, ROWS), 1, piece.color, right))
    
        return moves

    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break
            
            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last
                
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)
                    moves.update(self._traverse_left(r+step, row, step, color, left-1,skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, left+1,skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            left -= 1
        
        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLUMNS:
                break
            
            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r,right)] = last + skipped
                else:
                    moves[(r, right)] = last
                
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)
                    moves.update(self._traverse_left(r+step, row, step, color, right-1,skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, right+1,skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1
        
        return moves
    
 