file = open("./One/data.txt", "r")
content = file.readlines()

leftList = []
rightList = []

distance = 0

for line in range(len(content)):
    
    row = content[line].split('   ')
    leftList.insert(line, row[0])
    rightList.insert(line, row[1].strip())


leftList.sort()
rightList.sort()

for line in range(len(content)):
    distance = distance + abs(int(leftList[line]) - int(rightList[line]))     

print(distance)
file.close()