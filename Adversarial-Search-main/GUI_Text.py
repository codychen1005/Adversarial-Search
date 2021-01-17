from Board import *
from Piece import *
from Cell import *
from Game import *
from Search import *

def print_instructions():
    print("wW: white Wumpus, bW: black Wumpus, wH: white Hero, bH: black Hero, wM: white Mage, bM: black Mage, P: Pit")
    print("Hero captures Wumpus, Wumpus captures Mage, and Mage captures Hero")
    print("Good Luck!")
# def get_user_input():
#     user_input = input()
#     while(type(user_input) is not int):
#         user_input = input()
#     pass

def main():
    adversary_turn = True
    
    print("Enter the size of the board as a multiple of 3 (e.g. '3'): ", end = ' ')
    side_length = int(input())

    main_board = Board([], [], [], side_length)
    # main_board.side_length = d

    print_instructions() 
    make_grid(main_board)
    
    '''Standard set board'''
    set_grid(main_board)
    print_grid(main_board)
    print("x" *100, end = "\n\n")
    
    '''Test Depth of 1'''
    # blackMage = Mage(False, 'b')
    # main_board.my_grid[1][0].piece = blackMage
    # main_board.agent_pieces.append(Cell(1, 0, blackMage, False))

    # whiteHero = Hero(False, 'w')
    # main_board.my_grid[1][1].piece = whiteHero
    # main_board.adversary_pieces.append(Cell(1, 1, whiteHero, False))

    '''Test Depth of 2'''
    # blackMage = Mage(False, 'b')
    # main_board.my_grid[0][1].piece = blackMage
    # main_board.agent_pieces.append(Cell(0, 1, blackMage, False))

    # whiteHero = Hero(False, 'w')
    # main_board.my_grid[1][0].piece = whiteHero
    # main_board.adversary_pieces.append(Cell(1, 0, whiteHero, False))
    # whiteHero2 = Hero(False, 'w')
    # main_board.my_grid[1][2].piece = whiteHero2
    # main_board.adversary_pieces.append(Cell(1, 2, whiteHero2, False))
    # whiteWumpus = Wumpus(False, 'w')
    # main_board.my_grid[2][1].piece = whiteWumpus
    # main_board.adversary_pieces.append(Cell(2, 1, whiteWumpus, False))

    '''Test Depth of 3'''
    # blackMage = Mage(False, 'b')
    # main_board.my_grid[0][0].piece = blackMage
    # main_board.agent_pieces.append(Cell(0, 0, blackMage, False))

    # whiteHero = Hero(False, 'w')
    # main_board.my_grid[1][0].piece = whiteHero
    # main_board.adversary_pieces.append(Cell(1, 0, whiteHero, False))

    # main_board.my_grid[1][1].isPit = True
    '''Test Depth of 3, second'''
    # blackMage = Mage(False, 'b')
    # main_board.my_grid[0][0].piece = blackMage
    # main_board.agent_pieces.append(Cell(0, 0, blackMage, False))

    # whiteHero = Hero(False, 'w')
    # main_board.my_grid[1][2].piece = whiteHero
    # main_board.adversary_pieces.append(Cell(1, 2, whiteHero, False))

    
    print_grid(main_board)

    print("Enter '1' to search by standard mini_max or '2' to search by alpha_beta_pruning: ", end = ' ')
    algorithm_selection = int(input())

    print("Enter depth of search as an integer (e.g. '3'): ", end = ' ')
    depth = int(input())
    
    while(not game_over(main_board)):

        if(adversary_turn): #human
            get_user_input(main_board)

        else:
            t = best_move_search(main_board, 3, False, algorithm_selection)

            cell_src = t[0]
            cell_dest = t[1]
            move_piece(main_board, cell_src, cell_dest)
            print("x" * 100, end = "\n\n")
            
            print_grid(main_board)
            # print(get_ai_move())
        
        adversary_turn = not adversary_turn

    get_result(main_board)

if __name__ == "__main__":
    main()
