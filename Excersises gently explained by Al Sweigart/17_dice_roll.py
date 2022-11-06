import random

def roll_dice(number_of_dice: int) -> int:
    """ Simulate rolling any number of six-sided dice and 
        returning the total sum of the dice roll.

    Args:
        number_of_dice (int): Parameter that represents the number of a six-sided dice.

    Returns:
        int: The function returns the sum of all of the dice rolls.
    """
    
    sum = 0
    for _ in range(number_of_dice):
        sum += random.randint(1, 6)
    
    return sum


assert roll_dice(0) == 0
assert roll_dice(1000) != roll_dice(1000)
for i in range(1000):
    assert 1 <= roll_dice(1) <= 6
    assert 2 <= roll_dice(2) <= 12
    assert 3 <= roll_dice(3) <= 18
    assert 100 <= roll_dice(100) <= 600