#Ishaan Lahoti
#CSCI - 102 Section C
#Week 3A Twitter
#References: None
#Time: 20 minutes

print("Enter the Tweet or Message abbreviation to decode.")
tweet = input("TWEET> ")
decoded = ""
print("The decoded abbreviation is: ")
if tweet == "IDK":
    decoded = "I don't know"
if tweet == "BTW":
    decoded = "By the way"
if tweet == "CU":
    decoded = "See you"
if tweet == "AFAIK":
    decoded = "As far as I know"
print("OUTPUT", tweet, "=", decoded)
