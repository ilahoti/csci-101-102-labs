#Ishaan Lahoti
#CSCI 101 – Section G
#Python Lab 3
#References: None
#Time: 20 minutes

hourmax = 24
minmax = 60

hours = int(input("HOURS> "))
minutes = int(input("MINUTES> "))

if minutes - 40 < 0:
    minutes = minmax + (minutes - 40)
    if hours - 1 < 0:
        hours = hourmax - 1
    else:
        hours -= 1
elif minutes - 40 >= 0:
    minutes = minutes - 40

if minutes == 0:
    minutes = "00"

print("OUTPUT", hours, minutes)
