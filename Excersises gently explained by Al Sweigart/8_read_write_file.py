
def writeToFile(filename, text):
    with open(filename, "w") as f:
        f.write(text)

def appendToFile(filename, text):
    with open(filename, "a") as f:
        f.write(text)

def readFromFile(filename):
    with open(filename, "r") as f:
        return f.read()


writeToFile('greet.txt', 'Hello!\n')
appendToFile('greet.txt', 'Goodbye!\n')
assert readFromFile("greet.txt") == "Hello!\nGoodbye!\n"