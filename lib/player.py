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
                random_pos
                ):
        """ This is the class constructor """
        super().__init__()
        self.maze = maze # Copy of the maze for single player
        if(random_pos):
            self.pos = random.choice(self.get_available_cells()) # Random position of the player
        else:
            self.pos = pos #Selected position of the player
        self.image = pygame.image.load("graphics/robot.png").convert() # Load the player's image
        self.image = pygame.transform.scale(self.image, (BLOCK_SIZE, BLOCK_SIZE)) # set the size to fit the size of the maze cells = BLOCK_SIZE
        self.rect = self.image.get_rect(center=self.pos) # Create a rectangle around the image to use is late for collision detection.
        self.image.set_colorkey(BLACK) # Adjust the image transparency

    def move(self):
        r = int(self.pos.y/BLOCK_SIZE) # get the row index (r), PAY ATTENTION that it is equivalent to the y position on the screen
        c = int(self.pos.x/BLOCK_SIZE) # get the column index (c), PAY ATTENTION that it is equivalent to the x position on the screen
        possible_moves = self.get_possible_moves(r, c) #get neighbor cells' values with their positions
        filtered_moves = filter(lambda possible_move:possible_move[0]==0,possible_moves) #choosing only paths with zero values
        filtered = list(filtered_moves)
        try: #checking if the paths with zero values exits in this situation
            next_move = random.choice(filtered) #choosing one of the zero valued paths randomly
            self.pos = next_move[1] #moving the robot to the chosen cell
            self.maze[r][c] = 50 #mark visited cell
        except:
            self.maze[r][c] -= 1 #mark dead ends/loops
            possible_moves.sort(key=lambda possible_move:possible_move[0]) #sort pathes in increasing order of values
            self.pos = possible_moves[-1][1] #choose the path with highest value
        self.rect = self.image.get_rect(center=self.pos) #update position

    def get_possible_moves(self, r, c):
        #list of tuples
        #Each tuple holds the value of neighboring cell and its position
        possible_moves = []
        possible_moves.append((self.maze[r][c+1], self.pos + Vector2((BLOCK_SIZE,0)))) #moving right
        possible_moves.append((self.maze[r][c-1], self.pos + Vector2((-BLOCK_SIZE,0)))) #moving left
        possible_moves.append((self.maze[r-1][c], self.pos + Vector2((0,-BLOCK_SIZE)))) #moving up
        possible_moves.append((self.maze[r+1][c], self.pos + Vector2((0,BLOCK_SIZE)))) #moving down
        return possible_moves

    def checkCollision(self, sprite2):
        col = self.rect.colliderect(sprite2)
        if col == True:
            print("You Win!")
            sys.exit()


    def get_available_cells(self):
        available_cells = []
        for index_row, row in enumerate(self.maze):
            for index_col, elem in enumerate(row):
                if elem == 0:
                     available_cells.append(Vector2((index_col*BLOCK_SIZE, index_row*BLOCK_SIZE)))
        return available_cells

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