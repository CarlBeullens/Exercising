from functools import update_wrapper
import random, string

def generate_password(length: int) -> str:
    """Generates password with min 12 characters, contains lowercase, uppercase, number and special chars.

    Args:
        length (int): desired length of the password with a min of 12

    Returns:
        str: password
    """
        
    LOWER = string.ascii_lowercase
    UPPER = string.ascii_uppercase
    NUMBERS = "1234567890"
    SPECIALS = "~!@#$%^&*()_+"
    ALL_CHARACTERS = LOWER + UPPER + NUMBERS + SPECIALS
    password = []
        
    if length < 12:
        length = 12
       
    password.append(LOWER[random.randint(0, len(LOWER)-1)])
    password.append(UPPER[random.randint(0, len(UPPER)-1)])
    password.append(NUMBERS[random.randint(0, 9)])
    password.append(SPECIALS[random.randint(0, len(SPECIALS)-1)])
    
    while True:
        if len(password) < length:
            password.append(ALL_CHARACTERS[random.randint(0, len(ALL_CHARACTERS)-1)])
        else:
            random.shuffle(password)
            return "".join(password)
