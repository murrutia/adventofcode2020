#!/usr/bin/env python3

import sys

sum_to_find = 2020

# récupération des valeurs dans un tableau trié par ordre croissant
with open('input.txt', 'r') as f:
    values = sorted(map(int, f.read().strip().split('\n')))

# on avance suivant les premières valeurs du tableau
for ind, i in enumerate(values):
    # puis on avance depuis l'indice + 1 pour la seconde valeur
    for j in values[ind+1:]:
        # et on parcoure le tableau à rebours pour la troisième valeur
        # (de cette manière, pas besoin de retenir l'indice de la deuxième valeur pour le parcours des valeurs restantes)
        for k in values[::-1]:
            # si c'est trop grand, on continue
            if i + j + k > sum_to_find:
                pass
            # si c'est la bonne valeur, on s'arrête
            elif i + j + k == sum_to_find:
                print(f"Les valeurs sont {i}, {j} et {k}; le résultat est {i * j * k}")
                sys.exit(0)
            # si c'est trop petit, i et j n'ont pas de k correspondant pour notre somme voulue
            else:
                break

