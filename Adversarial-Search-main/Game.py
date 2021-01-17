from Board import *
from Move import *
from math import inf, sqrt
#Adversary = White = Human
#Agent = Black = AI


def game_over(board):
    if(len(board.adversary_pieces) == 0 or len(board.agent_pieces) == 0):
        return True
    return False

def move_piece(board, cell, new_cell):
    
    #Starting cell does not have a piecealse
    if(cell.piece == None):
        return False

    #piece is destroyed by the pit
    if(new_cell.isPit):
        remove_piece(board, cell)
        board.my_grid[cell.x][cell.y].piece = None
        return True
    
    if(new_cell.piece == None):
        board.my_grid[new_cell.x][new_cell.y].piece = cell.piece
        update_cell(board, cell, new_cell)
        board.my_grid[cell.x][cell.y].piece = None
        return True

    type_start = type(cell.piece)
    type_dest = type(new_cell.piece)
    
    #both pieces destroyed    
    if(type_start is type_dest):
        remove_piece(board, cell)
        remove_piece(board, new_cell)
        board.my_grid[new_cell.x][new_cell.y].piece = None
        
    #Hero attacks
    elif(type_start is Hero):
        if(type_dest is Wumpus):
            update_cell(board, cell, new_cell)
            remove_piece(board, new_cell)
            board.my_grid[new_cell.x][new_cell.y].piece = cell.piece
        elif(type_dest is Mage):
            remove_piece(board, cell)

    #Mage attacks
    elif(type_start is Mage):
        if(type_dest is Hero):
            update_cell(board, cell, new_cell)
            remove_piece(board, new_cell)
            board.my_grid[new_cell.x][new_cell.y].piece = cell.piece
        elif(type_dest is Wumpus):
            remove_piece(board, cell)

    #Wumpus attacks
    elif(type_start is Wumpus):
        if(type_dest is Mage):
            update_cell(board, cell, new_cell)
            remove_piece(board, new_cell)
            board.my_grid[new_cell.x][new_cell.y].piece = cell.piece
        elif(type_dest is Hero):
            remove_piece(board, cell)

    board.my_grid[cell.x][cell.y].piece = None
    return True
    

#Adversary = white = human
def remove_piece(board, cell):
    if(cell.piece.color == 'w'):
        pieces = board.adversary_pieces
    else:
        pieces = board.agent_pieces

    for temp_cell in pieces:
        if((temp_cell.x == cell.x) and (temp_cell.y == cell.y)):
            pieces.remove(temp_cell)
            
def update_cell(board, cell, new_cell):
    if(cell.piece.color == 'w'):
        pieces = board.adversary_pieces
    else:
        pieces = board.agent_pieces
    remove_piece(board, cell)
    pieces.append(new_cell)


def display_valid_neighbors(board, cell):
    neighbors = get_valid_neighbors(board, cell)
    neighbors_coordinates = []
    for index in range(len(neighbors)):
        coordinate = (neighbors[index].x, neighbors[index].y)
        neighbors_coordinates.append(coordinate)

    return neighbors_coordinates

def get_valid_neighbors(board, cell):
    grid = board.my_grid
    neighbors = []
    # print(cell.x, cell.y)
    same_side_piece = False
    temp_cell = 0
    side = board.side_length

    #Diagonal Neighbors
    if(cell.x-1 > -1) and (cell.y-1 > -1):
        if(grid[cell.x-1][cell.y-1].piece != None):
            if(grid[cell.x-1][cell.y-1].piece.color != cell.piece.color):
                neighbors.append(grid[cell.x-1][cell.y-1])
        else:
            neighbors.append(grid[cell.x-1][cell.y-1])

    if(cell.x-1 > -1) and (cell.y+1 < side):
        if(grid[cell.x-1][cell.y+1].piece != None):
            if(grid[cell.x-1][cell.y+1].piece.color != cell.piece.color):
                neighbors.append(grid[cell.x-1][cell.y+1])
        else:
            neighbors.append(grid[cell.x-1][cell.y+1])


    if(cell.x+1 < side) and (cell.y-1 > -1):
        if(grid[cell.x+1][cell.y-1].piece != None):
            if(grid[cell.x+1][cell.y-1].piece.color != cell.piece.color):
                neighbors.append(grid[cell.x+1][cell.y-1])
        else:
            neighbors.append(grid[cell.x+1][cell.y-1])

    if(cell.x+1 < side) and (cell.y+1 < side):   
        if(grid[cell.x+1][cell.y+1].piece != None):
            if(grid[cell.x+1][cell.y+1].piece.color != cell.piece.color):
                neighbors.append(grid[cell.x+1][cell.y+1])
        else:
            neighbors.append(grid[cell.x+1][cell.y+1])
    
    #Horizontal/Vertical Neighbors
    if(cell.x-1 > -1):
        
        if(grid[cell.x-1][cell.y].piece != None):
            if(grid[cell.x-1][cell.y].piece.color != cell.piece.color):
                neighbors.append(grid[cell.x-1][cell.y])
        else:
            neighbors.append(grid[cell.x-1][cell.y])

    if(cell.x+1 < side):
        
        if(grid[cell.x+1][cell.y].piece != None):
            if(grid[cell.x+1][cell.y].piece.color != cell.piece.color):
                neighbors.append(grid[cell.x+1][cell.y])
        else:
            neighbors.append(grid[cell.x+1][cell.y])

    if(cell.y-1 > -1):
        
        if(grid[cell.x][cell.y-1].piece != None):
            if(grid[cell.x][cell.y-1].piece.color != cell.piece.color):
                neighbors.append(grid[cell.x][cell.y-1])
        else:
            neighbors.append(grid[cell.x][cell.y-1])
            
    if(cell.y+1 < side):
        if(grid[cell.x][cell.y+1].piece != None):
            if(grid[cell.x][cell.y+1].piece.color != cell.piece.color):
                neighbors.append(grid[cell.x][cell.y+1])
        else:
            neighbors.append(grid[cell.x][cell.y+1])

    return neighbors #list of dest cells

def set_valid_moves(board, move_list, cell, neighbors):
    x_src = cell.x
    y_src = cell.y
    for cell_dest in neighbors:
        x_dest = cell_dest.x
        y_dest = cell_dest.y
        move_list.append(Move(x_src, y_src, x_dest, y_dest, None, None, None))
    return move_list #list of moves



#Simple heuristic based on the number of pieces each side has
def get_evaluation(board, depth, maximizingPlayer):
    
    num_adversary_pieces = len(board.adversary_pieces) #Number of human, white pieces
    num_agent_pieces = len(board.agent_pieces) #Number of AI, black pieces
    
    evaluation = (num_adversary_pieces - num_agent_pieces) #2 - 3 = -1
    
    if(game_over(board)):
        if(evaluation > 0): #depth 2, maximizing player (AI won), evaluation -depth
            evaluation = evaluation + depth
        elif(evaluation < 0):
            evaluation = evaluation - depth

    return evaluation 

#Heurisitic value
def get_all_moves(board, adversaryTurn):
    pieces = []
    if(adversaryTurn):
        pieces = board.adversary_pieces
    else:
        pieces = board.agent_pieces

    my_moves = []
    for cell in pieces:
        neighbors = get_valid_neighbors(board, cell)
        my_moves = set_valid_moves(board, my_moves, cell, neighbors)

        #appending as a list BAD

    return my_moves

def get_result(board):
    if(len(board.adversary_pieces) == 0 and len(board.agent_pieces) != 0):
        print("Agent won")
    elif(len(board.adversary_pieces) != 0 and len(board.agent_pieces) == 0):
        print("Adversary won")
    else:
        print("Draw")

def get_user_input(board):

    side = board.side_length

    valid_cell = False
    x_start = -1
    y_start = -1
    while(not valid_cell):
        print("Select valid cell, must be a cell with white piece: ")
        print("\tSelect the x piece coordinate to move, must be int between 0 and ", side-1, end = ': ')
        x_start = int(input())
        print("\tSelect the y piece coordinate to move, must be int between 0 and ", side-1, end = ': ')
        y_start= int(input())
        for c in board.adversary_pieces:
            if (c.x == x_start) and (c.y == y_start):
                valid_cell = True
                break
        
        valid_moves = display_valid_neighbors(board, board.my_grid[x_start][y_start])
        print("select a valid move:")
        print("\tvalid moves: ", end='')
        print(valid_moves, end = "\n\n")
            
        dest_coordinate = (-1, -1)

        while(not(dest_coordinate in valid_moves)):
            print("Select the x piece coordinate of destination, must be int between 0 and ", side-1, end = ': ')
            x_dest = int(input())
            print("Select the y piece coordinate of destination, must be int between 0 and ", side-1, end = ': ')
            y_dest = int(input())

            dest_coordinate = (x_dest, y_dest)
                
        x_dest = dest_coordinate[0]
        y_dest = dest_coordinate[1]
        cell_start = board.my_grid[x_start][y_start]
        cell_dest = board.my_grid[x_dest][y_dest]

        move_piece(board, cell_start, cell_dest)

        print_grid(board)

def calculate_diagonal_distance(x_src, y_src, x_dest, y_dest):
    return sqrt((x_dest-x_src)**2 + (y_dest-y_src)**2)
    

def calculate_heuristic_piece(board, move):

    piece = board.my_grid[move.x_src][move.y_src].piece
    opponent_pieces = []
    if(piece.color == 'w'):
        opponent_pieces = board.agent_pieces
    else:
        opponent_pieces = board.adversary_pieces
    
    x_player = move.x_dest
    y_player = move.y_dest

    best_capturable_piece = 0
    
    player_piece_type = type(piece)
    
    best_distance = +inf
    distance = +inf

    for cell in opponent_pieces:
        
        x_opp = cell.x
        y_opp = cell.y
        opp_piece_type = type(cell.piece)
        if(player_piece_type is Hero ):
            if (opp_piece_type is Wumpus):
                distance = calculate_diagonal_distance(x_player, y_player, x_opp, y_opp)
                
        elif(player_piece_type is Mage ):
            if(opp_piece_type is Hero ):
                distance = calculate_diagonal_distance(x_player, y_player, x_opp, y_opp)

        elif(player_piece_type is Wumpus ):
            if (opp_piece_type is Mage):
                distance = calculate_diagonal_distance(x_player, y_player, x_opp, y_opp)

        if(distance < best_distance):
            best_distance = distance

    return best_distance
