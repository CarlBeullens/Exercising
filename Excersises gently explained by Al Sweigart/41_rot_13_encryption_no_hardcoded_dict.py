from string import ascii_uppercase

def rot13(text: str) -> str:
    
    text_to_rot13_chars = list()
    ENCRYPTION = {}

    for char in ascii_uppercase:
        
        if ord(char) < 78:
            value = ord(char) + 13
        elif ord(char) >= 78:
            value = ord(char) - 13
        ENCRYPTION[char] = chr(value)
    
    for char in text:
        
        if not char.isalpha():
            text_to_rot13_chars.append(char)
        
        elif char.isupper(): #H
            value = ENCRYPTION[char]
            text_to_rot13_chars.append(value)
        
        elif char.islower():
            value = ENCRYPTION[char.upper()].lower()
            text_to_rot13_chars.append(value)
                
    return "".join(text_to_rot13_chars)        
    
    
print(rot13("Hello, world!"))

assert rot13('Hello, world!') == 'Uryyb, jbeyq!'
assert rot13('Uryyb, jbeyq!') == 'Hello, world!'
assert rot13(rot13('Hello, world!')) == 'Hello, world!'
assert rot13('abcdefghijklmnopqrstuvwxyz') == 'nopqrstuvwxyzabcdefghijklm'
assert rot13('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'NOPQRSTUVWXYZABCDEFGHIJKLM'



