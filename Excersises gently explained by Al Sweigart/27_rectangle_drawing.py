
def draw_rectangle(width: int, height: int):
    
    for i in range(height):
        print("#" * width, end="")
        print()
        
draw_rectangle(10, 10)