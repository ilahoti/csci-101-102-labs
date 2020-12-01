# Ishaan Lahoti
# CSCI 101 – Section G
# Python Lab 6
# References: None
# Time: 30 minutes

dna = input("STRING> ")
list1 = []
for i in dna:
    list1.append(i)

acount = 0
ccount = 0
gcount = 0
tcount = 0
output = ""
default = 0

for i in range(0, len(list1)):
    if list1[i] == "A":
        acount += 1
    elif list1[i] == "C":
        ccount += 1
    elif list1[i] == "G":
        gcount += 1
    elif list1[i] == "T":
        tcount += 1
        list1[i] = "U"
    else:
        output = "DNA string not valid"
        default = 1
        break
    output += list1[i]
if default != 1:
    print("OUTPUT", acount, ccount, gcount, tcount)
print("OUTPUT " + output)
