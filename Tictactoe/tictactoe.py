
import random

board = [[], [], []]
moves = set()
score_X = 0
score_O = 0

def reset_game():
    START_BOARD = [
                ["| ", "0" , " | " , "1" , " | " , "2" , " | "],
                ["| ", "3" , " | " , "4" , " | " , "5" , " | "],
                ["| ", "6" , " | " , "7" , " | " , "8" , " | "],
                ]
    
    for i, row in enumerate(START_BOARD):
        board[i] = row
        
    # Set comprehension to make a list of the possible moves 0-8 as str.
    ALL_MOVES = {str(i) for i in range(9)}    
    moves.update(ALL_MOVES)
    

def print_board():
    for row in board:
        for element in row:
            print(element, end="")
        print()
    print()     


def human_move():
    # Human player gets to play with "X".
    if not moves:
        sys.exit("It's a tie!")

    # while loop to make sure we only enter a valid move.
    while True:
        move = input("Your move: ")
        if move in moves:
            moves.remove(move)
            break
        else:
            continue

    for row in range(len(board)):
        for element in range(len(board[row])):
            if board[row][element] == move:
                board[row][element] = "X"  
    
    print_board()

    
def computer_move():
    # Computer gets to play with "O".
    if not moves:
        sys.exit("It's a tie!")
    
    move = random.choice(tuple(moves))
    moves.remove(move)
    print(f"Computers move: {move}")
    
    for row in range(len(board)):
        for element in range(len(board[row])):
            if board[row][element] == move:
                board[row][element] = "O"  
    
    print_board()

 
def check_for_winner():  
    horizontal_win = _horizontal_win()
    vertical_win = _vertical_win()
    diagonal1_win = _diagonal_win_1()
    diagonal2_win = _diagonal_win_2()
    
    possible_wins = [horizontal_win, vertical_win, diagonal1_win, diagonal2_win]
    
    for winner in possible_wins:
        
        if winner == "X":
            return "X"
        elif winner == "O":
            return "O"


def _horizontal_win(): 
    for row in range(len(board)):
        counter_X = 0
        counter_O = 0
        for col in range(1, 7, 2):
                
            if board[row][col] == "X":
                counter_X += 1  
            elif board[row][col] == "O":
                counter_O += 1
                
            if counter_X == 3:
                return "X"
            elif counter_O == 3:
                return "O"


def _vertical_win():
    for col in range(1, 7, 2):
        counter_X = 0
        counter_O = 0
        for row in range(len(board)):
            
            if board[row][col] == "X":
                counter_X += 1
            elif board[row][col] == "O":
                counter_O += 1
                
            if counter_X == 3:
                return "X"
            elif counter_O == 3:
                return "O"


def _diagonal_win_1():
    i = 1
    counter_X = 0
    counter_O = 0
    for row in range(len(board)):
        
        if board[row][i] == "X":
            counter_X += 1  
        elif board[row][i] == "X":
            counter_X += 1  
        
        i += 2
    
    if counter_X == 3:
            return "X"
    elif counter_O == 3:
            return "O"


def _diagonal_win_2():
    i = 5
    counter_X = 0
    counter_O = 0
    for row in range(len(board)):
        
        if board[row][i] == "X":
            counter_X += 1  
        elif board[row][i] == "X":
            counter_X += 1  
        
        i -= 2
    
    if counter_X == 3:
            return "X"
    elif counter_O == 3:
            return "O"


def _update_score_X():
    global score_X
    score_X += 1
    print(f"You win! Score: {score_X}-{score_O}")
    
    
def _update_score_O():   
    global score_O
    score_O += 1 
    print(f"Computer wins! Score: {score_X}-{score_O}")

            
def tictactoe(score_X=0, score_O=0):
    print_board()
    
    while True:
        
        human_move()
        
        if check_for_winner() == "X":
            _update_score_X()
            break
        
        elif check_for_winner() == "O":
            _update_score_O()
            break
        
        computer_move()
        
        if check_for_winner() == "X":
            _update_score_X
            break
        
        elif check_for_winner() == "O":
            _update_score_O()
            break
    
    
def game_loop():
    while True:
        reset_game()
        tictactoe()
        if input("Press any key to keep playing, press 'q' to quit. ") == "q":
            break
    
    print("\nGoodbye!") 
    
    
if __name__ == "__main__":
    game_loop()
