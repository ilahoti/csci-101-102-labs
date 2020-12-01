# Ishaan Lahoti
# CSCI 101 – Section G
# Python Lab 11
# References: None
# Time: 45 minutes


def read_csv(text):
    with open(text, "r", encoding="utf-8") as file1:
        line = file1.read().splitlines()
        whole = []

        for i in range(0, len(line)):
            whole.append(line[i].split(","))

    return whole


def stops_by_race(default, race):
    whitecount = 0
    blackcount = 0
    asiancount = 0
    tempcount = 0

    for i in range(1, len(default)):
        if default[i][-1] == "WHITE":
            whitecount += 1
        elif "BLACK" in default[i][-1]:
            blackcount += 1
        elif default[i][-1] == "ASIAN":
            asiancount += 1
        else:
            tempcount += 1

    if race.lower() == "white":
        return whitecount
    if race.lower() == "black":
        return blackcount
    if race.lower() == "asian":
        return asiancount
    if race.lower() == "all":
        return whitecount + blackcount + asiancount + tempcount


def stops_by_sex(default, sex):
    male = 0
    female = 0

    for i in range(1, len(default)):
        if default[i][9] == "male":
            male += 1
        elif default[i][9] == "female":
            female += 1

    if sex.lower() == "male":
        return male
    if sex.lower() == "female":
        return female
    if sex.lower() == "ALL":
        return male + female

