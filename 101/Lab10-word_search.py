#   Ishaan Lahoti
#  ​CSCI 101 – Section G
#   Python Lab 10 - Word Search
#   References: None
#   Time: 30 minutes
import random

file = open("dictionary.txt", "r")
size = int(input("LENGTH> "))
seed = int(input("SEED> "))
random.seed(seed)

sizelist = []
sizecount = 0

list1 = file.read().splitlines()

maxlen = len(list1[0])
maxlist = []

for i in list1:
    if len(i) > maxlen:
        maxlen = len(i)

for i in list1:
    if len(i) == maxlen:
        maxlist.append(i)

for i in range(0, len(list1)):
    if len(list1[i]) == size:
        sizecount += 1
        sizelist.append(list1[i])

temp = random.randrange(0, len(sizelist) - 1)


print("OUTPUT", sizecount)
print("OUTPUT " + '"' + sizelist[temp] + '"')
print("OUTPUT", maxlist)

file.close()
