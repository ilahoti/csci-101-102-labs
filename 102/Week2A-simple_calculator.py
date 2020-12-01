# Ishaan Lahoti
# CSCI 102 – Section C
# Week 2 - Lab A - Simple Calculator
# References: None
# Time: 30 minutes

print("Input the first operand.")
first = float(input("FIRST> "))
print("Input the second operand.")
second = float(input("SECOND> "))

print("The sum of", first, "and", second, "is", round(first + second, 1))
print("The difference of", first, "and", second, "is", round(first - second, 1))
print("The product of", first, "and", second, "is", round(first * second, 1))
print("The quotient of", first, "and", second, "is", int(first / second))
print("The remainder of", first, "and", second, "is", round(first % second, 2))
