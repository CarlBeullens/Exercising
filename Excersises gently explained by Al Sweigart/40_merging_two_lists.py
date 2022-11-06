
def merge_two_lists(list1: list[int], list2: list[int]) -> list[int]:
    
    merged_list = list()
    
    i1, i2 = 0, 0
    
    while True:
        
        if len(merged_list) == len(list1) + len(list2):
            break
        
        elif not i1 == len(list1) and not i2 == len(list2):
            
            if list1[i1] < list2[i2]:
                merged_list.append(list1[i1])
                i1 += 1
                
            else:
                merged_list.append(list2[i2])
                i2 += 1
        
        elif i1 == len(list1):
            merged_list.append(list2[i2])
            i2 += 1
            
        elif i2 == len(list2):
            merged_list.append(list1[i1])
            i1 += 1
            
    return merged_list
        

print(merge_two_lists([4, 5], [1, 2, 3]))


assert merge_two_lists([1, 3, 6], [5, 7, 8, 9]) == [1, 3, 5, 6, 7, 8, 9]
assert merge_two_lists([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]
assert merge_two_lists([4, 5], [1, 2, 3]) == [1, 2, 3, 4, 5]
assert merge_two_lists([2, 2, 2], [2, 2, 2]) == [2, 2, 2, 2, 2, 2]
assert merge_two_lists([1, 2, 3], []) == [1, 2, 3]
assert merge_two_lists([], [1, 2, 3]) == [1, 2, 3]