"""A simple number-guessing game.

The computer picks a random number from 1 to 100 and the player tries to
guess it. After each guess the game reports whether the guess was too high
or too low, and counts how many guesses it took to win.
"""

import random

LOW = 1
HIGH = 100


def check_guess(guess, answer):
    """Compare a guess against the answer.

    Returns "high" if the guess is greater than the answer, "low" if it is
    less than the answer, and "correct" if they match. Kept separate from the
    I/O loop so it can be tested in isolation.
    """
    if guess > answer:
        return "high"
    if guess < answer:
        return "low"
    return "correct"


def prompt_guess():
    """Ask the player for a guess, repeating until they enter a valid number."""
    while True:
        raw = input(f"Guess a number ({LOW}-{HIGH}): ")
        try:
            return int(raw)
        except ValueError:
            print("Please enter a whole number.")


def play():
    """Run one game from start to finish."""
    answer = random.randint(LOW, HIGH)
    guesses = 0

    print(f"I'm thinking of a number between {LOW} and {HIGH}.")

    while True:
        guess = prompt_guess()
        guesses += 1

        result = check_guess(guess, answer)
        if result == "high":
            print("Too high!")
        elif result == "low":
            print("Too low!")
        else:
            word = "guess" if guesses == 1 else "guesses"
            print(f"Correct! You got it in {guesses} {word}. Congratulations!")
            return


if __name__ == "__main__":
    play()
