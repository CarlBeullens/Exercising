
from curses.ascii import isalpha, isupper


def get_title_case(text: str) -> str:
    
    title_case_text = ""
    
    for i in range(len(text)):
        
        if i == 0 and text[i].isalpha():
            title_case_text += text[i].upper()
            
        elif text[i-1].isalpha() and text[i].isalpha():
            title_case_text += text[i].lower()
        
        elif not text[i-1].isalpha() and text[i].isalpha():
            title_case_text += text[i].upper()
            
        else:
            title_case_text += text[i]
            
    return title_case_text
                       

assert get_title_case('Hello, world!') == 'Hello, World!'
assert get_title_case('HELLO') == 'Hello'
assert get_title_case('hello') == 'Hello'
assert get_title_case('hElLo') == 'Hello'
assert get_title_case('') == ''
assert get_title_case('abc123xyz') == 'Abc123Xyz'
assert get_title_case('cat dog RAT') == 'Cat Dog Rat'
assert get_title_case('cat,dog,RAT') == 'Cat,Dog,Rat'