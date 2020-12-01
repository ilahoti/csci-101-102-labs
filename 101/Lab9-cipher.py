#   Ishaan Lahoti
#  ​CSCI 101 – Section G
#   Python Lab 9
#   References: None
#   Time: 30 minutes

alpha1 = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
list1 = alpha1.split(" ")
alpha2 = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
list2 = alpha2.split(" ")

rev1 = "z y x w v u t s r q p o n m l k j i h g f e d c b a"
revlist1 = rev1.split(" ")
rev2 = "Z Y X W V U T S R Q P O N M L K J L H G F E D C B A"
revlist2 = rev2.split(" ")

ask = input("STRING> ")
newlist = []
asklist = []
for i in ask:
    asklist.append(i)

for i in range(0, len(asklist)):
    temp = False
    for j in range(0, len(list1)):
        if asklist[i] == list1[j]:
            newlist.append(revlist1[j])
            temp = True
        elif asklist[i] == list2[j]:
            newlist.append(revlist2[j])
            temp = True
    if not temp:
        newlist.append(asklist[i])

print("OUTPUT", "".join(newlist))

