import pygame, sys, random
from pygame.math import Vector2
from lib import maze, player
import configparser

config = configparser.ConfigParser()
config.read('var.ini')

# Global variables
BLACK = eval(config['DEFAULT']['BLACK']) # defining the black color using RBG
WHITE = eval(config['DEFAULT']['WHITE']) # defining the white color using RBG
GREEN = eval(config['DEFAULT']['GREEN']) # defining the green color using RBG
WINDOW_HEIGHT = int(config['DEFAULT']['WINDOW_HEIGHT']) # defining the height of the game window in pixels 
WINDOW_WIDTH = int(config['DEFAULT']['WINDOW_WIDTH']) # defining the width of the game window in pixels
BLOCK_SIZE = int(config['DEFAULT']['BLOCK_SIZE']) #Set the size of the grid block
MAZE = maze.predefined_maze() # call this function to get the maze matrix, which will be used to draw the maze on the window, and will also be used by the robot to navigate the maze.
MAZE = maze.randomMaze(int(WINDOW_HEIGHT/BLOCK_SIZE), int(WINDOW_WIDTH/BLOCK_SIZE))

def createSquare(x, y, color):
    pygame.draw.rect(SCREEN, color, [x, y, BLOCK_SIZE, BLOCK_SIZE])


def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    
    _player = player.Player(pos = Vector2(BLOCK_SIZE, BLOCK_SIZE), maze = MAZE)
    _target = player.Target((random.randrange(BLOCK_SIZE, WINDOW_WIDTH, BLOCK_SIZE),random.randrange(BLOCK_SIZE, WINDOW_HEIGHT, BLOCK_SIZE)), maze=MAZE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        SCREEN.fill(WHITE)
        _player.explore()
        maze.drawMaze(SCREEN, MAZE, BLOCK_SIZE) # Call the drawMaze method from the lib package to draw the maze on the screen 
        SCREEN.blit(_target.image,_target.pos)
        SCREEN.blit(_player.image,_player.pos)
        _player.checkCollision(_target.rect)
        pygame.display.flip()
        CLOCK.tick(3)

if __name__ == '__main__':
    main()