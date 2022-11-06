
def get_cost_off_coffee(number_of_coffees: int, price_per_coffee: float) -> float:
    """ 
        Simple calculation to see how much a given quantity of
        coffees costs while considering this buy-8-get-1-free system.

    Args:
        number_of_coffees (int): number of coffees bought
        price_per_coffee (float): price per coffee

    Returns:
        float: Total cost taking into account every 9th coffee is free.
    """
    
    n = number_of_coffees // 9
    return (number_of_coffees - n) * price_per_coffee

assert get_cost_off_coffee(7, 2.50) == 17.50
assert get_cost_off_coffee(8, 2.50) == 20
assert get_cost_off_coffee(9, 2.50) == 20
assert get_cost_off_coffee(10, 2.50) == 22.50

for i in range(1, 4):
    assert get_cost_off_coffee(0, i) == 0
    assert get_cost_off_coffee(8, i) == 8 * i
    assert get_cost_off_coffee(9, i) == 8 * i
    assert get_cost_off_coffee(18, i) == 16 * i
    assert get_cost_off_coffee(19, i) == 17 * i
    assert get_cost_off_coffee(30, i) == 27 * i