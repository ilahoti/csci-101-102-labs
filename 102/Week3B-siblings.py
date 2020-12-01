#Ishaan Lahoti
#CSCI 102 – Section C
#Week 3 - Lab B - Three Siblings
#References: None
#Time: 20 minutes

print("Input a positive number for the siblings to consider:")
num = int(input("NUMBER> "))
print("The sibling(s) who will work with", num, "follow:")
digi = str(num)
digisum = 0
for i in digi:
    digisum += int(i)

if num % 2 == 1:
    print("OUTPUT Jimmy")
if 10 <= num <= 100:
    print("OUTPUT Jared")
if digisum == 8 or digisum == 6:
    print("OUTPUT Josephine")

