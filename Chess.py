#responsible for user input and showing current game state

import pygame as p
p.init()
import ChessEngine

WIDTH = HEIGHT = 400
DIMENSION = 8 #8x8 board could be !!CHANGED!! for multiple player chess/ new gamemode
SquareSize = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

#initiliase global dictionary of images, called once 
#can !!CHANGE!! it so player can change skins 
def loadImages():
    pieces = ["wp","wR", "wN", "wB", "wQ", "wK",  "bp", "bR", "bN", "bB", "bQ", "bK"]
    for piece in pieces:
        # transform to make sure peices are of correct and same size
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SquareSize, SquareSize))


# main driver that handles user input and updates graphics 
def main():
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    #drawBoard(screen)
    #screen.fill((255, 255, 255))
    #GameState variable that calls ChessEngine with its variables included 
    gs = ChessEngine.GameState()
    loadImages()
    drawGameState(screen, gs)
    running = True
    while running:
        #lists events since last frame
        for e in p.event.get():
        #if player trys to close application, end it
            if e.type == p.QUIT:
                running = False

        clock.tick(MAX_FPS)
        p.display.flip()


#draws the graphics 
def drawGameState(screen, gs):
    drawBoard(screen)#draws squares onto board
    #add piece !!HIGHLIGHTER!!
    drawPieces(screen, gs.board)#draws pieces onto squares


def drawBoard(screen):
    
    XCoordinate = 0
    YCoordinate = 0

    for row in range(8):
        for column in range(8):
            if (column + row) % 2 == 0:
                p.draw.rect(screen, (118, 150, 86), (XCoordinate, YCoordinate, SquareSize, SquareSize))
            else:
                p.draw.rect(screen, (238, 238, 210), (XCoordinate, YCoordinate, SquareSize, SquareSize))
            XCoordinate += SquareSize
        YCoordinate += SquareSize
        XCoordinate = 0



def drawPieces(screen, board):

    XCoordinate = 0
    YCoordinate = 0

    for row in range(8):
        for column in range(8):
                piece = board[row][column]
                if piece != "--":
                    screen.blit(IMAGES[piece], p.Rect((XCoordinate, YCoordinate, SquareSize, SquareSize)))
                XCoordinate += SquareSize

        YCoordinate += SquareSize
        XCoordinate = 0


            

#means code is only ran when file is executed directly
if __name__ == "__main__":
    main()