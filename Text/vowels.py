"""
Count Vowels - Enter a string and the program counts the number of vowels in the text.
For added complexity have it report a sum of each vowel found.
"""

def main():
    prompt = input("enter string: ")
    dict_of_vowels = count_vowels(prompt)
    print(dict_of_vowels)
    
def count_vowels(prompt):
    vowels = ["a", "e", "i", "o", "u"]
    counter = {}
    
    for char in prompt:
        if char in vowels:
            counter[char] = prompt.count(char)
    return counter

    
main()

