#   Ishaan Lahoti
#   CSCI 102 – Section C
#   Week 6 - Lab A - Lost Marbles
#   References: None
#   Time: 10 minutes

marbles = input("MARBLES> ")
final = []
for i in range(0, len(marbles)):
    if marbles[i] == "O":
        final.append(i)
print("OUTPUT", final)
