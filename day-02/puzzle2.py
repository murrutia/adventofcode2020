#!/usr/bin/env python3

with open('input.txt', 'r') as f:
    lines = f.read().strip().split('\n')

corrects = 0
wrongs = 0
for line in lines:
    # découpage de la ligne pour obtenir les informations voulues
    rule, password = line.split(': ')
    limits, letter = rule.split(' ')
    one, two = map(lambda x : int(x) - 1, limits.split('-'))

    # vérification de la règle (la lettre DOIT être à la position une OU deux)
    ok = (password[one] == letter) ^ (password[two] == letter)

    # impression des résultats (pour vérification du bon fonctionnement du code) et decompte des bons/mauvais résultats
    print(rule, ':', password, end=' -> ')
    if ok:
        print('correct')
        corrects += 1
    else:
        print('wrong')
        wrongs += 1

print(f"Il y a {wrongs} mauvais passwords dans le fichier")
print(f"Il y a {corrects} bons passwords dans le fichier")

