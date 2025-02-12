# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# dictionnary = dict(zip(keys, values))
# print(dictionnary)

# first_name = "Jhon" 
# last_name = "Doe"
# favorite_hobby = "Python"
# sport_hobby = "Gym"
# age = 82

# dictionnary = dict(zip(["First Name", "Last Name", "Favorite Hobby", "Sport Hobby", "Age"], [first_name, last_name, favorite_hobby, sport_hobby, age]))
# print(dictionnary)

# # Exercice 2

# # Print the total duration of the playlist

# playlist = {
#     'title': "Hello World",
#     'author': "Planet",
#     'songs': [
#         {
#             'song_title': "Song One",
#             'artist': ['Artist 1', 'Artist 2'],
#             'duration': 4.31,
#         },
#         {
#             'song_title': "Song Two",
#             'artist': ['Artist 1'],
#             'duration': 2.53,
#         },
#         {
#             'song_title': "Song Three",
#             'artist': ['Artist 1', 'Artist 2', 'Artist 3'],
#             'duration': 3.43,
#         }
#     ]
# }

# dure_playlist = sum([song['duration'] for song in playlist['songs']])
# print(dure_playlist)

def average_length_of_words(sentence):
    """
    Calcule la longueur moyenne des mots dans une phrase.
    Arrondit le résultat à 1 décimale.
    """
    words = sentence.split()  # Divise la phrase en mots
    total_length = sum(len(word) for word in words)  # Calcule la somme des longueurs des mots
    return round(total_length / len(words), 1)  # Calcule la moyenne et arrondit
