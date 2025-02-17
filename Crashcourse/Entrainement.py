print(type("hello world"))
# alors pour afficher notre code j'utilise print()
# et pour afficher le type de la variable j'utilise type()
#  "hello world " est une chaine de caractère
# <class 'str'> est le type de la variable "hello world"
# le nombre 0 est de type entier
# <class 'int'> est le type de la variable 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# 0.5 est de type float 
# <class 'float'> est le type de la variable 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5

# mon_entier = str(42) 

# ma_string = "hello world"

# print(float(mon_entier) )
#  jai appris que une variable est une espace de stockage qui contient une valeur
# et que pour convertir une variable en chaine de caractère on utilise str()
# et pour afficher la valeur de la variable on utilise print()
# et pour changer le type de la variable on utilise type()
# et pour concaténer deux variables on utilise le signe +
# et pour concaténer une variable et une chaine de caractère on utilise str()
# et pour concaténer une variable et un entier en un float()


# Temperature = int(input("Quelle est la température ?"))
# Tusa = Temperature * 9/5 + 32
# print ( "La température en Fahrenheit est de", Tusa)
#  < <= > >= == !=

# mot_de_passe = input ("Quel est votre mot de passe ?")
        
# if len(mot_de_passe) < 4:
#                 print ("Mot de passe incorrect")
# elif mot_de_passe == "1234":
#                 print ("Mot de passe correct")
# else:
#                 print ("Mot de passe incorrect")
# Moyenne_Bac = float(input("Quelle est votre moyenne au Bac ?"))
# if Moyenne_Bac > 20:
#         print ("Moyenne incorrecte")
# if 12 <= Moyenne_Bac < 14:
#         print ("Mention assez Bien")
# elif  14<= Moyenne_Bac < 16:
#         print ("Mention Bien")
# elif  16<= Moyenne_Bac < 18:
#         print ("Mention Très Bien")
# elif  18<= Moyenne_Bac < 20 :
#         print ("Mention Excellent")
# else:
#         print("pas de mention")

# ma_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
# ma_liste2 = list(range(11, 20))
# ma_liste.append(258)
# ma_liste.remove(5)
# print(10 in ma_liste)
# i = 0
# while i < 10 :
#  print(i)
#  i += 1

# for i in range(10):
#     print(i)

# mot = "mange"

# if "a" in mot:
#     print("le mot contient a")
# else: 
#     print("le mot ne contient pas a")
    
# heure = float(input("Quelle heure est-il ?"))

# if 6 <= heure <12:
#     print("matin")
# elif 12 <= heure < 18:
#     print("apres midi")
# else:
# #     (print("soir"))
# i = 5 
# while i < 15:
#     print(i)
#     i += 3
    
# fruits = ["pomme", "banane", "orange", "fraise"]
    
# for fruit in fruits :
#         print (fruit) 
        
# # fruits = ["pomme", "banane", "cerise"]

# # for fruit in fruits:  # Pour chaque fruit dans la liste
# #     print(fruit)

# i = 1
# while i <= 10:
#     print(i)
#     i *= 2

# mot = ""

# while "a" not in mot:
#     mot = input("Entrez un mot : ")
    
# for i in range(1,6):
#     print(f" le carree de {i} , {i**2}")
    

# for letter in "python":
#     print(letter)

# nb = nb = int(input("Entrez un nombre : "))
# while nb > 0:
#     print(nb)
#     nb -= 1
# nb_secret = 7
# nb = ""
# while nb != nb_secret:
#     nb = int(input("Devinez le nombre ?  "))
#     if nb != nb_secret:
#         print("Mauvaise réponse")
#     else:
#         print("Bonne réponse")

# n = int(input("Entrez un nombre : "))

# for i in range(1,n+1):
#     print(i)
#     i += 1
#     n = n + i

# mot = input("Entrez un mot : ")
# Liste_voyelle = ["a", "e", "i", "o", "u", "y"]
# for i in mot:
#     if i in Liste_voyelle:
#         print(i)
# n = int(input("Entre un nombre : "))  # Demande un nombre à l'utilisateur
# somme = 0  # Initialisation de la somme

# for i in range(1, n + 1):  # Parcourt les nombres de 1 à n
#     somme += i  # Ajoute chaque nombre à la somme

# print("La somme des nombres de 1 à", n, "est :", somme)

