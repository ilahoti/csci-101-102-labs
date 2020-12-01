# Ishaan Lahoti
# CSCI 102 – Section C
# Week 4 - Lab B - Amino Acids
# Refrences: None
# Time: 20 minutes

Alanine = [3, 7, 1, 2, 0]
Arginine = [6, 14, 4, 2, 0]
Asparagine = [4, 8, 2, 3, 0]
Cysteine = [3, 7, 1, 2, 1]
Histidine = [6, 9, 3, 2, 0]
Glutamine = [5, 10, 2, 3, 0]
mystery = []
amino = ""
print("Input the chemical elements of the amino acid:")
mystery.append(int(input("CARBON> ")))
mystery.append(int(input("HYDROGEN> ")))
mystery.append(int(input("NITROGEN> ")))
mystery.append(int(input("OXYGEN> ")))
mystery.append(int(input("SULFUR> ")))
if mystery == Alanine:
    amino = "Alinine"
if mystery == Arginine:
    amino = "Arginine"
if mystery == Asparagine:
    amino = "Asparagine"
if mystery == Cysteine:
    amino = "Cysteine"
if mystery == Histidine:
    amino = "Histidine"
if mystery == Glutamine:
    amino = "Glutamine"
for x in range(0, len(mystery)):
    mystery[x] = str(mystery[x])
print("The amino acid for C-" + mystery[0] + "H-" + mystery[1] + "N-" + mystery[2] + "O-" + mystery[3] + "S-" + mystery[4] + " is " + amino)
print("OUTPUT C-" + mystery[0] + "H-" + mystery[1] + "N-" + mystery[2] + "O-" + mystery[3] + "S-" + mystery[4])
print("OUTPUT " + amino)



