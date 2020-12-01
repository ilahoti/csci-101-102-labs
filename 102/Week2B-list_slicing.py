# Ishaan Lahoti
# CSCI 102 – Section C
# Week 2 - Lab B - List Slicing
# References: None
# Time: 30 minutes

print("Enter your string:")
words = str(input("STRING> "))
print("Enter four numbers to slice the string")
first = int(input("A> "))
second = int(input("B> "))
third = int(input("C> "))
fourth = int(input("D> "))
newfirst = words[first:second+1]
newsec = words[third:fourth+1]
print("OUTPUT", newfirst, newsec)
