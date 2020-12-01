# Ishaan Lahoti
# CSCI 102 – Section C
# Week 4 - Lab A - Missing Chess Pieces
# References: None
# Time: 20 minutes

print("Please enter the number of white chess pieces that you have of each type:")
kings = int(input("KINGS> "))
queens = int(input("QUEENS> "))
rooks = int(input("ROOKS> "))
bishops = int(input("BISHOPS> "))
knights = int(input("KNIGHTS> "))
pawns = int(input("PAWNS> "))
print("The output below provides the number of each type you have (over or under):")
print("OUTPUT", 1 - kings, 1 - queens, 2 - rooks, 2 - bishops, 2 - knights, 8 - pawns)
