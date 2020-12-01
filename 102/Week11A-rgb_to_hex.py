# Ishaan Lahoti
# CSCI 102 – Section G
# Week 11 Lab
# References: None
# Time: 45 minutes


def to_hex(value):

    value = int(value)
    hexletters = ["A", "B", "C", "D", "E", "F"]
    quot = int(value / 16)
    rem = int(value % 16)
    result = ""
    count = 0
    while count < 2:

        if rem > 9:
            result += hexletters[rem % 10]
        elif 0 < rem < 10:
            result += str(rem)
        else:
            result += "0"

        rem = int(quot % 16)
        quot = int(quot / 16)

        count += 1

    return result[::-1]


def rgb_to_hex(red, green, blue):
    red = int(red)
    green = int(green)
    blue = int(blue)

    final = ""
    final += to_hex(red)
    final += to_hex(green)
    final += to_hex(blue)

    return final
