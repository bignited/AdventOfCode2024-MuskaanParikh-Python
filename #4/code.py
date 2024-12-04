import re

file = open("./#4/data.txt", "r")
content = file.readlines()

amountOfRows = len(content)
rowLength = len(content[0])-1

horizontalCounter = 0

verticalCounter = 0 
verticalList = []

diagonalCounter = 0
diagonalListLR = []
diagonalListRL = []

XMAS_REGEX = 'XMAS'
SAMX_REGEX = 'SAMX'

def findPattern(list):
    total = 0 
    for i in range(len(list)):
        total = total + len(re.findall(XMAS_REGEX, list[i], re.M)) + len(re.findall(SAMX_REGEX, list[i], re.M))
    return total

for x in range(amountOfRows):
    for y in range(rowLength):
        if x+3 < rowLength: 
            verticalList.append(content[x][y]+content[x+1][y]+content[x+2][y]+content[x+3][y])
        
        if x+3 < rowLength and y+3 < amountOfRows: 
            diagonalListLR.append(content[x][y]+content[x+1][y+1]+content[x+2][y+2]+content[x+3][y+3])
            diagonalListRL.append(content[x][rowLength-y-1]+content[x+1][rowLength-y-2]+content[x+2][rowLength-y-3]+content[x+3][rowLength-y-4])

horizontalCounter = horizontalCounter + findPattern(content)
verticalCounter = verticalCounter + findPattern(verticalList)
diagonalCounter = diagonalCounter + (findPattern(diagonalListLR) + findPattern(diagonalListRL))

print("#4.1 XMAS word search: ", horizontalCounter + verticalCounter + diagonalCounter)

XmasCounter = 0

def findXPattern(x,y):
    leftDiagonal = content[x-1][y-1] + content[x][y] + content[x+1][y+1]
    rightDiagonal = content[x-1][y+1] + content[x][y] + content[x+1][y-1]
    
    return (leftDiagonal == 'MAS' or leftDiagonal == 'SAM') and (rightDiagonal == 'MAS' or rightDiagonal == 'SAM')
       
for x in range(amountOfRows):
        for y in range(rowLength):
            if y != 0 and y != rowLength-1 and x != 0 and x != amountOfRows-1 and content[x][y] == 'A':
                    if findXPattern(x,y): XmasCounter = XmasCounter + 1 
            

print("#4.2 XMAS word search: ", XmasCounter)