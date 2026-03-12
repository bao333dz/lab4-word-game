# Lab 4 — Word Game (Hangman)

A terminal-based Hangman game written in Python.

## Requirements

- Python 3.10+
- pytest (for tests only): `pip install pytest`

## How to Run the Game

```bash
python main.py
```

You will be prompted to guess a letter or the whole word. You have **6 lives**.  
Spaces and hyphens in multi-word entries (e.g. `ice cream`) are revealed automatically.

## How to Run the Tests

```bash
pytest test_main.py -v
```

Tests cover:
- Input validation (digits, symbols, empty string)
- Duplicate guess detection
- Correct/incorrect letter guesses
- Full word guesses (win/lose)
- Known bug: full-word guesses with spaces/hyphens fail validation
- Game invariants (display length, lives ceiling, word immutability)

## Project Structure

```
main.py         # Game logic and main loop
test_main.py    # Pytest test suite for update_game_state()
MY_NOTES.md     # Design notes: states, variables, rules, bugs
JOURNAL.md      # Interaction log
.gitignore      # Excludes __pycache__ and pytest cache
```

## Known Bug

Words containing spaces (`ice cream`) or hyphens (`jack-o-lantern`) cannot be guessed as a full word due to `str.isalpha()` rejecting those characters. Fix planned.
