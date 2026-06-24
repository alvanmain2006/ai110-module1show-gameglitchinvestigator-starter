"""Regression tests for the bugs fixed in the Game Glitch Investigator.

Each test group maps to a specific bug we fixed in app.py / logic_utils.py.
"""

from logic_utils import check_guess


# ---------------------------------------------------------------------------
# Bug 1: "Go HIGHER / Go LOWER" hints were swapped.
#
# A guess ABOVE the secret must tell the player to go LOWER, and a guess
# BELOW the secret must tell them to go HIGHER. The original code had these
# messages reversed.
# ---------------------------------------------------------------------------

def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"


def test_guess_too_high_says_go_lower():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_guess_too_low_says_go_higher():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


# ---------------------------------------------------------------------------
# Bug 2: the secret was stringified on even attempts (str(secret)), which made
# check_guess compare numbers lexicographically instead of numerically.
#
# Lexicographically "9" > "50" is True, so a too-low guess of 9 would wrongly
# be reported as "Too High". These tests pin down NUMERIC comparison, which
# only holds because the secret is now always passed as an int.
# ---------------------------------------------------------------------------

def test_single_digit_below_two_digit_secret_is_too_low():
    # 9 < 50 numerically -> "Too Low". String comparison would say "Too High".
    outcome, _ = check_guess(9, 50)
    assert outcome == "Too Low"


def test_two_digit_above_single_digit_secret_is_too_high():
    # 50 > 9 numerically -> "Too High". String comparison would say "Too Low".
    outcome, _ = check_guess(50, 9)
    assert outcome == "Too High"


def test_exact_match_wins_for_two_digit_number():
    # The stringify bug also prevented wins, since int == str is always False.
    outcome, _ = check_guess(42, 42)
    assert outcome == "Win"
