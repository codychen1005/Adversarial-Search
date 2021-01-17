from Piece import *
from Cell import *

import random

class Board():
    def __init__(self, my_grid, adversary_pieces, agent_pieces, side_length):
        self.my_grid = my_grid
        self.adversary_pieces = adversary_pieces
        self.agent_pieces = agent_pieces
        self.side_length = side_length

def make_grid(board):
    side = board.side_length
    for x in range (side):
        board.my_grid.append([])
        for y in range(side):
            board.my_grid[x].append(Cell(x, y, None, False))
 
def set_grid(board):
    set_agent_pieces(board)
    set_adversary_pieces(board)
    set_pit(board)

def set_agent_pieces(board):
    #setting pieces for the top side, agent
    for x in range (0, board.side_length, 3): #Double check 3 is the counter
        #Wumpus
        piece = Wumpus(False, 'b')
        board.my_grid[x][0].piece = piece
        board.agent_pieces.append(Cell(x, 0, piece, False))
        #Hero
        piece = Hero(False, 'b')
        board.my_grid[x+1][0].piece = piece
        board.agent_pieces.append(Cell(x+1, 0, piece, False))
        #Mage
        piece = Mage(False, 'b')
        board.my_grid[x+2][0].piece = piece
        board.agent_pieces.append(Cell(x+2, 0, piece, False))

def set_adversary_pieces(board):
    #setting pieces for the bottom side, adversary
    side = board.side_length
    for x in range (0, side, 3): #Double check 3 is the counter
        #Wumpus
        piece = Wumpus(False, 'w')
        board.my_grid[x][side-1].piece = piece
        board.adversary_pieces.append(Cell(x, side-1, piece, False))
        #Hero
        piece = Hero(False, 'w')
        board.my_grid[x+1][side-1].piece = piece
        board.adversary_pieces.append(Cell(x+1, side-1, piece, False))
        #Mage
        piece = Mage(False, 'w')
        board.my_grid[x+2][side-1].piece = piece
        board.adversary_pieces.append(Cell(x+2, side-1, piece, False))
    

def set_pit(board):
    side = board.side_length
    for y in range(1, side - 1):
        pits_per_row = (side / 3)
        counter = 0
        while(counter < pits_per_row):
            x = random.randint(0, side-1)
            if(board.my_grid[x][y].isPit == False):
                board.my_grid[x][y].isPit = True
                counter += 1
    
def print_grid(board):
    # print("X")
    side = board.side_length
    for row in range (side):
        # print(row, "")
        for column in range (side):
            # print(column, "")
            if(board.my_grid[column][row].piece == None):
                if(board.my_grid[column][row].isPit == True):
                    print("P", end = '\t')
                else:
                    print("0", end = '\t')
            else:
                print (board.my_grid[column][row].get_piece().toString(), end = '\t')
        print("\n\n\n")
