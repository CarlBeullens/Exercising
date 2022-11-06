# Comparing naive and binary search algorithm.

import random
import time

l = [1, 3, 5, 7, 9, 11, 13]
target = 11

def naive_search(l: list[int], target: int) -> int:
    
    for index, value in enumerate(l):
        if value == target:
            return index
    return -1


def binary_search(l, target, low=0, high=len(l)):
    
    if high < low:
        return -1
        
    mid = (low + high) // 2
        
    if l[mid] == target:
        return mid
        
    elif target < l[mid]:
        return binary_search(l, target, low, mid-1)
            
    elif target > l[mid]:
        return binary_search(l, target, mid+1, high)


result_naive_search = naive_search(l, 11)
print(result_naive_search)

result_binary_search = binary_search(l, 11)
print(result_binary_search)


# Test naive and binary search on a large list.

# Create large list to test both searches.
l_large = list()
for _ in range(10000):
    l_large.append(random.randint(0, 10000)) 
l_large.sort()


# Test naive search algorithm.
start = time.time()
for target in l_large:
    naive_search(l_large, target)
end = time.time()

time_per_iteration = (end - start) / 10000

print(f"The naive search algorithm took {(time_per_iteration * 1000_000):.2f} microseconds per iteration.")


# Test binary search algorithm.
start = time.time()
for target in l_large:
    binary_search(l_large, target)
end = time.time()

time_per_iteration = (end - start) / 10000

print(f"The binary search algorithm took {(time_per_iteration * 1000_000):.2f} microseconds per iteration.")
