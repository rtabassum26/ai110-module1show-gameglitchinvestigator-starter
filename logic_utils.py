"""Pure game logic for Glitchy Guesser."""


def get_range_for_difficulty(difficulty: str):
    ranges = {"Easy": (1, 20), "Normal": (1, 100), "Hard": (1, 50)}
    return ranges.get(difficulty, (1, 100))


def parse_guess(raw: str):
    if raw is None or not str(raw).strip():
        return False, None, "Enter a guess."
    try:
        return True, int(str(raw).strip()), None
    except ValueError:
        return False, None, "Enter a whole number."


# FIXME (resolved): previously, the guessing logic
# produced incorrect hints die to inconsistent data types.
# Verified the behavior using pytest.
def check_guess(guess, secret):
    guess, secret = int(guess), int(secret)
    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        return "Too High", "📈 Go LOWER!"
    return "Too Low", "📉 Go HIGHER!"


# FIXME (resolved): previously, incorrect guesses could
# sometimes increase the player's score.

def update_score(current_score: int, outcome: str, attempt_number: int):
    if outcome == "Win":
        return current_score + max(10, 100 - 10 * attempt_number)
    if outcome in ("Too High", "Too Low"):
        return current_score - 5
    return current_score
