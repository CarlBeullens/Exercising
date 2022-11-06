
# coins in the denominations of 1 (pennies), 5 (nickels), 10 (dimes), and 25 cents (quarters)

def make_change(amount: int) -> dict[str, int]:
    
    """ Simple cash register to dispense correct change: denominations of 1 (pennies), 5 (nickels), 10 (dimes), and 25 cents (quarters).

    Returns:
        dict[str, int]: Dictionary returning minimum required amount of possible coins to cover the given amount.
    """

    change = {}
    remainder = 0
    
    # quarters
    n = amount // 25
    if n != 0:
        change["quarters"] = n
    remainder = amount % 25
        
    # dimes
    n = remainder // 10
    if n != 0:
        change["dimes"] = n
    remainder = remainder % 10
    
    # dimes    
    n = remainder // 5
    if n != 0:
        change["nickels"] = n
    remainder = remainder % 5
    
    # pennies    
    n = remainder // 1
    if n != 0:
        change["pennies"] = n
    remainder = remainder % 1
        
    return change


print(make_change(57))

assert make_change(30) == {'quarters': 1, 'nickels': 1}
assert make_change(10) == {'dimes': 1}
assert make_change(57) == {'quarters': 2, 'nickels': 1, 'pennies': 2}
assert make_change(100) == {'quarters': 4}
assert make_change(125) == {'quarters': 5}