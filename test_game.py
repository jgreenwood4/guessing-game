"""Tests for the check_guess function.

Run these with:

    pytest

or, if pytest isn't installed:

    python -m pytest

pytest automatically discovers any file named test_*.py and runs every
function inside it whose name starts with "test_". Each test makes some
assertions; if an assert fails, pytest reports that test as a failure.
"""

from game import check_guess


def test_guess_above_answer_returns_high():
    # When the guess (50) is GREATER than the answer (10), the function
    # should report "high" — i.e. the player guessed too high.
    assert check_guess(50, 10) == "high"


def test_guess_below_answer_returns_low():
    # When the guess (5) is LESS than the answer (10), the function
    # should report "low" — i.e. the player guessed too low.
    assert check_guess(5, 10) == "low"


def test_guess_equal_to_answer_returns_correct():
    # When the guess (10) exactly EQUALS the answer (10), the function
    # should report "correct" — the player won.
    assert check_guess(10, 10) == "correct"


def test_boundary_values():
    # A quick check at the edges of the game's range (1 and 100) to make
    # sure the comparison still works at the smallest and largest numbers.
    assert check_guess(100, 1) == "high"   # 100 is above 1
    assert check_guess(1, 100) == "low"    # 1 is below 100
    assert check_guess(1, 1) == "correct"  # 1 equals 1
