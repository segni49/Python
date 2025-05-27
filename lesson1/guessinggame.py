hidden_word = "python"
def play_game():
    print("Welcome to the Guessing Game!")
    print("Try to guess the hidden word.")
    
    attempts = 0
    while True:
        guess = input("Enter your guess: ").lower()
        attempts += 1

        if guess == hidden_word:
            print(f"Congratulations! You've guessed the word '{hidden_word}' in {attempts} attempts.")
            break
        elif attempts == 3:
            print(f"Sorry, you've used all your attempts. The hidden word was '{hidden_word}'.")
            break
        else:
            print("Incorrect guess, try again.")
            
play_game()           