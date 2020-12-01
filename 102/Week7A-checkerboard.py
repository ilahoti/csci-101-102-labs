#   Ishaan Lahoti
#   CSCI 102 – Section C
#   Week 7 - Lab A - Checkerboard
#   References: None
#   Time: 30 minutes

length = int(input("LENGTH> "))
first = input("FIRST> ")
second = input("SECOND> ")
big = []


for i in range(0, length):
    small = []
    for j in range(0, length):
        if i % 2 == 0 and j % 2 == 1:
            small.append(second)
        elif i % 2 == 0 and j % 2 == 0:
            small.append(first)
        elif i % 2 == 1 and j % 2 == 0:
            small.append(second)
        elif i % 2 == 1 and j % 2 == 1:
            small.append(first)
    print("OUTPUT", small)
    big.append(small)
print("OUTPUT", big)

