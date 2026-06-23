# Number Guessing Game

A small command-line game written in Python. The computer picks a random
number from **1 to 100** and you try to guess it. After each guess the game
tells you whether you were too high or too low, and when you win it shows how
many guesses it took.

## Requirements

- Python 3.6 or newer (no external packages needed)

## How to play

Run the game from a terminal:

```bash
python game.py
```

Then enter a number when prompted. The game responds with one of:

- **Too high!** — your guess was greater than the answer
- **Too low!** — your guess was less than the answer
- **Correct!** — you found it; the game congratulates you and shows your guess count

Keep narrowing your range until you win. A good strategy is to start at 50 and
halve the remaining range each time — you can always win in 7 guesses or fewer.

## Code layout

The core comparison logic lives in its own function so it can be tested
independently of the input/output loop:

```python
check_guess(guess, answer)  # returns "high", "low", or "correct"
```

- `check_guess(guess, answer)` — pure function comparing a guess to the answer
- `prompt_guess()` — reads and validates a number from the player
- `play()` — runs a full game, tracking the guess count

## Testing

Because `check_guess` is a pure function, it is easy to test:

```python
from game import check_guess

assert check_guess(60, 42) == "high"
assert check_guess(10, 42) == "low"
assert check_guess(42, 42) == "correct"
```
