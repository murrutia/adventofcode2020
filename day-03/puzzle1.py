#!/usr/bin/env python3

# input_file = 'input-example.txt'
input_file = 'input.txt'

with open(input_file, 'r') as f:
    forest = f.read().strip().split('\n')

# initialisation des variables
trees = 0
col = 0
row = 0
len_row = len(forest[0])
# print(len(forest))

# Parcours des lignes de la forêt
# Note : comme on sait qu'on avance d'une ligne à chaque tour, on fait s'arrêter
# la boucle quand on sait qu'au tour suivant on sortira de la forêt
while row + 1 < len(forest):
    # application des mouvements
    col += 3
    row += 1

    # On rajoute un arbre si forest[row][col] contient un '#'
    # comme les patterns bouclent sur chaque ligne, on applique module (%) sur le numéro de colonne
    trees += 1 if forest[row][col % len_row] == '#' else 0
    print(f"row : {row} - col : {col} (% = {col % len_row}")

print(f"Ce chemin vous fait rencontrer {trees} arbres.")
