import random

def shuffle(values: list[any]) -> list[any]:
    
    working_list = values[:]
    possible_indices = list()
    
    [possible_indices.append(i) for i in range(len(values))]
    
    for item in values:
        i = random.choice(possible_indices)
        working_list[i] = item
        possible_indices.remove(i)
    
    for i in range(len(working_list)):
        values[i] = working_list[i]


integers = [1, 2, 3, 4, 5]
shuffle(integers)
print(integers)


# TESTING THE FUNCTION

# Perform this test ten times:
for i in range(10):
    test_data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    shuffle(test_data1)
    # Make sure the number of values hasn't changed:
    assert len(test_data1) == 10
    # Make sure the order has changed:
    assert test_data1 != [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Make sure that when re-sorted, all the original values are there:
    assert sorted(test_data1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    

test_data2 = []
shuffle(test_data2)
assert test_data2 == []
