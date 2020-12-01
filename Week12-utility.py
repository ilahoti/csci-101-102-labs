# Ishaan Lahoti
# CSCI 102 – Section C
# Week 12 - Utility using Git and Incremental Development
# References: Brenton Dixon, Chad Holmes
# Time: 50 minutes


def load_file(name):
    file = open(name, "r")
    list1 = []

    for i in file:
        list1.append(i[0:-1])

    return list1


def update_string(org, add, ind):
    temp = ""
    for i in range(0, len(org)):
        if i == ind:
            for j in range(0, len(add)):
                temp += add[j]
        temp += org[i]

    return temp


def find_word_count(list2, tofind):
    count = 0
    temp = list2
    for i in temp:
        temp2 = i.split(" ")
        for j in temp2:
            if j == tofind:
                count += 1

    return count
