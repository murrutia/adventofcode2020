#!/usr/bin/env python3

from functools import reduce

# input_file = 'input-example.txt'
input_file = 'input.txt'

with open(input_file, 'r') as f:
    forest = f.read().strip().split('\n')

slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]
trees = []

len_row = len(forest[0])
for i in range(len(slopes)):
    trees.append(0)
    col = 0
    row = 0

    while row + slopes[i][1] < len(forest):
        col += slopes[i][0]
        row += slopes[i][1]
        print(f"row : {row} - col : {col % len_row}")
        trees[i] += 1 if forest[row][col % len_row] == '#' else 0

print("Ces chemins vous ont fait rencontrer :")
for i in range(len(slopes)):
    print(f"\tRight {slopes[i][0]}, down {slopes[i][1]} : {trees[i]} arbres")

mult = reduce(lambda x, y : x * y, trees)
print(f"Tous ces arbres multipliés donnent : {mult}")