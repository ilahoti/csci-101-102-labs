# Ishaan Lahoti
# CSCI 102 – Section G
# Week 9 - Lab B - Combing Through a Haystack
# References: None
# Time: 40 minutes

import random

randlist = []
rolls = int(input("NUMBER> "))
seed = int(input("SEED> "))
random.seed(seed)
countlist = [0, 0, 0, 0, 0, 0]

for i in range(0, rolls):
    temp = random.randint(1, 6)
    if temp == 1:
        countlist[0] += 1
    elif temp == 2:
        countlist[1] += 1
    elif temp == 3:
        countlist[2] += 1
    elif temp == 4:
        countlist[3] += 1
    elif temp == 5:
        countlist[4] += 1
    elif temp == 6:
        countlist[5] += 1

for i in range(1, 7):
    print("OUTPUT", i, "occurred", countlist[i - 1], "times")
