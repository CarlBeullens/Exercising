
# Solved as a bubble sort where the first or last number of the list is being returned.

def get_smallest(numbers: list[int]) -> int:
    
    if not numbers:
        return None
    
    for i in range(len(numbers) -1):
        for j in range(i+1, len(numbers)):
            
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
                
    return numbers[0]


def get_biggest(numbers: list[int]) -> int:
    
    if not numbers:
        return None
    
    for i in range(len(numbers) -1):
        for j in range(i+1, len(numbers)):
            
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
                
    return numbers[-1]


# Solved with variable. Probably the better solution.

def get_smallest_with_variable(numbers: list[int]) -> int:
    
    if not numbers:
        return None
    
    smallest = numbers[0]
    
    for value in numbers:
        if value < smallest:
            smallest = value
    
    return smallest


print(get_smallest([28, 25, 42, 2, 28]))
print(get_biggest([28, 25, 42, 2, 28]))
print(get_smallest_with_variable([28, 25, 42, 2, 28]))