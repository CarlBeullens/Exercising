
def draw_pyramid(height: int) -> str:
    
    for i in range(1, height * 2, 2):
        row = ("#" * i).center(height * 2 - 1)
        print(row)
        
        
draw_pyramid(8)