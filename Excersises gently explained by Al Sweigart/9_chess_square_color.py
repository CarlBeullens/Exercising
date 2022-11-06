
def getChessSquareColor(column, row):
    
    c = column - 1
    r = row - 1
    
    if c | r < 0 or c | r > 8:
        return ""
    if c + r == 1:
        return "black"
    if (c + r) % 2 == 0:
        return "white"
    else: 
        return "black"


assert getChessSquareColor(1, 1) == "white"
assert getChessSquareColor(2, 1) == "black"
assert getChessSquareColor(1, 2) == "black"
assert getChessSquareColor(8, 8) == "white"
assert getChessSquareColor(0, 8) == ""
assert getChessSquareColor(2, 9) == ""
