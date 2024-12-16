file = open("./#6/data.txt", "r")
CONTENT = file.readlines()

amountOfRows = len(CONTENT)
amountOfColumns = len(CONTENT[0])

labMap = []
positionsOnMap = 0
possibleObstaclesOnMap = 0

for x in range(amountOfRows): 
    row = []
    for y in range(amountOfColumns-1):
        row.append(CONTENT[x][y])    
    labMap.append(row)
    
DIRECTIONS = ["N", "E", "S", "W"]
directionTowards = "N"
GUARD = "^"
OBSTACLE = "#"
movementsGuard = []

def turnRight():
    indexCurrentDirection = DIRECTIONS.index(directionTowards) 
    if len(DIRECTIONS)-1 == indexCurrentDirection: return DIRECTIONS[0]
    return DIRECTIONS[indexCurrentDirection+1]

def checkForOTheEnd(currentX, currentY):
    match directionTowards:
        case "N": return currentX == 0
        case "E": return currentY == amountOfColumns-1
        case "S": return currentX == amountOfRows-1
        case "W": return currentY == 0

def checkForObstacleAhead(currentX, currentY):
    try:
        match directionTowards:
            case "N": return labMap[currentX-1][currentY] == OBSTACLE
            case "E": return labMap[currentX][currentY+1] == OBSTACLE
            case "S": return labMap[currentX+1][currentY] == OBSTACLE
            case "W": return labMap[currentX][currentY-1] == OBSTACLE
    except:
        return False
    

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
movementsGuard.append([directionTowards, guard_x, guard_y])

while checkForOTheEnd(guard_x, guard_y) == False:
    if checkForObstacleAhead(guard_x, guard_y) == False:
        guard_x, guard_y = walkStraight(guard_x, guard_y)
        labMap[guard_x][guard_y] = GUARD
        movementsGuard.append([directionTowards, guard_x, guard_y])
    else:
        directionTowards = turnRight()

for i in range(amountOfRows):
    positionsOnMap = positionsOnMap + labMap[i].count(GUARD)

print("#6.1 Guard Patrol steps: ", positionsOnMap)

def resetMap():
    labMap = []
    for x in range(amountOfRows): 
        row = []
        for y in range(amountOfColumns-1):
            row.append(CONTENT[x][y])    
        labMap.append(row)
    return labMap

uniquePositions = []
 
for direction, x, y in movementsGuard[1:]:
    if [x,y] in uniquePositions:
        continue
    else:
        uniquePositions.append([x,y])

labMap = resetMap()
guard_x, guard_y = findGuard()
uniquePositions.remove([guard_x, guard_y])
 
for x in range(1, len(uniquePositions)):
    visited = []
    labMap = resetMap()
    guard_x, guard_y = findGuard()
    directionTowards = "N"
 
    labMap[uniquePositions[x][0]][uniquePositions[x][1]] = "#"
 
    while checkForOTheEnd(guard_x, guard_y) == False:
        if [directionTowards, guard_x, guard_y] in visited:
            possibleObstaclesOnMap += 1
            break
        else:
            visited.append([directionTowards, guard_x, guard_y])
            if checkForObstacleAhead(guard_x, guard_y) == False:
                guard_x, guard_y = walkStraight(guard_x, guard_y)
            else:
                directionTowards = turnRight()
    
print("#6.2 Guard Patrol steps: ", possibleObstaclesOnMap)