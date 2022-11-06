
def calculate_sum(numbers: list) -> float:
    
    sum_of_numbers = 0
    
    if len(numbers) != 0:
        for number in numbers:
            sum_of_numbers += number
        
    return sum_of_numbers


def average(numbers: list) -> float:
    
    return calculate_sum(numbers) / len(numbers)


assert average([1, 2, 3]) == 2
assert average([1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2
assert average([12, 20, 37]) == 23
assert average([0, 0, 0, 0, 0]) == 0

