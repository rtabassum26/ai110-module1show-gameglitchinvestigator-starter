from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


# --- Tests for fixed bugs in logic_utils.py ---

from logic_utils import update_score


def test_check_guess_too_high_outcome():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_check_guess_too_low_outcome():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_check_guess_win_outcome():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"


def test_check_guess_handles_string_secret():
    # Regression: the secret used to be passed as a str on even attempts
    assert check_guess(60, "50")[0] == "Too High"
    assert check_guess(40, "50")[0] == "Too Low"
    assert check_guess(50, "50")[0] == "Win"


def test_too_high_decreases_score_by_5():
    # Regression: "Too High" used to add 5 points on even attempts
    for attempt in range(1, 9):
        assert update_score(100, "Too High", attempt) == 95


def test_too_low_decreases_score_by_5():
    for attempt in range(1, 9):
        assert update_score(100, "Too Low", attempt) == 95
