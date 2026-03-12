import pytest
from main import update_game_state

# --- Helpers ---
def make_display(word: str) -> list[str]:
    """Build initial masked display, preserving spaces and hyphens."""
    return [c if c in (" ", "-") else "_" for c in word]


# --- Input Validation ---
class TestInputValidation:
    def test_digit_rejected(self):
        _, _, _, result = update_game_state(list("hat"), [], "1", 6, make_display("hat"))
        assert result == "wrong input"

    def test_symbol_rejected(self):
        _, _, _, result = update_game_state(list("hat"), [], "!", 6, make_display("hat"))
        assert result == "wrong input"

    def test_empty_string_rejected(self):
        _, _, _, result = update_game_state(list("hat"), [], "", 6, make_display("hat"))
        assert result == "wrong input"

    def test_valid_letter_accepted(self):
        _, _, _, result = update_game_state(list("hat"), [], "h", 6, make_display("hat"))
        assert result != "wrong input"


# --- Duplicate Guesses ---
class TestDuplicateGuesses:
    def test_duplicate_letter_returns_already(self):
        _, _, _, result = update_game_state(list("hat"), ["h"], "h", 6, make_display("hat"))
        assert result == "already"

    def test_duplicate_does_not_decrement_lives(self):
        lives, _, _, _ = update_game_state(list("hat"), ["z"], "z", 5, make_display("hat"))
        assert lives == 5

    def test_duplicate_does_not_grow_guessed_list(self):
        _, guessed, _, _ = update_game_state(list("hat"), ["h"], "h", 6, make_display("hat"))
        assert guessed.count("h") == 1


# --- Single Letter: Correct ---
class TestCorrectLetter:
    def test_result_code(self):
        _, _, _, result = update_game_state(list("hat"), [], "a", 6, make_display("hat"))
        assert result == "correct"

    def test_lives_unchanged(self):
        lives, _, _, _ = update_game_state(list("hat"), [], "a", 6, make_display("hat"))
        assert lives == 6

    def test_display_updated(self):
        _, _, display, _ = update_game_state(list("hat"), [], "a", 6, make_display("hat"))
        assert display == ["_", "a", "_"]

    def test_all_occurrences_revealed(self):
        """Correct letter reveals every occurrence, not just the first."""
        _, _, display, _ = update_game_state(list("banana"), [], "a", 6, make_display("banana"))
        assert display == ["_", "a", "_", "a", "_", "a"]

    def test_letter_added_to_guessed(self):
        _, guessed, _, _ = update_game_state(list("hat"), [], "a", 6, make_display("hat"))
        assert "a" in guessed


# --- Single Letter: Incorrect ---
class TestIncorrectLetter:
    def test_result_code(self):
        _, _, _, result = update_game_state(list("hat"), [], "z", 6, make_display("hat"))
        assert result == "incorrect"

    def test_lives_decremented(self):
        lives, _, _, _ = update_game_state(list("hat"), [], "z", 6, make_display("hat"))
        assert lives == 5

    def test_display_unchanged(self):
        original = make_display("hat")
        _, _, display, _ = update_game_state(list("hat"), [], "z", 6, original.copy())
        assert display == ["_", "_", "_"]

    def test_letter_added_to_guessed(self):
        _, guessed, _, _ = update_game_state(list("hat"), [], "z", 6, make_display("hat"))
        assert "z" in guessed


# --- Full Word Guess ---
class TestFullWordGuess:
    def test_correct_word_wins(self):
        _, _, _, result = update_game_state(list("hat"), [], "hat", 6, make_display("hat"))
        assert result == "win"

    def test_correct_word_lives_unchanged(self):
        lives, _, _, _ = update_game_state(list("hat"), [], "hat", 6, make_display("hat"))
        assert lives == 6

    def test_incorrect_word_costs_life(self):
        lives, _, _, result = update_game_state(list("hat"), [], "cat", 6, make_display("hat"))
        assert result == "incorrect"
        assert lives == 5

    def test_partial_word_rejected(self):
        _, _, _, result = update_game_state(list("banana"), [], "ban", 6, make_display("banana"))
        assert result == "incorrect"


# --- Known Bug: multi-word guesses ---
class TestKnownBugs:
    def test_ice_cream_full_word_blocked_by_validation(self):
        """
        BUG: 'ice cream' contains a space, so full-word guess fails isalpha() check.
        This test documents the current (broken) behaviour.
        Remove/update once the bug is fixed.
        """
        word = list("ice cream")
        _, _, _, result = update_game_state(word, [], "ice cream", 6, make_display("ice cream"))
        assert result == "wrong input"  # expected WRONG behaviour — should be "win"


# --- Invariants ---
class TestInvariants:
    def test_display_length_preserved(self):
        word = list("hangman")
        display = make_display("hangman")
        _, _, new_display, _ = update_game_state(word, [], "a", 6, display)
        assert len(new_display) == len(word)

    def test_lives_never_exceed_max(self):
        lives, _, _, _ = update_game_state(list("hat"), [], "a", 6, make_display("hat"))
        assert lives <= 6

    def test_secret_word_not_mutated(self):
        word = list("hangman")
        original = word.copy()
        update_game_state(word, [], "a", 6, make_display("hangman"))
        assert word == original
