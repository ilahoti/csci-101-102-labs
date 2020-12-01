# Ishaan Lahoti
# CSCI 101 - Section G
# Python Lab 2A
# References: no one
# Time: 30 minutes


list1 = list(input("LIST1> "))
list1.insert(0, list1[-1])
list1.insert(0, list1[-2])
list1.pop(-2)
list1.pop(-1)
str1 = "".join(list1)

list2 = list(input("LIST2> "))
list2.pop(-1)
list2.pop(-1)
str2 = "".join(list2)

list3 = list(input("LIST3> "))
numchar = int(len(list3) / 2.0)
i = 0
for x in list3:
    if i < numchar:
        list3[i] = ""
        i += 1
str3 = "".join(list3)

list4 = list(input("LIST4> "))
third = list4[2]
list4[2] = list4[0]
list4[0] = third
str4 = "".join(list4)

list5 = list(input("LIST5> "))
numchar2 = int(len(list5) / 2)
part1 = ""
part2 = ""
j = 0
for x in list5:
    if j < numchar2:
        part1 += list5[j]
        j += 1
    else:
        part2 += list5[j]
        j += 1

print(part1, str1 + str2 + str3 + str4, part2)



