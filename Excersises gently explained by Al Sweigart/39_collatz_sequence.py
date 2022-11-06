import random

def collatz(starting_number: int) -> list[int]:
    
    collatz_seq = list()
    n = starting_number
       
    if n < 1:
        return []
    
    else: 
        while True:
            
            collatz_seq.append(n)
            
            if n == 1:
                break
            
            elif n % 2 == 0:
                n = n // 2
                
            else:
                n = 3 * n + 1
                
    return collatz_seq


assert collatz(0) == []
assert collatz(10) == [10, 5, 16, 8, 4, 2, 1]
assert collatz(11) == [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
assert collatz(12) == [12, 6, 3, 10, 5, 16, 8, 4, 2, 1]
assert len(collatz(256)) == 9
assert len(collatz(257)) == 123


for i in range(1000):
    startingNum = random.randint(1, 10000)
    seq = collatz(startingNum)
    assert seq[0] == startingNum    # Make sure it includes the starting number.
    assert seq[-1] == 1             # Make sure the last integer is 1.