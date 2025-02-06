import random

def number_guessing_game():
    random_number = random.randint(1, 100)  # Générer un nombre entre 1 et 100
    max_attempts = 7  # Nombre d'essais maximum

    print(" Welcome to the Number Guessing Game!")
    print(f"You have {max_attempts} attempts to guess the number between 1 and 100.")

    for attempt in range(1, max_attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}/{max_attempts}: Enter your guess (1-100): "))

            if guess < 1 or guess > 100:
                print("Out of bounds! Please enter a number between 1 and 100.")
                continue  # Redemander un nombre sans compter cet essai

            if guess < random_number:
                print("Too low! Try again.")
            elif guess > random_number:
                print("Too high! Try again.")
            else:
                print(f" Congratulations! You guessed the number {random_number} in {attempt} attempts!")
                break  # Fin du jeu si la réponse est correcte

        except ValueError:
            print(" Invalid input! Please enter a number.")

    else:
        print(f" Game over! The correct number was {random_number}.")

# Lancer le jeu
number_guessing_game()