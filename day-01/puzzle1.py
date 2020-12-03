#!/usr/bin/env python3

import sys

sum_to_find = 2020

# récupération des valeurs dans un tableau trié par ordre croissant
with open('input.txt', 'r') as f:
    all_file = f.read()                     # lecture du fichier dans une string
    all_file_trimmed = all_file.strip()     # nettoyage des caractères 'blancs' au début et à la fin
    lines = all_file_trimmed.split('\n')    # découpage par lignes pour obtenir un tableau
    values = map(int, lines)                # application de la fonction `int()` sur chaque valeur du tableau (sinon ce sont des `str`)
    values_sorted = sorted(values)          # tri des valeurs par ordre croissant
    
    # toutes ces opérations peuvent être effectuées sur une seule ligne :
    # values_sorted = sorted(map(int, f.read().strip().split('\n')))
    
for one in values_sorted:
    for two in values_sorted[::-1]:
        if one + two == sum_to_find:
            print(f"Les valeurs sont {one} et {two} et le résultat est {one * two}")
            sys.exit(0)

print("Aucune addition n'a donné le bon résultat")
