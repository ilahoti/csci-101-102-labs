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


def score_finder(names, scores, toscore):
    count = 0
    name = ""
    score = 0
    for i in range(0, len(names)):
        if names[i].lower() == toscore:
            name = names[i]
            score = scores[i]
            count += 1

    if count >= 1:
        print("OUTPUT " + name + " got a score of " + str(score))
    else:
        print("OUTPUT player not found")


def union(list1, list2):
    temp1 = list1
    temp2 = list2
    final = []

    for i in range(0, len(temp1)):
        if temp1[i] in temp2:
            temp2[temp2.index(temp1[i])] = "NahG"
            temp1[i] = "NahG"

    for i in range(0, len(temp1)):
        if temp1[i] != "NahG":
            final.append(temp1[i])

    for i in range(0, len(temp2)):
        if temp2[i] != "NahG":
            final.append(temp2[i])

    return final


def intersect(list1, list2):
    result = []

    for i in range(0, len(list1)):
        if list1[i] in list2:
            result.append(list1[i])

    return result


def not_in(list1, list2):
    result = []

    for i in range(0, len(list1)):
        if list1[i] not in list2:
            result.append(list1[i])

    return result

