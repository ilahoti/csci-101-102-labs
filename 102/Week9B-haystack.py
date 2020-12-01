# Ishaan Lahoti
# CSCI 102 – Section G
# Week 9 - Lab B - Combing Through a Haystack
# References: None
# Time: 40 minutes

org = input("s> ")
search = input("t> ")
done = True
temp = 0
list1 = []

while done:
    temp = org.find(search, temp, -1)
    if temp == -1:
        break
    list1.append(temp)
    temp += 1

for i in range(0, len(list1)):
    list1[i] += 1

tempstr = ""
for i in range(0, len(list1)):
    if i != len(list1) - 1:
        tempstr += str(list1[i]) + " "
    else:
        tempstr += str(list1[i])

print("OUTPUT", len(list1))
print("OUTPUT", tempstr)


