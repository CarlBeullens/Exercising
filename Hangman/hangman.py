# Program representing hangman including visuals.

import hangman_visual, random, string

ALPHABET_UPPER = set(string.ascii_uppercase)
 
def _get_word() -> str:
    with open ("words.txt", "r") as f:
        words = f.readlines()
   
    return random.choice(words).rstrip().upper()

  
def game_logic(word, letters_in_word, chosen_letters, lives=7):
    while True:
        word_in_progress = ""
        chosen_letter = input("\nPlease choose a letter. ").upper()
        
        if not chosen_letter.isalpha():
            print("\nChoose from the alphabet only")
            continue
            
        elif chosen_letter in ALPHABET_UPPER - chosen_letters:
            chosen_letters.add(chosen_letter)
                
            if chosen_letter in letters_in_word:
                letters_in_word.remove(chosen_letter)
                    
            else:
                lives -= 1 
                print(f"\nLetter not in the word. You have {lives} lives left.")    
                    
        elif chosen_letter in chosen_letters:
            print("\nYou already chose this letter, choose another one.")
                
        for letter in word:
            if letter in chosen_letters:
                word_in_progress += letter + " "
            else:
                word_in_progress += "- "
                    
        print(word_in_progress)
        print(hangman_visual.lives_visual_dict[lives])
        
        if lives == 0:
            print(f"\nSorry, no more lives! Answer was {word}.")
            break
        
        if len(letters_in_word) == 0:
            print(f"\nYou guessed the word, {word}.")
            break
        
    
def game_loop():
    print("Let's play. You have 6 attempts to guess a random word.")
    while True:
        word = _get_word()
        letters_in_word = set(word)
        chosen_letters = set()
        lives = 7        
        game_logic(word, letters_in_word, chosen_letters)
        if input("Enter \"q\" to quit or any key to play again. ") == "q":
            break

    print("\nGoodbye!")
   
    
if __name__ == '__main__':
    game_loop()
    
