def is_leap_year(year: int) -> bool:
    
        if (year % 100) != 0 and (year % 4) == 0 or (year % 400) == 0:
            return True
        
        return False


assert is_leap_year(1999) == False
assert is_leap_year(2000) == True
assert is_leap_year(2001) == False
assert is_leap_year(2004) == True
assert is_leap_year(2100) == False
assert is_leap_year(2400) == True