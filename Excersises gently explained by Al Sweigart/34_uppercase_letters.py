
def get_upper_case(text: str) -> str:   
    
    lower_upper = {
                    "a": "A", "b": "B", "c": "C", "d": "D", "e": "E",
                    "f": "F", "g": "G", "h": "H", "i": "I", "j": "J", 
                    "k": "K", "l": "L", "m": "M", "n": "N", "o": "O",
                    "p": "P", "q": "Q", "r": "R", "s": "S", "t": "T", 
                    "u": "U", "v": "V", "w": "W", "x": "X", "y": "Y", 
                    "z": "Z"
                    }

    upper_case_text = ""

    for char in text:
        if char in lower_upper:
            upper_case_text += lower_upper[char]
        else:
            upper_case_text += char

    return upper_case_text
         
                
assert get_upper_case("Hello") == "HELLO"
assert get_upper_case("hello") == "HELLO"
assert get_upper_case("HELLO") == "HELLO"
assert get_upper_case("Hello, world!") == "HELLO, WORLD!"
assert get_upper_case("goodbye 123!") == "GOODBYE 123!"
assert get_upper_case("12345") == "12345"
assert get_upper_case("") == ""

print(get_upper_case("Hello, world!"))

    
