
def multiplication_table():
    
    print("|".rjust(3), end="")
    for row in range(1, 11):
        value = str(row).rjust(2)
        print(value, end=" ")
    print()

    print("--+" + 30 * "-")

    for row in range(1, 11):
        print(f"{row}|".rjust(3), end="")
        for column in range(1, 11):
            value = str(row * column).rjust(2)
            print(value, end=" ")
        print()
        
multiplication_table()