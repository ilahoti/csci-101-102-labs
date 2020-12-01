# Ishaan Lahoti
# Week 8 - Lab A - Reverse Reverse
# References: None
# Time: 30 minutes


print("What size 2D list would you like to create?")
size = int(input("N> "))
OG = []
OG2 = []
count = 1

for i in range(0, size):
    temp = []
    for j in range(0, size):
        temp.append(count)
        count += 1
    OG.append(temp)
    OG2.append(temp)

print("The original list is:")
print(OG)

print("First method: ")

for i in range(0, size):
    OG[i].reverse()
OG.reverse()

print(OG)

print("Second method: ")

new = []

for i in range(size - 1, -1, -1):
    temp2 = []
    for j in range(0, size):
        temp2.append(OG2[i][j])
    new.append(temp2)

print(new)






