# Ishaan Lahoti
# CSCI 101 – Section G
# Python Lab 2B
# References: None
# Time: 30 minutes

print("Input the currency to convert from")
curr = input("CURRENCY> ")
print("Input today's convert rate for " + curr)
rate = float(input("RATE> "))
print("Input the cost of the item you want to purchase")
cost = float(input("COST> "))
dollar = str(round(cost*rate, 2))
print("The item that costs", round(cost, 1), "in " + curr + " costs $" + dollar + " in US dollars")
print("OUTPUT $" + dollar)


