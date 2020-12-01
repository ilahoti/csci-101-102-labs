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

