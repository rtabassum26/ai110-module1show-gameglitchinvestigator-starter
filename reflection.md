
# 💭 Reflection: Game Glitch Investigator

## 1. What was broken when you started?

When I first ran the game, the interface seemed to work fine, but I noticed several issues while playing. The game allowed 8 attempts on Normal difficulty, but initially displayed only 7 remaining attempts. The guessing logic was also reversed, meaning that guessing a number lower than the secret would return "Too High" and vice versa. Another issue was that after winning, the player could not properly start another game because the winning notification continued to appear. I also noticed that the previous guess remained in the input field when starting a new game.

**Bug Reproduction Log**

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Start a game on Normal difficulty | Display 8 remaining attempts | Initially displayed 7 attempts | None observed |
| Guess 8 when the secret is 9 | Display "Too Low" | Displayed "Too High" | Incorrect hint |
| Guess 10 when the secret is 9 | Display "Too High" | Displayed "Too Low" | Incorrect hint |
| Win a game and start another | Start a new game without the previous winning notification | Winning notification continued to appear | None observed |
| Start another game after entering a guess | Clear the previous input | Previous guess remained in the input field | None observed |

During further testing, I discovered two additional issues. The remaining-attempt counter was displaying outdated information, and the Developer Debug Info section did not immediately show the most recent guess. These issues were related to when the interface displayed information relative to updates in the game's session state.

---

## 2. How did you use AI as a teammate?

I used Claude Code in VS Code and ChatGPT to investigate the bugs, suggest fixes, and refactor the code. Initially, I asked Claude to identify problematic sections and suggest changes without modifying the code directly, so I could review and implement them myself. I accepted its suggestion for clearing the input field whenever a new game starts and verified that it worked by testing the interface. However, I rejected its first suggestion for fixing the new game functionality because, although another game could start, the previous winning notification continued to appear. I also had to correct AI-generated pytest tests because they expected a single string instead of the tuple returned by `check_guess()`, which showed me that AI suggestions can be incomplete even when the underlying logic is correct.

---

## 3. Debugging and testing your fixes

I started by manually testing the game and checking whether the actual behavior matched what I expected. After fixing the bugs, I moved the core functions into `logic_utils.py` and used pytest to verify the guessing and scoring logic. Initially, three tests failed because the AI-generated assertions did not account for the two return values of `check_guess()`, so I corrected the tests instead of changing the function. After making those changes, all 9 tests passed, including tests for correct guesses, high/low hints, string inputs, and scoring. I also ran the Streamlit application again and verified that the hints, attempts, score, input field, and new game functionality worked correctly.

---

## 4. What did you learn about Streamlit and state?

I learned that Streamlit reruns the application script whenever a user interacts with certain elements, such as buttons or input fields. Because of this, ordinary variables may be recreated during execution, while `st.session_state` allows the application to preserve important information such as the secret number, attempts, score, and guess history. I also learned that the order in which the interface is rendered matters. For example, the attempt counter and debug information were initially displayed before the latest guess was processed, which caused them to show outdated values. Moving those displays after the game logic helped ensure that the interface reflected the updated state.

---

## 5. Looking ahead: your developer habits

One habit I want to continue is testing individual changes instead of modifying several parts of a program at once. I also found Git's Source Control useful for reviewing changes and understanding exactly what had been modified. Next time, I would give AI more specific instructions and ask it to preserve the existing code structure rather than making unnecessary changes. This project showed me that AI-generated code can be useful, but it still requires careful review, especially when a suggested fix introduces another problem. I think the most important lesson was learning to treat AI as an assistant whose suggestions need verification rather than as a source of automatically correct solutions.
