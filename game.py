import random


def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I have picked a random number between 1 and 100. Can you guess it?")

    # Pick a random number from 1 to 100
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            # Get the player's input
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Check the guess against the secret number
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(
                    f"🎉 Congratulations! You guessed the number in {attempts} attempts!"
                )
                break
        except ValueError:
            print("Invalid input. Please enter a whole number between 1 and 100.")


if __name__ == "__main__":
    number_guessing_game()