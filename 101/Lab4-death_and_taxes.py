#   Ishaan Lahoti
#  ​CSCI 101 – Section G
#   Python Lab 4
#   References: None
#   Time: 30 minutes

print("Please enter the filing status:")
status = input("STATUS> ")
print("Please enter the income earned:")
income = float(input("INCOME> "))

tax = 0.0
perc = 0.0

if status == "single":
    if income <= 9325:
        tax = 9325 * .1
    if 9325 < income <= 37950:
       tax += 9325 * .1
       tax += (income - 9325) * .15
    if 37950 < income <= 91900:
       tax += 9325 * .1
       tax += (37950 - 9325) * .15
       tax += (income - 37950) * .25
    if 91900 < income <= 191650:
        tax += 9325 * .1
        tax += (37950 - 9325) * .15
        tax += (91900 - 37950) * .25
        tax += (income - 91900) * .28
    if 191650 < income <= 416900:
        tax += 9325 * .1
        tax += (37950 - 9325) * .15
        tax += (91900 - 37950) * .25
        tax += (191650 - 91900) * .28
        tax += (income - 191650) * .33
    if 416900 < income <= 418400:
        tax += 9325 * .1
        tax += (37950 - 9325) * .15
        tax += (91900 - 37950) * .25
        tax += (191650 - 91900) * .28
        tax += (416900 - 191650) * .33
        tax += (income - 416900) * .35
    if income > 418400:
        tax += 9325 * .1
        tax += (37950 - 9325) * .15
        tax += (91900 - 37950) * .25
        tax += (191650 - 91900) * .28
        tax += (416900 - 191650) * .33
        tax += (418400 - 416900) * .35
        tax += (income - 418400) * .396
    perc = round((tax / income) * 100, 2)
if status == "joint":
    if income <= 18650:
        tax = 18650 * .1
    if 18650 < income <= 75900:
       tax += 18650 * .1
       tax += (income - 18650) * .15
    if 75900 < income <= 153100:
       tax += 18650 * .1
       tax += (75900 - 18650) * .15
       tax += (income - 75900) * .25
    if 153100 < income <= 233350:
        tax += 18650 * .1
        tax += (75900 - 18650) * .15
        tax += (153100 - 75900) * .25
        tax += (income - 153100) * .28
    if 233350 < income <= 416900:
        tax += 18650 * .1
        tax += (75900 - 18650) * .15
        tax += (153100 - 75900) * .25
        tax += (233350 - 153100) * .28
        tax += (income - 233350) * .33
    if 416900 < income <= 470700:
        tax += 18650 * .1
        tax += (75900 - 18650) * .15
        tax += (153100 - 75900) * .25
        tax += (233350 - 153100) * .28
        tax += (416900 - 233350) * .33
        tax += (income - 416900) * .35
    if income > 470700:
        tax += 18650 * .1
        tax += (75900 - 18650) * .15
        tax += (153100 - 75900) * .25
        tax += (233350 - 153100) * .28
        tax += (416900 - 233350) * .33
        tax += (470700 - 416900) * .35
        tax += (income - 470700) * .396
    perc = round((tax / income) * 100, 2)

print("OUTPUT", int(tax))
print("OUTPUT", perc)




