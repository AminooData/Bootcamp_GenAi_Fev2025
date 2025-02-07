#Exercise 1
# Utilisation de '\n' pour ajouter un saut de ligne entre chaque "Hello world"
print("Hello world\nHello world\nHello world\nHello world")

#Exercise 2
# Calcul de la puissance : 99 à la puissance 3
puissance = 99 ** 3  

# Multiplication du résultat par 8
resultat = puissance * 8  

# Affichage du résultat final
print(resultat)

#Exercise 3
#  Demande à l'utilisateur d'entrer son prénom
user_name = input("Quel est ton prénom ? ")  

#  Notre prénom pour comparer
my_name = "Amin"  

#  Vérifie si l'utilisateur a le même prénom
if user_name == my_name:  
    print("Wow ! Nous avons le même prénom !")  #  Affiche ce message si les prénoms sont identiques
else:  
    print(f"Oh ! Enchanté, {user_name}, joli prénom !")  #  Affiche un message personnalisé

#Exercise 4

use_tall =int(input("Quelle taille faite vous ?"))

tall = 145

if use_tall >=  tall:
    print("Vous pouvez monter à bord !")
else:
    print("Désolé, vous ne pouvez pas monter à bord !")
    
#Exercise 5
    # Créer un ensemble appelé my_fav_numbers avec tous vos numéros favoris
my_fav_numbers = {7, 14, 21, 28}

# Ajouter deux nouveaux nombres à l'ensemble
my_fav_numbers.add(35)
my_fav_numbers.add(42)

# Supprimer le dernier numéro (les ensembles ne sont pas ordonnés, donc on ne peut pas directement supprimer le "dernier")
# Cependant, on peut supprimer un élément spécifique si on le connaît
my_fav_numbers.discard(42)  # Supprime 42 si présent

# Créer un ensemble appelé friend_fav_numbers avec les numéros préférés de vos amis
friend_fav_numbers = {3, 6, 9, 12}

# Concaténer my_fav_numbers et friend_fav_numbers vers une nouvelle variable appelée our_fav_numbers
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

# Afficher les résultats
print("Mes numéros favoris:", my_fav_numbers)
print("Les numéros favoris de mes amis:", friend_fav_numbers)
print("Nos numéros favoris combinés:", our_fav_numbers)

# Exercise 6
#  Faux 

# Exercise 7
#  Définition de la liste de départ
basket = ["Banana", "Apples", "Oranges", "Blueberries"]

#  1. Supprimer "Banana" de la liste
basket.remove("Banana")  # La méthode .remove() supprime un élément par son nom

#  2. Supprimer "Blueberries" de la liste
basket.remove("Blueberries")  # On supprime aussi Blueberries de la liste

#  3. Ajouter "Kiwi" à la fin de la liste
basket.append("Kiwi")  # La méthode .append() ajoute un élément à la fin

#  4. Ajouter "Apples" au début de la liste
basket.insert(0, "Apples")  # .insert(position, élément) ajoute "Apples" à l'index 0 (début)

#  5. Compter combien de "Apples" sont présents dans la liste
apple_count = basket.count("Apples")  # .count() compte le nombre d'occurrences d'un élément
print(f"Il y a {apple_count} pommes dans le panier.")  # Affiche le nombre de pommes

#  6. Vider complètement la liste
basket.clear()  # .clear() supprime tous les éléments de la liste

#  7. Afficher la liste vide
print(basket)  # Affiche []

# Exercise 8

#  Liste des commandes initiales
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich",
                   "Pastrami sandwich", "Egg sandwich", "Chicken sandwich",
                   "Pastrami sandwich"]

# Étape 1 : Supprimer tous les "Pastrami sandwich" car il n'y en a plus
while "Pastrami sandwich" in sandwich_orders:  
    sandwich_orders.remove("Pastrami sandwich")  

#  Étape 2 : Créer une liste pour stocker les sandwichs préparés
finished_sandwiches = []  

#  Étape 3 : Préparer chaque sandwich
while sandwich_orders:  
    current_sandwich = sandwich_orders.pop(0)  # 📌 Retirer le premier sandwich de la liste
    print(f"Je prépare votre {current_sandwich}.")  
    finished_sandwiches.append(current_sandwich)  

#  Étape 4 : Afficher tous les sandwichs préparés
print("\nTous les sandwichs ont été préparés :")
for sandwich in finished_sandwiches:  
    print(f"- {sandwich}")  
