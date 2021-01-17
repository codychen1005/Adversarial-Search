from Game import *
from Move import *

from queue import PriorityQueue 
from math import inf, isfinite
import math

from copy import deepcopy



def best_move_search(board, depth, maximizingPlayer, algorithm):
    
    best_heuristic = +inf
    best_move = Move(None, None, None, None, None, None, None)
    
    alpha = -inf
    beta = +inf
            

    possible_moves = get_all_moves(board, maximizingPlayer)
    priority_queue = PriorityQueue()
    
    for move in possible_moves:
        move.heuristic_value = calculate_heuristic_piece(board, move)
        priority_queue.put(move)
    
    while not priority_queue.empty():
        move = priority_queue.get()
        
        child_board = deepcopy(board)
        current_cell = child_board.my_grid[move.x_src][move.y_src]
        new_cell = child_board.my_grid[move.x_dest][move.y_dest]
        move_piece(child_board, current_cell, new_cell)
        
        if algorithm == 1:
            value = min(best_heuristic, mini_max(child_board, depth-1, not maximizingPlayer))
        
        else:
            value = min(best_heuristic, alpha_beta(child_board, depth-1, alpha, beta, not maximizingPlayer))
            beta = min(beta, value)

        if(value < best_heuristic):
            # best_move = deepcopy(move)
            best_heuristic = value
            best_move.heuristic_value = best_heuristic
            best_move.x_src = move.x_src
            best_move.y_src = move.y_src
            best_move.x_dest = move.x_dest
            best_move.y_dest = move.y_dest
    
    start_cell = board.my_grid[best_move.x_src][best_move.y_src]
    end_cell = board.my_grid[best_move.x_dest][best_move.y_dest]
    return (start_cell, end_cell)


def mini_max(board, depth, maximizingPlayer):
    
    if(depth == 0 or game_over(board)):
        # print_grid(board)

        # print("get evaluation called", get_evaluation(board, depth, maximizingPlayer))
        return get_evaluation(board, depth, maximizingPlayer)

    current_board = deepcopy(board)

    if(maximizingPlayer):
        maxEval = -math.inf
        
        priority_queue = PriorityQueue()
        
        possible_moves = get_all_moves(board, maximizingPlayer)

        # getting all possible moves from the current_position and storing it in a queue       
        # Set heuristic_value for insertion  
        for move in possible_moves:
            #calculate move heuristic value
            #calculate distance to closest piece that can be captured
            move.heuristic_value = calculate_heuristic_piece(current_board, move)
            
            priority_queue.put(move)
            
        # priority_queue.sort(reverse=True)
        # traversing the children moves and evaluating them
        while(not priority_queue.empty()):
            child_board = deepcopy(current_board)
            move = priority_queue.get()
            
            current_cell = child_board.my_grid[move.x_src][move.y_src]
            new_cell = child_board.my_grid[move.x_dest][move.y_dest]
            
            # change position here to the child position on the grid (using child_position)
            move_piece(child_board, current_cell, new_cell)

            # evaluate
            maxEval = max(maxEval, mini_max(child_board, depth-1, False))
        return maxEval

    else:
        minEval = +math.inf
        
        priority_queue = PriorityQueue()
        
        possible_moves = get_all_moves(board, maximizingPlayer)

        # getting all possible moves from the current_position and storing it in a queue         
        for move in possible_moves:
            move.heuristic_value = calculate_heuristic_piece(current_board, move)

            priority_queue.put(move)
        
        # priority_queue.sort(reverse=True)
        # traversing the children moves and evaluating them
        while(not priority_queue.empty()):
            child_board = deepcopy(current_board)
            move = priority_queue.get()
            
            current_cell = child_board.my_grid[move.x_src][move.y_src]
            new_cell = child_board.my_grid[move.x_dest][move.y_dest]
            
            # change position here to the child position on the grid (using child_position)
            move_piece(child_board, current_cell, new_cell)

            # evaluate
            minEval = min(minEval, mini_max(child_board, depth-1, True))
        return minEval


def alpha_beta(board, depth, alpha, beta, maximizingPlayer):

    if(depth == 0 or game_over(board)):
        # print_grid(board)

        # print("get evaluation called", get_evaluation(board, depth, maximizingPlayer))
        return get_evaluation(board, depth, maximizingPlayer)

    current_board = deepcopy(board)

    if(maximizingPlayer):
        maxEval = -math.inf
        
        priority_queue = PriorityQueue()
        
        possible_moves = get_all_moves(board, maximizingPlayer)

        # getting all possible moves from the current_position and storing it in a queue         
        for move in possible_moves:
            move.heuristic_value = calculate_heuristic_piece(current_board, move)

            priority_queue.put(move)
        
        # priority_queue.sort(reverse=True)
        # traversing the children moves and evaluating them
        while(not priority_queue.empty()):
            child_board = deepcopy(current_board)
            move = priority_queue.get()
            
            current_cell = child_board.my_grid[move.x_src][move.y_src]
            new_cell = child_board.my_grid[move.x_dest][move.y_dest]
            
            # change position here to the child position on the grid (using child_position)
            move_piece(child_board, current_cell, new_cell)

            # evaluate
            eval = alpha_beta(child_board, depth-1, alpha, beta, False)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if(beta <= alpha):
                break

        return maxEval

    else:
        minEval = +math.inf
        
        priority_queue = PriorityQueue()
        
        possible_moves = get_all_moves(board, maximizingPlayer)

        # getting all possible moves from the current_position and storing it in a queue         
        for move in possible_moves:
            move.heuristic_value = calculate_heuristic_piece(current_board, move)

            priority_queue.put(move)
        
        # priority_queue.sort(reverse=True)
        # traversing the children moves and evaluating them
        while(not priority_queue.empty()):
            child_board = deepcopy(current_board)
            move = priority_queue.get()
            
            current_cell = child_board.my_grid[move.x_src][move.y_src]
            new_cell = child_board.my_grid[move.x_dest][move.y_dest]
            
            # change position here to the child position on the grid (using child_position)
            move_piece(child_board, current_cell, new_cell)

            # evaluate
            eval = alpha_beta(child_board, depth-1, alpha, beta, True)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if(beta <= alpha):
                break

        return minEval
