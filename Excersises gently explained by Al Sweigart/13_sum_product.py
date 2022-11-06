
def calculate_sum(numbers: list) -> float:
    
    sum_of_numbers = 0
    
    if len(numbers) != 0:
        for number in numbers:
            sum_of_numbers += number
        
    return sum_of_numbers


def calculate_product(numbers: list) -> float:
    
    product_of_numbers = 1
    
    if len(numbers) != 0:
        for number in numbers:
            product_of_numbers *= number
        
    return product_of_numbers


assert calculate_sum([]) == 0
assert calculate_sum([2, 4, 6, 8, 10]) == 30

assert calculate_product([]) == 1
assert calculate_product([2, 4, 6, 8, 10]) == 3840