
def rot13(text: str) -> str:
    
    encryption_uppercase = {"A" : "N", "B" : "O", "C" : "P", "D" : "Q", "E" : "R", "F" : "S",
                            "G" : "T", "H" : "U", "I" : "V", "J" : "W", "K" : "X", "L" : "Y",
                            "M" : "Z", "N" : "A", "O" : "B", "P" : "C", "Q" : "D", "R" : "E",
                            "S" : "F", "T" : "G", "U" : "H", "V" : "I", "W" : "J", "X" : "K",
                            "Y" : "L", "Z" : "M"
                            }
    
    text_to_rot13_chars = list()
    
    for char in text:
        
        if not char.isalpha():
            text_to_rot13_chars.append(char)
        
        elif char.isupper():
            value = encryption_uppercase[char]
            text_to_rot13_chars.append(value)
        
        elif char.islower():
            value = encryption_uppercase[char.upper()].lower()
            text_to_rot13_chars.append(value)
                
    return "".join(text_to_rot13_chars)        
    
    
print(rot13("Hello, world!"))

assert rot13('Hello, world!') == 'Uryyb, jbeyq!'
assert rot13('Uryyb, jbeyq!') == 'Hello, world!'
assert rot13(rot13('Hello, world!')) == 'Hello, world!'
assert rot13('abcdefghijklmnopqrstuvwxyz') == 'nopqrstuvwxyzabcdefghijklm'
assert rot13('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'NOPQRSTUVWXYZABCDEFGHIJKLM'

