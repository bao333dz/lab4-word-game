"""Hangman word-guessing game.

States: START → SHOW_STATUS → GET_GUESS → VALIDATE_INPUT → PROCESS_GUESS → CHECK_END → WIN/LOSE → PLAY_AGAIN
"""
import random
import time

def update_game_state(secret_word_chars: list[str], guessed_letters: list[str], guess: str, lives: int, display: list) -> tuple[int, list[str], list, str]:
    """Process a player guess and update game state.
    
    Args:
        secret_word_chars: Secret word as list of chars
        guessed_letters: All guessed letters so far
        guess: Current player input (letter or word)
        lives: Remaining wrong guesses
        display: Current masked word display
    
    Returns:
        (lives, guessed_letters, display, result_code)
        result_code: 'wrong input', 'already', 'correct', 'incorrect', 'win'
    
    Note: Input validation rejects multi-char guesses with spaces/hyphens (bug for words like 'ice cream')
    """
    if not guess.isalpha():
        return lives, guessed_letters, display, "wrong input"

    # Prevent duplicate guesses
    if guess in guessed_letters:
        return lives, guessed_letters, display, "already"

    guessed_letters.append(guess)

    # Whole word guess
    if len(guess) > 1:
        if guess == "".join(secret_word_chars):
            return lives, guessed_letters, secret_word_chars, "win"
        else:
            lives -= 1
            return lives, guessed_letters, display, "incorrect"

    # Single letter guess: reveal all occurrences
    if guess in secret_word_chars:
        for q in range(len(secret_word_chars)):
            if secret_word_chars[q] == guess:
                display[q] = guess
        return lives, guessed_letters, display, "correct"
    else:
        lives -= 1
        return lives, guessed_letters, display, "incorrect"

def run_game() -> None:
    """Run a single round of Hangman."""
    words = ["bungalow", "quartz", "zephyr", "pangolin", "hydrant", "astronaut", "labyrinth", "umbrella", "ice cream", "jack-o-lantern"]
    secret_word = random.choice(words)
    secret_word_chars = list(secret_word)
    
    # Initialize display: reveal spaces/hyphens, mask letters
    display = []
    for char in secret_word_chars:
        if char in ["-", " "]:
            display.append(char)
        else:
            display.append("_")

    guessed_letters = []  # TODO: should be a set for O(1) lookup
    lives = 6
    
    print("\n" + "="*20)
    print("The word is:", "".join(display))
    auto = input("Do you want to turn on auto play? (ok/no):")

    if auto == "no":
        # Main game loop: SHOW_STATUS → GET_GUESS → VALIDATE_INPUT → PROCESS_GUESS → CHECK_END_CONDITION
        while lives > 0 and display != secret_word_chars:
            guess = input("\nInput your guess (letter or whole word): ").lower()

            lives, guessed_letters, display, result = update_game_state(secret_word_chars, guessed_letters, guess, lives, display)

            if result == "wrong input":
                print("Invalid input! Use letters only.")
            elif result == "already":
                print(f"You already guessed '{guess}'!")
            elif result == "correct":
                print("Good guess!")
            elif result == "incorrect":
                print("Wrong!")
            elif result == "win":
                print("Good job mate! You guessed the whole word!")
                break

            print("Current progress:", "".join(display))
            print(f"Lives left: {lives}")
            print(f"Guessed so far: {', '.join(guessed_letters)}")

        # WIN or LOSE state
        if display == secret_word_chars:
            print("\nCongratulations! You won!")
        else:
            print(f"\nGame Over. The word was: {secret_word}")
    elif auto == "ok":
        wordl = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        while lives > 0 and display != secret_word_chars:
            guess = random.choice(wordl)
            norep = guess
            wordl.remove(norep)

            lives, guessed_letters, display, result = update_game_state(secret_word_chars, guessed_letters, guess, lives, display)
            
            time.sleep(3)
            if result == "wrong input":
                print("Invalid input! Use letters only.")
            elif result == "already":
                print(f"You already guessed '{guess}'!")
            elif result == "correct":
                print("Good guess!")
            elif result == "incorrect":
                print("Wrong!")
            elif result == "win":
                print("Good job mate! You guessed the whole word!")
                break

            print("Current progress:", "".join(display))
            print(f"Lives left: {lives}")
            print(f"Guessed so far: {', '.join(guessed_letters)}")

        # WIN or LOSE state
        if display == secret_word_chars:
            print("\nCongratulations! You won!")
        else:
            print(f"\nGame Over. The word was: {secret_word}")


def main() -> None:
    """Main loop: PLAY_AGAIN state."""
    play = "y"
    while play == "y":
        run_game()
        play = input("Play again? (y/n): ").lower()

if __name__ == "__main__":
    main()