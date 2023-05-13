import pygame
from AvoidingCircularImport import WIDTH , HEIGHT , SQUARE 
from CheckersPackage.gamelogic import Game
from CheckersPackage.CheckersBoard import CheckersBoard

# Setting a constant FPS for the game
FPS = 45

# making the border size
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT)) 

#title of the game 
pygame.display.set_caption('Checkers Game')


def getCordinatesByMouse(pos):
    x,y =pos
    row = y // SQUARE
    column = x // SQUARE
    return row , column
    


#runing the game in event loop every n of seconds to check if there is any change to render 
def main():
    #just a var for the event loop of the game running
    newBoard=CheckersBoard() #instance of the checkers board 
    game=Game(WINDOW) #instance of the game
    gameRuning = True

    clock = pygame.time.Clock() #for the FPS
    # piece=newBoard.get_piece(0,1)
    # newBoard.movement(piece, 4 ,3)




    while gameRuning:

        clock.tick(FPS) #tick FPS Defined Above
        
        for event in pygame.event.get():  #check event if happened any time
            if event.type == pygame.QUIT: #if i needed to quit and pressed it turn off the game  
                gameRuning = False  #and exit the loop

            if event.type == pygame.MOUSEBUTTONDOWN:
                 pass
                # pos=pygame.mouse.get_pos()
                # rosw , columsn = getCordinatesByMouse(pos)
                

        game.update()
    # pygame.quit() #window    of game is closed fffrrrrrr mnwwww


main()