# Program to play a game of rock paper scissors vs the computer.

import random

def get_human_move():
    # input human
    return input("rock paper or scissors: ")

def get_computer_move():
    # input computer
    computer_move = random.choice(["rock", "paper", "scissors"])
    print(f"computer: {computer_move}")
    return computer_move
    
def get_winner(human_move, computer_move):
    # game logic to define winner
    match human_move , computer_move:
        case "rock" , "scissors":
            return "you win"
        case "paper" , "rock":
            return "you win"
        case "scissors" , "paper":
            return "you win"
        case "scissors" , "rock":
            return "computer wins"
        case "rock" , "paper":
            return "computer wins"
        case "paper" , "scissors":
            return "computer wins"
        case _:
            return "tie"
     
def play():
    # game loop   
    while True:
        human_move = get_human_move()
        computer_move = get_computer_move()
        winner = get_winner(human_move, computer_move)
        print(winner)
        if input("Press any key to keep playing or 'q' to exit ") == "q":
            break
              
if __name__ == "__main__":
    play()
