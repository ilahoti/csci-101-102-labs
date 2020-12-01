# Ishaan Lahoti
# CSCI 102 – Section C
# Week 10 Lab
# References: None
# Time: 30 minutes

with open("formations.csv", "r") as file:
    lines = file.read().splitlines()
    lines.pop(0)
    depths = []
    names = []
    minD = []
    maxD = []
    avg = []
    for i in range(0, len(lines)):
        lines[i] = lines[i].split(",")
        depths.append(lines[i][0])
        names.append(lines[i][1])

    for i in range(0, len(depths)):
        depths[i] = depths[i].split("-")
        minD.append(float(depths[i][0]))
        maxD.append(float(depths[i][1]))
        avg.append(round((float(depths[i][1]) + float(depths[i][0])) / 2, 1))

with open("formations_parsed.csv", "w") as file1:
    file1.writelines("Depth,Start Depth,End Depth,Average Depth,Formation\n")

    for i in range(0, len(lines)):
        file1.writelines(f"{depths[i][0]}-{depths[i][1]},{minD[i]},{maxD[i]},{avg[i]},{names[i]}\n")
