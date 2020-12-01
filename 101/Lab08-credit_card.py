#   Ishaan Lahoti
#  ​CSCI 101 – Section G
#   Python Lab 8
#   References: None
#   Time: 30 minutes

num = input("NUMBER> ")
list1 = []
list2 = []
list3 = []
sum1 = 0
sum2 = 0
valid = True
for i in num:
    if i != " ":
        list1.append(i)


for i in range(1, len(list1), 2):
    sum1 += int(list1[i])

for i in range(0, len(list1), 2):
    list2.append(str(int(list1[i]) * 2))

for i in range(0, len(list2)):
    for j in range(0, len(list2[i])):
        list3.append(int(list2[i][j]))

for i in range(0, len(list3)):
    sum2 += list3[i]

if (sum1 + sum2) % 10 == 0:
    print("OUTPUT Valid")
else:
    print("OUTPUT Invalid")
    valid = False





