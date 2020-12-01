# Ishaan Lahoti
# CSCI 102 - Section C
# Week 1 - Part B
# References: None
# Time: 30 minutes

var1 = 0
var2 = 0
var3 = 0

print("Input your weight, in pounds.")
var1 = float(input("WEIGHT> ")) * 0.454
print("Input your height, in inches.")
var2 = float(input("HEIGHT> ")) * .0254
var3 = float(var1 / (var2 ** 2))
print("Your Body-Mass Index is:")
print("OUTPUT", round(var3,1))
