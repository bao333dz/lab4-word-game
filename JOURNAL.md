# This JOURNAL.md file gets automatically updated by the journal-logger agent after every interaction with CoPilot. It serves as a comprehensive log of all prompts, responses, changes made, and reflections during the development process. Each entry is formatted consistently for easy reading and is listed in reverse chronological order, with the most recent interactions at the top.

---

## New Interaction

**Date**: 03-12-2026 14:30

**User**: bao.duong@epita.fr

**Prompt**: What are possible bugs in Word Guess / Hangman implementations?

**CoPilot Mode**: Ask

**CoPilot Model**: Claude Haiku 4.5

**Changes Made**: 
- Documented 20 common bug patterns in Hangman/Word Guess implementations
- Provided practical bug categories related to game states, invariants, and edge cases
- Offered to convert into pre-release testing checklist format

**Reasons for Changes**: 
- Proactive bug identification helps prevent implementation errors during coding
- Bugs documented are directly tied to the app rules/invariants previously established
- Reference guide for testing strategy and code review

**Context**: 
- User building word game implementation in lab4-word-game
- Started with app architecture (states, variables, rules) and now documenting edge cases
- Bug prevention strategy before actual implementation begins

**My Observations**:
- Common themes: state management issues, data structure drift, boundary cases, input validation
- Most bugs stem from incomplete state normalization or missed synchronization between tracking sets

---

## New Interaction

**Date**: 03-12-2026 14:20

**User**: bao.duong@epita.fr

**Prompt**: What are the rules and invariants?

**CoPilot Mode**: Ask

**CoPilot Model**: Claude Haiku 4.5

**Changes Made**: 
- Documented 15 core rules and invariants for Hangman game logic
- Covered state constraints, data integrity, win/lose conditions, and input rules
- Added to APP RULES AND INVARIANTS section in MY_NOTES.md

**Reasons for Changes**: 
- Formal invariants prevent logic bugs and state corruption
- Clear rules enable consistent testing and validation
- Foundation for assertions/unit tests later during implementation

**Context**: 
- Building design document for lab4-word-game before implementation
- Following AI4SE incremental design practice (states → variables → rules)

**My Observations**:
- Invariants naturally follow from state machine design; they act as contracts between state handlers

---

## New Interaction

**Date**: 03-12-2026 14:10

**User**: bao.duong@epita.fr

**Prompt**: What variables should I keep track of?

**CoPilot Mode**: Ask

**CoPilot Model**: Claude Haiku 4.5

**Changes Made**: 
- Documented 14 core variables and 4 optional tracking variables for Hangman game
- Provided descriptions and type hints for each variable
- Added to APP VARIABLES section in MY_NOTES.md

**Reasons for Changes**: 
- Clear variable inventory prevents scope creep and forgotten state
- Type hints aid code clarity and IDE support
- Variables directly support the app states defined earlier

**Context**: 
- Second part of design phase after app states were established
- Variables needed to represent game state across all state transitions

**My Observations**:
- Set data structures (`guessed_letters`, `correct_letters`, `wrong_letters`) provide efficient uniqueness constraints
- Optional variables (scoreboard, round tracking) enable extensibility without cluttering core logic

---

## New Interaction

**Date**: 03-12-2026 14:00

**User**: bao.duong@epita.fr

**Prompt**: What states does a Word Game like Hangman game need?

**CoPilot Mode**: Ask

**CoPilot Model**: Claude Haiku 4.5

**Changes Made**: 
- Documented 10 core app states for Hangman implementation
- Added to APP STATES section in MY_NOTES.md
- Provided state transition guidance (e.g., CHECK_END_CONDITION branches to WIN/LOSE or back to SHOW_STATUS)

**Reasons for Changes**: 
- Explicit state machine prevents ambiguous control flow
- Foundation for organizing game loop logic
- States correspond to discrete game phases (setup, gameplay, resolution)

**Context**: 
- User initiating design phase for lab4-word-game project
- Following incremental design-before-code approach from AI4SE curriculum

**My Observations**:
- Clean separation between data display (SHOW_STATUS), input (GET_GUESS), validation (VALIDATE_INPUT), and processing (PROCESS_GUESS) avoids monolithic state handlers
- Terminal states (WIN, LOSE) explicitly prevent further processing until PLAY_AGAIN decision made

---

## New Interaction

**Date**: 03-02-2026 11:00

**User**: bao.duong@epita.fr

**Prompt**: Implement a recursive Fibonacci function in main.py → do the dp bottom up approach

**CoPilot Mode**: Edit

**CoPilot Model**: Claude Haiku 4.5

**Changes Made**: 
- Implemented `fibonacci_dp_bottom_up(n)` function in main.py using dynamic programming bottom-up approach
- Added comprehensive docstring with time/space complexity analysis
- Included test harness with 10 test cases (n=0 to n=9)
- Function verified to produce correct Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

**Reasons for Changes**: 
- Bottom-up DP provides O(n) time complexity (vs exponential for naive recursion)
- Builds solution iteratively from base cases upward, avoiding redundant calculations
- Uses array storage for previously computed values, enabling efficient lookup

**Context**: 
- User refined initial recursive requirement to specify DP bottom-up algorithm
- Implementation tested and verified to work correctly with edge cases (n=0, n=1)
- Algorithm suitable for larger Fibonacci values without stack overflow risk

**My Observations**:

---

## New Interaction

**Date**: 03-02-2026 10:58

**User**: bao.duong@epita.fr

**Prompt**: Read the ai4se.instructions.md file and follow its directive. Activate the journal agent in journal-logger.agent.md

**CoPilot Mode**: Ask

**CoPilot Model**: Claude Haiku 4.5

**Changes Made**: 
- Activated journal-logger agent by setting user email in journal-logger.agent.md
- Logged initial activation entry in JOURNAL.md
- Reviewed ai4se.instructions.md and journal-logger.agent.md directives

**Reasons for Changes**: 
- Established persistent user identity for all future journal entries
- Initialized comprehensive logging system to track all CoPilot interactions, changes, and rationale
- Ensured alignment with repository's AI4SE tutor mode and incremental implementation policies

**Context**: 
- User workspace located in d:\code with lab4-word-game project
- Repository implements AI4SE practices with tutor-focused interaction model
- Journaling system configured to log each interaction with timestamp, mode, model, and contextual information

**My Observations**:

