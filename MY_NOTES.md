# APP STATES
A Hangman-style Word Game usually needs these core states:

START
Load/setup game data, choose a secret word, reset tries and guessed letters.

SHOW_STATUS
Display current masked word (_ a _ _), wrong guesses left, and guessed letters.

GET_GUESS
Ask the player for input (letter or full word).

VALIDATE_INPUT
Check input rules: one letter, alphabetic, not already guessed, etc.

PROCESS_GUESS
Compare guess to secret word and update state:

correct letter -> reveal positions
wrong letter -> reduce attempts
repeated guess -> warning/no penalty (your rule)
CHECK_END_CONDITION
Decide if game should continue or end:
all letters revealed -> WIN
attempts exhausted -> LOSE
otherwise -> back to SHOW_STATUS
WIN
Show victory message and final word.

LOSE
Show loss message and reveal secret word.

PLAY_AGAIN
Ask whether to start a new round or exit.

EXIT
Terminate cleanly.

# APP VARIABLES
secret_word: str
The word to guess.

masked_word: list[str] or display_word: str
Current revealed view (example: ["_", "a", "_", "_"]).

guessed_letters: set[str]
All letters already guessed (for duplicate checks).

correct_letters: set[str]
Letters guessed that are in the word.

wrong_letters: set[str]
Letters guessed that are not in the word.

max_attempts: int
Total wrong guesses allowed (example: 6).

attempts_left: int
Remaining wrong guesses.

game_state: str
Current state from your state list (START, GET_GUESS, WIN, etc.).

current_guess: str
The player’s latest input before processing.

is_word_guessed: bool
True when all letters are revealed.

play_again: bool
Controls whether a new round starts after WIN/LOSE.

Useful optional ones:

word_list: list[str]
Pool of possible words.

round_number: int
Track how many games were played.

wins: int and losses: int
Simple scoreboard.

input_error: str | None
Stores validation message to show user.

# APP RULES AND INVARIANTS
secret_word is fixed during a round.
It is chosen at START and never changes until next round.

attempts_left is always between 0 and max_attempts.
Invariant: 0 <= attempts_left <= max_attempts.

Only new wrong guesses reduce attempts.
A repeated wrong letter should not reduce attempts_left again.

guessed_letters contains unique lowercase letters only.
Invariant: no duplicates, no non-letters.

correct_letters and wrong_letters are disjoint.
Invariant: correct_letters ∩ wrong_letters = ∅.

guessed_letters is the union of correct and wrong letters.
Invariant: guessed_letters = correct_letters ∪ wrong_letters.

A letter is in correct_letters iff it exists in secret_word.
No incorrect classification allowed.

masked_word length always equals secret_word length.
Invariant: len(masked_word) == len(secret_word).

Revealed characters in masked_word must match secret_word at same index.
Unknown positions stay as _ (or your chosen placeholder).

Win condition is exact and deterministic.
WIN iff all unique letters in secret_word are guessed
(or masked_word == secret_word).

Lose condition is exact and deterministic.
LOSE iff attempts_left == 0 and game is not already won.

Input validation must happen before processing.
Only valid guesses can update letters/attempts/state.

State transitions follow the state machine only.
No skipping directly from GET_GUESS to WIN/LOSE without check logic.

Round-end states are terminal until PLAY_AGAIN.
After WIN or LOSE, no further guess processing in that round.

Case-insensitive gameplay.
Normalize input and word comparison (commonly lowercase).

# APP BUGS
Repeated wrong guess reduces lives again
Should usually warn only; no extra penalty.

Case-sensitivity mismatch
A and a treated differently if you forget normalization.

Guess validation too weak
Accepting empty input, numbers, symbols, or multi-char letter guesses unintentionally.

Off-by-one in attempts
Game ends one guess too early or allows one extra wrong guess.

Win condition checks full string incorrectly
Comparing masked word with spaces/formatting can fail even when solved.

Not revealing all occurrences of a correct letter
Guessing a in banana reveals only one a instead of all.

Penalizing correct full-word guesses accidentally
If full-word mode exists, logic may decrement attempts before checking match.

Duplicate state updates in one turn
A guess gets processed twice because of loop/state-transition errors.

Bad transition order
Checking LOSE before WIN can report loss on the final correct guess at 0 attempts edge cases.

Inconsistent tracking sets
guessed_letters, correct_letters, and wrong_letters drift out of sync.

Hidden word not reset between rounds
Old letters/lives carry into the next game due to missed reinitialization.

Mutating secret_word accidentally
Converting/overwriting it during processing breaks future checks.

Unicode/accent handling issues
Words like cafe vs café fail unless normalization rules are clear.

Input whitespace bugs
" a " or newline chars cause false invalid or mismatch checks.

Non-deterministic random choice in tests
Tests become flaky if word selection isn’t seeded/mocked.

Infinite loop on invalid input
State never advances or never reprompts correctly.

Wrong display synchronization
masked_word and rendered display string diverge after updates.

Scoreboard/accounting bugs
Wins/losses increment in wrong state or increment twice.

Full-word guess bypasses guessed-letter history
Player can repeatedly spam full guesses without intended penalties/rules.

Terminal end-state still accepts guesses
After WIN/LOSE, input loop continues modifying game state.

# My notes
## Coding by myself
Firstly, I just code the game by myself without the help of anything, manage to did it, everything working fine
## Asking AI
Then I ask Gemini to compare my current code of the requirements of the assignment and then I fix what is needed
## Check the instruction file 1 last time
Finally I go through the instruction file up and down one last time to make sure I did everything is all good

## Auto play
I gonna put the option of auto play at the start of each play
Then if the user type ok, auto play start, it will randomly choose a random word from the alphabet
Then the chosen word is popped out of the alphabet so that it wont choose itself again