"""
    Check if Palindrome - Checks if the string entered by the user is a palindrome.
    That is that it reads the same forwards as backwards like “racecar”
"""

def check_if_palindrome():
    prompt = input("==> ")
    original_list = [char for char in prompt]
    reversed_list = [char for char in prompt]
    reversed_list.reverse()
    
    for i in range(len(original_list)):
        if original_list[i] != reversed_list[i]:
            return False
    return True


check_1 = check_if_palindrome()
print(check_1)
