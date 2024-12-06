import re

file = open("./#4/data.txt", "r")
CONTENT = file.readlines()

amountOfRows = len(CONTENT)
rowLength = len(CONTENT[0])-1

horizontalCounter = 0

verticalList = []

diagonalList = []

XMAS_REGEX = 'XMAS'
SAMX_REGEX = 'SAMX'

for x in range(amountOfRows):
    
    horizontalCounter = horizontalCounter + len(re.findall(XMAS_REGEX, CONTENT[x], re.M)) + len(re.findall(SAMX_REGEX, CONTENT[x], re.M))
    
    for y in range(rowLength):
        
        if x+3 < rowLength : 
            verticalCheck = CONTENT[x][y]+CONTENT[x+1][y]+CONTENT[x+2][y]+CONTENT[x+3][y]
            if verticalCheck == XMAS_REGEX or verticalCheck == SAMX_REGEX: verticalList.append(verticalCheck)
        
            if y+3 < amountOfRows: 
                diagonalLeftCheck = CONTENT[x][y]+CONTENT[x+1][y+1]+CONTENT[x+2][y+2]+CONTENT[x+3][y+3]
                diagonalRightCheck = CONTENT[x][rowLength-y-1]+CONTENT[x+1][rowLength-y-2]+CONTENT[x+2][rowLength-y-3]+CONTENT[x+3][rowLength-y-4]
                
                if diagonalLeftCheck == XMAS_REGEX or diagonalLeftCheck == SAMX_REGEX: diagonalList.append(diagonalLeftCheck) 
                if diagonalRightCheck == XMAS_REGEX or diagonalRightCheck == SAMX_REGEX: diagonalList.append(diagonalRightCheck) 

print("#4.1 XMAS word search: ", horizontalCounter + len(verticalList) + len(diagonalList))

XmasCounter = 0

def findXPattern(x,y):
    leftDiagonal = CONTENT[x-1][y-1] + CONTENT[x][y] + CONTENT[x+1][y+1]
    rightDiagonal = CONTENT[x-1][y+1] + CONTENT[x][y] + CONTENT[x+1][y-1]
    
    return (leftDiagonal == 'MAS' or leftDiagonal == 'SAM') and (rightDiagonal == 'MAS' or rightDiagonal == 'SAM')
       
for x in range(amountOfRows):
        for y in range(rowLength):
            if y != 0 and y != rowLength-1 and x != 0 and x != amountOfRows-1 and CONTENT[x][y] == 'A':
                    if findXPattern(x,y): XmasCounter = XmasCounter + 1 
            

print("#4.2 XMAS word search: ", XmasCounter)