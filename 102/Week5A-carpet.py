# Ishaan Lahoti
# CSCI 102 - Section C
# Week 5- Lab A - Carpet
# References: None
# Time: 30 minutes

print("Input the dimensions for the rug, and the character to print:")
width = int(input("WIDTH> "))
height = int(input("HEIGHT> "))
symbol = input("CHARACTER> ")

for i in range(0, height):
    print("OUTPUT", end=" ")
    for j in range(0, width):
        if j == width - 1 and i == height - 1:
            print(symbol, end="")
        else:
            print(symbol, end=" ")
    print("\n", end="")



