
def draw_border(width: int, height: int) -> str:
    
    for i in range(height):
        if i == 0 or i == height-1:
            print("+" + (width - 2) * "-" + "+")
        else:
            print("|" + (width - 2) * " " + "|")
  
  
draw_border(16, 4)
    