file = open("./#5/data.txt", "r")
content = file.read()

rules, updates = content.split("\n\n")

updatesList = []
rulesList = []
incorrectUpdatesList= []

for i in range(len(updates.split("\n"))):
    updatesList.append(updates.split("\n")[i].split(","))

for i in range(len(rules.split("\n"))-1):
    rulesList.append(rules.split("\n")[i].split("|"))

def checkCorrectOrder(leftValue, rightValue):
    return [leftValue, rightValue] in rulesList 

def checkCorrectRowForCorrectOrder(row):
    rowValid = True
    
    for y in range(len(row)-1):
        if checkCorrectOrder(row[y], row[y+1]) == False:
            rowValid = False
    return rowValid        

def getMiddleOfRow(row, x): 
    return int(row[x][int(len(row[x])/2)])

def addMiddleOfCorrectUpdates(list): 
    total = 0
    for x in range(len(list)): 
        if checkCorrectRowForCorrectOrder(list[x]): total = total + getMiddleOfRow(list, x)
    return total

print("#5.1 Updates middleIndex: ", addMiddleOfCorrectUpdates(updatesList))

def findIncorrectRows(list):
    for x in range(len(list)):
        if checkCorrectRowForCorrectOrder(list[x]) == False: incorrectUpdatesList.append(list[x])  

findIncorrectRows(updatesList)

def fixIncorrectRow(row):
    for y in range(len(row)-1):
        if checkCorrectOrder(row[y], row[y+1]) == False: 
            tempLeft = row[y]
            tempRight = row[y+1]
        
            row[y] = tempRight
            row[y+1] = tempLeft
    return row

for x in range(len(incorrectUpdatesList)):
    while checkCorrectRowForCorrectOrder(incorrectUpdatesList[x]) == False: 
        incorrectUpdatesList[x] = fixIncorrectRow(incorrectUpdatesList[x])

print("#5.2 Updates middelIndex: ", addMiddleOfCorrectUpdates(incorrectUpdatesList))
