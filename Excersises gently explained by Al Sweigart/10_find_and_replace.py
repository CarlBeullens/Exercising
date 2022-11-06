
# making use of replace function in Python
def find_and_replace(text, old_text, new_text):
    
    if old_text in text:
        new = text.replace(old_text, new_text)
    return new

# making no use of replace function in Python
def find_and_replace_2(text, old_text, new_text):
    pass
    
    
assert find_and_replace("The fox", "fox", "dog") == "The dog"
assert find_and_replace("fox", "fox", "dog") == "dog"
assert find_and_replace("Firefox", "fox", "dog") == "Firedog"
assert find_and_replace("foxfox", "fox", "dog") == "dogdog"
assert find_and_replace("The Fox and fox.", "fox", "dog") == "The Fox and dog."


