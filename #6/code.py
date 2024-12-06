file = open("./#6/data.txt", "r")
CONTENT = file.readlines()

amountOfRows = len(CONTENT)
amountOfColumns = len(CONTENT[0])

labMap = []
positionsOnMap = 0

for x in range(amountOfRows): 
    row = []
    for y in range(amountOfColumns-1):
        row.append(CONTENT[x][y])    
    labMap.append(row)
    
DIRECTIONS = ["N", "E", "S", "W"]
directionTowards = "N"
GUARD = "^"

def turnRight():
    indexCurrentDirection = DIRECTIONS.index(directionTowards) 
    if len(DIRECTIONS)-1 == indexCurrentDirection: return DIRECTIONS[0]
    return DIRECTIONS[indexCurrentDirection+1]

def checkForOTheEnd(currentX, currentY):
    match directionTowards:
        case "N": return currentX == 0
        case "E": return currentX == amountOfRows-1 and currentY == amountOfColumns-2
        case "S": return currentX == amountOfRows-1
        case "W": return currentY == 0

def checkForObstacleAhead(currentX, currentY):
    match directionTowards:
        case "N": return labMap[currentX-1][currentY] == "#"
        case "E": return labMap[currentX][currentY+1] == "#"
        case "S": return labMap[currentX+1][currentY] == "#"
        case "W": return labMap[currentX][currentY-1] == "#"

def walkStraight(currentX, currentY):
    match directionTowards:
        case "N": return [currentX-1, currentY]
        case "E": return [currentX, currentY+1]
        case "S": return [currentX+1, currentY]
        case "W": return [currentX, currentY-1]

def findGuard(): 
    for x in range(amountOfRows): 
        if GUARD in labMap[x]: return [x, labMap[x].index(GUARD)]

guard_x, guard_y = findGuard()

while checkForOTheEnd(guard_x, guard_y) == False:
    if checkForObstacleAhead(guard_x, guard_y) == False:
        guard_x, guard_y = walkStraight(guard_x, guard_y)
        labMap[guard_x][guard_y] = GUARD
    else:
        directionTowards = turnRight()

for i in range(amountOfRows): 
    positionsOnMap = positionsOnMap + labMap[i].count(GUARD)

print("#6.1 Guard Patrol steps: ", positionsOnMap)
print("#6.2 Guard Patrol steps: ", 0)