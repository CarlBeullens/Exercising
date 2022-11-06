
import pprint

def find_next_empty(puzzle):
    
    for row_index in range(len(puzzle)):
        for col_index in range(len(puzzle[row_index])):
            if puzzle[row_index][col_index] == -1:          
                return row_index, col_index
        
    # If nothing is found, it means the board is full already
    return None, None


def is_valid(puzzle, guess, row_index, col_index):
    
    # Check if my guess is already in row coordinate.
    nums_in_row = puzzle[row_index]
    
    if guess in nums_in_row:
        return False
    
    # Check if my guess is already in column coordinate.
    nums_in_col = []
    
    for r in range(len(puzzle)):
        nums_in_col.append(puzzle[r][col_index])
    if guess in nums_in_col:
        return False
    
    # Check if my guess is already in the 3x3 matrix.
    # Work with remainder of the division that gets rounded to 0, 1 or 2 (// division).
    # Then multiply with 3 to get start index of 0, 3, 6
    row_start = (row_index // 3) * 3
    col_start = (col_index // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
            
    # If we get here, we passed all checks and therefore we return True.  
    return True


def solve_sudoku(puzzle):
        
    # tuple unpacking   
    r_coordinate, c_coordinate = find_next_empty(puzzle)
    
    # If all spaces are filled, we can't find anymore coordinates.
    if r_coordinate == None:
        return True
        
    for guess in range(1, 10):
        
        if is_valid(puzzle, guess, r_coordinate, c_coordinate):
            puzzle[r_coordinate][c_coordinate] = guess
            
            if solve_sudoku(puzzle):
                return True
        
        puzzle[r_coordinate][c_coordinate] = -1

    # If no number works out, then the puzzle can't be solved.
    return False


if __name__ == "__main__":
    
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    
    print(solve_sudoku(example_board))
    pprint.pprint(example_board)
