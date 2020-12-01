#   Ishaan Lahoti
#  ​CSCI 101 – Section G
#   Python Lab 7
#   References: None
#   Time: 45 minutes

rows = int(input("ROWS> "))
col = int(input("COLUMNS> "))
big = []
watered = True
big2 = []
temp = big

for i in range(0, rows):
    big.append(input("ROW" + str(i) + "> ").split(" "))

# Row Check
for i in range(0, rows):
    for j in range(0, col):
        if big[i][j] == "c":
            if j < col - 1 and j != 0:
                if big[i][j + 1] == "w" or big[i][j - 1] == "w":
                    temp[i][j] = " "
            elif j == 0 and col - 1 != 0:
                if big[i][j + 1] == "w":
                    temp[i][j] = " "
            elif j == col - 1 and col - 1 != 0:
                if big[i][j - 1] == "w":
                    temp[i][j] = " "


# Column Check
for i in range(0, rows):
    for j in range(0, col):
        if big[i][j] == "c":
            if i < rows - 1 and i != 0:
                if big[i + 1][j] == "w" or big[i - 1][j] == "w":
                    temp[i][j] = " "
            elif i == 0 and rows - 1 != 0:
                if big[i + 1][j] == "w":
                    temp[i][j] = " "
            elif i == rows - 1 and rows - 1 != 0:
                if big[i - 1][j] == "w":
                    temp[i][j] = " "

# Diagonal Check
for i in range(0, rows):
    for j in range(0, col):
        if big[i][j] == "c":
            if i < rows - 1 and i != 0 and j < col - 1 and j != 0:
                if big[i + 1][j + 1] == "w" or big[i - 1][j + 1] == "w" or big[i + 1][j - 1] == "w" or big[i - 1][j - 1] == "w":
                    temp[i][j] = " "
            elif j == 0 and i == 0 and col - 1 != 0 and rows - 1 != 0:
                if big[i + 1][j + 1] == "w":
                    temp[i][j] = " "
            elif j == col - 1 and i == 0 and col - 1 != 0 and rows - 1 != 0:
                if big[i + 1][j - 1] == "w":
                    temp[i][j] = " "
            elif j == 0 and i == rows - 1 and col - 1 != 0 and rows - 1 != 0:
                if big[i - 1][j + 1] == "w":
                    temp[i][j] = " "
            elif j == col - 1 and i == rows - 1 and col - 1 != 0 and rows - 1 != 0:
                if big[i - 1][j - 1] == "w":
                    temp[i][j] = " "
            elif i == 0 and col - 1 != 0 and rows - 1 != 0:
                if big[i + 1][j - 1] == "w" or big[i + 1][j + 1] == "w":
                    temp[i][j] = " "
            elif i == rows - 1 and col - 1 != 0 and rows - 1 != 0:
                if big[i - 1][j - 1] == "w" or big[i - 1][j + 1] == "w":
                    temp[i][j] = " "
            elif j == 0 and col - 1 != 0 and rows - 1 != 0:
                if big[i - 1][j + 1] == "w" or big[i + 1][j + 1] == "w":
                    temp[i][j] = " "
            elif j == col - 1 and col - 1 != 0 and rows - 1 != 0:
                if big[i - 1][j - 1] == "w" or big[i + 1][j - 1] == "w":
                    temp[i][j] = " "

# Coordinates
for i in range(0, rows):
    for j in range(0, col):
        if temp[i][j] == "c":
            big2.append((i, j))
            watered = False

print("OUTPUT", watered)

if not watered:
    print("OUTPUT", big2)




            


