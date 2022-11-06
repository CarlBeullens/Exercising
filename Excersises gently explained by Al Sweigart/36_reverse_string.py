
from distutils import text_file


def reverse_string(text: str) -> str:
    
    text_as_list = list(text)
    reversed_text_as_list = list()
    
    for i in range(len(text_as_list) - 1, -1, -1):
        reversed_text_as_list.append(text_as_list[i])
        
    return "".join(reversed_text_as_list)


print(reverse_string("Hello"))

assert reverse_string("Hello World") == "dlroW olleH"
assert reverse_string("") == ""
assert reverse_string("aaazzz") == "zzzaaa"
assert reverse_string("xxxx") == "xxxx"
assert reverse_string("Test") == "tseT"
assert reverse_string("Belgium") == "muigleB"