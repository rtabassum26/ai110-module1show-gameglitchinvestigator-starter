
# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

An AI-generated number guessing game built with Streamlit contained several bugs that affected gameplay. The objective of this project was to identify these issues, fix the underlying logic, and verify the changes through manual and automated testing.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the application: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Use the Developer Debug Info section to observe the secret number, attempts, score, and guess history.
2. **Identify the bugs.** Investigate incorrect hints, inconsistent scoring, problems with starting a new game, and outdated interface information.
3. **Fix the logic.** Correct the guessing and scoring behavior while preserving the original interface.
4. **Refactor & Test.** Move the game logic into `logic_utils.py` and use pytest to verify the fixes.

## 📝 Document Your Experience

- [x] **Game purpose:** The game allows players to guess a randomly generated number within a limited number of attempts. Players receive hints after each guess and earn a score based on their performance.

- [x] **Bugs identified:** The original game displayed incorrect remaining attempts, reversed the high/low hints, and prevented players from properly starting another game after winning. The input field also retained the previous guess, and the Developer Debug Info section did not immediately display the latest guess.

- [x] **Fixes applied:** I corrected the guessing and scoring logic, fixed the new game functionality, and cleared the input field whenever a new game starts. I also updated the attempt counter and debug information to reflect the current game state. The core game logic was moved into `logic_utils.py` to separate it from the Streamlit interface.

## 📸 Demo Walkthrough

The following example assumes the secret number is 50 on Normal difficulty.

1. The player starts a new game with 8 attempts available.
2. The player enters 40. The game displays "Too Low" and deducts 5 points.
3. The player enters 60. The game displays "Too High" and deducts another 5 points.
4. The player enters 50. The game displays "Correct!" and awards points based on the number of attempts.
5. The game displays the winning message and final score.
6. The player clicks "New Game" to reset the attempts, guess history, and input field.

The Developer Debug Info section displays the secret number, attempts, score, selected difficulty, and guess history.

## 🧪 Test Results

All 9 pytest tests passed after correcting the AI-generated test assertions to match the return values of `check_guess()`.

```text
9 passed
```

## 🚀 Stretch Features

- [ ] Challenge 4: Enhanced UI (not completed)
