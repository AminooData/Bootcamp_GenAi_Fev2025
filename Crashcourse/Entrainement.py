# Exercice 1
Name = "Alice"
Age = 30 
city = "New York"
print(f"Je m'appelle {Name}, j'ai {Age} ans et j'habite à {city}.")  # Affiche "Je m'appelle Alice, j'ai 30 ans et j'habite à New York."

# Exercice 2

age = int(input("Quel âge avez-vous ? "))  # Demande à l'utilisateur son âge
years_until_100 = 100 - age  # Calcule le nombre d'années restantes jusqu'à 100
print(f"Vous aurez 100 ans dans {years_until_100} ans.")  # Affiche le message

# # Exercice 3
# Ask the user for a number between 1 and 100
# If the number is a multiple of three, print Fizz
# If the number is a multiple of five, print Buzz.
# If the number is a multiple is a multiples of both three and five, print FizzBuzz instead.
#
input_number = int(input("Entrez un nombre entre 1 et 100: "))  # Demande à l'utilisateur un nombre
if input_number % 3 == 0 and input_number % 5 == 0:  # Vérifie si le nombre est un multiple de 3 et 5
    print("FizzBuzz")  # Affiche FizzBuzz
elif input_number % 3 == 0:
    print("Fizz")  # Affiche Fizz
elif input_number % 5 == 0:
    print("Buzz")  # Affiche Buzz
else:
    print(input_number)
    
# Exercice 4
# Find the largest among three numbers using if else and display it.
number1 = 10
number2 = 20
number3 = 30
if number1 >= number2 and number1 >= number3:
    print(f"{number1} est le plus grand.")
elif number2 >= number1 and number2 >= number3:
    print(f"{number2} est le plus grand.")
else:
    print(f"{number3} est le plus grand.")
    
# Exercice 5