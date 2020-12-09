#
# File:         question_2.py
# Author:       Toby Heath
# Student ID:   110337708
# Email ID:     heaty013@mymail.unisa.edu.au
# Date:         1/12/2020
# Description:  
#   This is my own work as defined by the University's
#   Academic Misconduct Policy
#
from itertools import combinations


def get_combination(filename, digits, target):
    with open(filename) as f:
        for i in combinations([int(x) for x in f.read().split()], digits):
            if sum(i) == target:
                return i


# 2 Digits, 2020
combo_list = get_combination("input.txt", 3, 2020)
combo_prod = 1

for item in combo_list:
    combo_prod *= item

print(combo_prod)
