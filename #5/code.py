file = open("./#5/data.txt", "r")
content = file.read()

rules, updates = content.split("\n\n")

updatesList = []
rulesList = []
midCount = 0

for i in range(len(updates.split("\n"))):
    updatesList.append(updates.split("\n")[i].split(","))

for i in range(len(rules.split("\n"))-1):
    rulesList.append(rules.split("\n")[i].split("|"))

def checkCorrectOrder(leftValue, rightValue):
    return [leftValue, rightValue] in rulesList 

for x in range(len(updatesList)): 
    correctUpdate = True 
    
    for y in range(len(updatesList[x])-1):
        if checkCorrectOrder(updatesList[x][y], updatesList[x][y+1]) == False:
            correctUpdate = False
            break
    
    if correctUpdate: 
        midCount = midCount + int(updatesList[x][int(len(updatesList[x])/2)])

print("#5.1 Updates middleIndex: ", midCount)
print("#5.2 Updates middelIndex: ", 0)
