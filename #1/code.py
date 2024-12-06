file = open("./#1/data.txt", "r")
CONTENT = file.readlines()

leftList = []
rightList = []

amountOfLines = len(CONTENT)

distance = 0
similarityScore = 0

for line in range(amountOfLines):
    row = CONTENT[line].split('   ')
    leftList.insert(line, int(row[0]))
    rightList.insert(line, int(row[1].strip()))

leftList.sort()
rightList.sort()

for line in range(amountOfLines):
    distance = distance + abs(leftList[line] - rightList[line])
    similarityScore = similarityScore + (leftList[line] * rightList.count(leftList[line]))     

print("#1.1 Distance: " , distance)
print("#1.2 Similarity score: " , similarityScore)
file.close()