from itertools import combinations


def get_combination(filename, digits, target):
    with open(filename) as f:
        for i in combinations([int(x) for x in f.read().split()], digits):
            if sum(i) == target:
                return i


# 2 Digits, 2020
combo_list = get_combination("input.txt", 2, 2020)
combo_prod = 1

for item in combo_list:
    combo_prod *= item

print(combo_prod)