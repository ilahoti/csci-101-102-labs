#   Ishaan Lahoti
#   CSCI 102 – Section C
#   Week 6 - Lab B - Visitors
#   References: None
#   Time: 30 minutes

temp = input("USERS> ")
users = temp.split(", ")
count = []
temp2 = []
for i in range(0, len(users)):
    users[i] = users[i].lower()

for i in users:
    if i not in temp2:
        temp2.append(i)
        count.append(users.count(i))

print("OUTPUT", users)
final = []
for i in range(0, len(temp2)):
    final.append(temp2[i])
    final.append(count[i])
print("OUTPUT", final)
