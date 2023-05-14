import pygame
from AvoidingCircularImport import WIDTH , HEIGHT , SQUARE , RED , WHITE , BLACK , BLUE
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
    run = True
    clock = pygame.time.Clock()
    game = Game(WINDOW)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = getCordinatesByMouse(pos)
              
                if game.turn==RED:
                    game.selectAPiece(int(row), int(col))
                    print (int(row), int(col))


        game.update()
    
    pygame.quit()

main()