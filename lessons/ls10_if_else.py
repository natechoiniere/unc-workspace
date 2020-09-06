"""Example of if-then-else statements."""

author = "730443739"

THE_ANSWER_TO_LIFE_THE_UNIVERSE_AND_EVERYTHING: int = 42

print("Guess a number...")

guess: int = int(input("Your Guess: "))

if guess == THE_ANSWER_TO_LIFE_THE_UNIVERSE_AND_EVERYTHING:
    print("Your guess is the answer to life, the universe, and everything.")
else:
    print("Your answer is incorrect.")

print("Game over.")