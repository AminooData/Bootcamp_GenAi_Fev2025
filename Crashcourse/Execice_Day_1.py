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