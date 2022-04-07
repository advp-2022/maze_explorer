import pygame, sys, random
from pygame.math import Vector2

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


class Player(pygame.sprite.Sprite):
    """
    This is the Player class, which is used to define the main functionalities of the player.
    """
    def __init__(self,
                pos,
                maze,
                ):
        """ This is the class constructor """
        super().__init__()
        self.pos = pos # The position of the player
        self.maze = maze
        self.image = pygame.image.load("graphics/robot.png").convert() # Load the player's image
        self.image = pygame.transform.scale(self.image, (BLOCK_SIZE, BLOCK_SIZE)) # set the size to fit the size of the maze cells = BLOCK_SIZE
        self.rect = self.image.get_rect(center=self.pos) # Create a rectangle around the image to use is late for collision detection.
        self.image.set_colorkey(BLACK) # Adjust the image transparency
        self.visited_pos = [] # Initialize an empty list to store the visited cells at a later stage
        self.last_cell_before_dead_end = [] # Initialize an empty list to store the positions of the last cells you visited before reaching a dead end.

    def explore(self):
        """ This function is responsible for the movement of the player"""
        r = int(self.pos.y/50) # get the row index (r), PAY ATTENTION that it is equivalent to the y position on the screen
        c = int(self.pos.x/50) # get the column index (c), PAY ATTENTION that it is equivalent to the x position on the screen
        self.maze[r][c] -= 1 # mark the already visited cells as -1
        if self.deadend(self.get_neighbors()):
            self.maze[r][c] -= 50
        next_move = self.get_available_moves(self.get_neighbors(), False)
     
        next_move()
        self.rect = self.image.get_rect(center=self.pos)
    
    def get_available_moves(self, neighbors_list, visited):
        """ this function will return the move of least risistance in my algo that is the path with value closest to 0
        """
        all_moves = [self.move_right, self.move_left, self.move_up, self.move_down]

        indexes = [index for index, neighbor in enumerate(neighbors_list) if neighbor == max(neighbors_list)]
        return all_moves[indexes[0]]


    def get_neighbors(self):
        """
        This function will return the values of all the neighbors of the robot in a list in the following order: [Right, Left, Up, Down]
        """
        r = int(self.pos.y/50) # get the row index (r), PAY ATTENTION that it is equivalent to the y position on the screen
        c = int(self.pos.x/50) # get the column index (c), PAY ATTENTION that it is equivalent to the x position on the screen
        return [self.maze[r][c+1], self.maze[r][c-1], self.maze[r-1][c], self.maze[r+1][c]]

   
    def deadend(self,l):
        count=0
        for x in range(0,len(l)):
            if l[x] == -100:
                count+=1
        if count==3:
            return True
        else:
            return False
    
    def move_right(self):
        self.pos = self.pos + Vector2((BLOCK_SIZE,0))

    def move_left(self):
        self.pos = self.pos + Vector2((-BLOCK_SIZE,0))

    def move_up(self):
        self.pos = self.pos + Vector2((0,-BLOCK_SIZE))

    def move_down(self):
        self.pos = self.pos + Vector2((0,BLOCK_SIZE))

    def checkCollision(self, sprite2):
        col = self.rect.colliderect(sprite2)
        if col == True:
            print("You Win!")
            sys.exit()

class Target(pygame.sprite.Sprite):
    def __init__(self,pos, maze):
        super().__init__()
        self.maze = maze
        self.pos = random.choice(self.get_available_cells())
        self.image = pygame.image.load("graphics/target.png").convert()
        self.image = pygame.transform.scale(self.image, (BLOCK_SIZE, BLOCK_SIZE))
        self.rect = self.image.get_rect(center=self.pos)
        self.image.set_colorkey((0, 0, 0))

    def get_available_cells(self):
        available_cells = []
        for index_row, row in enumerate(self.maze):
            for index_col, elem in enumerate(row):
                if elem == 0:
                     available_cells.append(Vector2((index_col*BLOCK_SIZE, index_row*BLOCK_SIZE)))
        return available_cells
