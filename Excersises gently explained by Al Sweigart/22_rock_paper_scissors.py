import random

def rsp_winner(player1: str, player2: str) -> str:
    
    """Simple rock paper scissors game

    Returns:
        _type_: String indicating the player who wins or a tie.
    """
    
    match player1, player2:
        case "paper", "rock":
            return "player one"
        case "rock", "scissors":
            return "player one"        
        case "scissors", "paper":
            return "player one"
        case "rock", "paper":
            return "player two"
        case "scissors", "rock":
            return "player two"
        case "paper", "scissors":
            return "player two"
        case "paper", "paper":
            return "tie"
        case "scissors", "scissors":
            return "tie"
        case "rock", "rock":
            return "tie"

assert rsp_winner('rock', 'paper') == 'player two'
assert rsp_winner('rock', 'scissors') == 'player one'
assert rsp_winner('paper', 'scissors') == 'player two'
assert rsp_winner('paper', 'rock') == 'player one'
assert rsp_winner('scissors', 'rock') == 'player two'
assert rsp_winner('scissors', 'paper') == 'player one'
assert rsp_winner('rock', 'rock') == 'tie'
assert rsp_winner('paper', 'paper') == 'tie'
assert rsp_winner('scissors', 'scissors') == 'tie'

moves = ["paper", "scissors", "rock"]


def main():
    for _ in range(10):
        print(rsp_winner(random.choice(moves), random.choice(moves)))
        

if __name__ == "__main__":
    main()
    