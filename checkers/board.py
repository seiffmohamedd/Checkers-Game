import pygame
from .constants import BLACK, ROWS, RED, SQUARE_SIZE, COLS, WHITE
from .piece import Piece

class Board:
    def __init__(self):
        self.board = []
        self.red_left = self.white_left = 12 #red pieces are left (initially once game starts) red is the above,# white pieces are left (initially once game starts) white is down
        self.red_kings = self.white_kings = 0 # kings starts as 0 both sides
        self.create_board()
    
    def draw_squares(self, win):
        win.fill(BLACK) #background color filled by black color
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):# here enna hn color el squares en el row initially 0 fa mod el 2 yb2a brdu 0 yb2a hn start mn col 0 we nemshy 2 by 2
                pygame.draw.rect(win, RED, (row*SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def evaluate(self):
        return self.white_left - self.red_left + (self.white_kings * 0.5 - self.red_kings * 0.5)

    def get_all_pieces(self, color): #list bl remaining pieces kollhom el fel board
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color: # if the place not empty and there is a piece with a color
                    pieces.append(piece)
        return pieces

    def move(self, piece, row, col):
        # swap the two pieces
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col] 
        piece.move(row, col)

        if row == ROWS - 1 or row == 0:
            piece.make_king()
            if piece.color == WHITE:
                self.white_kings += 1
            else:
                self.red_kings += 1 

    def get_piece(self, row, col): # here the return give me the specific piece used in the select function in game.py to get the available moves of the piece
        return self.board[row][col]

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row +  1) % 2): # lw kont 3ayz abdaa2 ely fo2 ya5ood aweel column 3ady msh ha7oot el +1 fel row
                    if row < 3:  #3shan 3ayzen ne3ml awel 3 foo2 bs ely homa btoo3 el red
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, RED))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)
        
    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    def remove(self, pieces): # remove the piece from this specific place if it was eaten or moved
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == RED:
                    self.red_left -= 1 # minimize the red left number by one
                else:
                    self.white_left -= 1 # minimize the white left number by one
    
    def winner(self):
        if self.red_left <= 0: #in case of the red has finished the pieces 
            return WHITE
        elif self.white_left <= 0: #in case of the white  has finished the pieces 
            return RED
        elif self.hasMoves(RED):
            return WHITE
        elif self.hasMoves(WHITE):
            return RED
        else:
            return None
    
    def get_valid_moves(self, piece): #get the valid moves for a specific piece used when we want to select a specific piece and get the movements valid
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == RED or piece.king:
            moves.update(self._traverse_left(row -1, max(row-3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row -1, max(row-3, -1), -1, piece.color, right))
        if piece.color == WHITE or piece.king:
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
            if right >= COLS:
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
    

    def hasMoves(self, color):
        pieces = []
        moves = {}
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        
        for piece in pieces:
            left = piece.col - 1
            right = piece.col + 1
            row = piece.row

            if piece.color == RED or piece.king:
                moves.update(self._traverse_left(row -1, max(row-3, -1), -1, piece.color, left))
                moves.update(self._traverse_right(row -1, max(row-3, -1), -1, piece.color, right))
            if piece.color == WHITE or piece.king:
                moves.update(self._traverse_left(row +1, min(row+3, ROWS), 1, piece.color, left))
                moves.update(self._traverse_right(row +1, min(row+3, ROWS), 1, piece.color, right))
        
        if len(moves):
            return False
        else:
            return True