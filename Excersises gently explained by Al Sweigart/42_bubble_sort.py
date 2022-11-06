
def bubble_sort(numbers: list[int]) -> list[int]:
    
    for i in range(len(numbers) -1):
        for j in range(i+1, len(numbers)):
            
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
        
    return numbers


print(bubble_sort([2, 0, 4, 1, 3]))