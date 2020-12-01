# Ishaan Lahoti
# CSCI 102 - Section C
# Week 5- Lab B - Prime Factors
# References: None
# Time: 30 minutes

keepgoing = True
while keepgoing:
    print("Enter a positive integer to generate its Prime Factors:")
    num = int(input("INPUT> "))
    factors = []
    count1 = 1
    primefactors = []
    finalanswer = []
    secondgoing = True
    count3 = 0
    tempnum = num
    stringversion = ""
    while count1 <= num:
        if num % count1 == 0:
            factors.append(count1)
        count1 += 1
    for x in factors:
        tempfactors = []
        for count2 in range(1, x + 1):
            if x % count2 == 0:
                tempfactors.append(count2)
        if len(tempfactors) == 2:
            primefactors.append(x)
    while count3 < len(primefactors):
        if tempnum % primefactors[count3] == 0:
            finalanswer.append(primefactors[count3])
            tempnum = tempnum / primefactors[count3]
        else:
            count3 += 1
    for x in finalanswer:
        stringversion += str(x) + "*"
    print(f"OUTPUT {stringversion[0:-1]}")
    print("Do you want to get Prime Factors for another input? (y/n)")
    cont = input("CONTINUE> ")
    if cont[0].lower() == "n":
        keepgoing = False
print("-------------------------------------------------------------")
print("Goodbye!")

