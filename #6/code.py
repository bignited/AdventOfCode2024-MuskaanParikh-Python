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
    match directionTowards:
        case "N": return labMap[currentX-1][currentY] == OBSTACLE
        case "E": return labMap[currentX][currentY+1] == OBSTACLE
        case "S": return labMap[currentX+1][currentY] == OBSTACLE
        case "W": return labMap[currentX][currentY-1] == OBSTACLE

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
    for x in range(amountOfRows): 
        row = []
        for y in range(amountOfColumns-1):
            row.append(CONTENT[x][y])    
        labMap.append(row)

visited = []
resetMap()
guard_x, guard_y = findGuard()
directionTowards = "N"

print(movementsGuard)

for x in range(1, len(movementsGuard)-1):
    shouldContinue = True
    # directionTowards, guard_x, guard_y = movementsGuard[x]
    
    for y in range(1, x):
        if (movementsGuard[y][1] == movementsGuard[x + 1][1] and movementsGuard[y][2] == movementsGuard[x + 1][2]):
            shouldContinue = False 
            break
       
    if shouldContinue == False:
        continue
               
    labMap[movementsGuard[x+1][1]][movementsGuard[x+1][2]] = "#"
    visited = []

    while checkForOTheEnd(guard_x, guard_y) == False:
        print("guard", directionTowards, guard_x, guard_y)
        if [directionTowards, guard_x, guard_y] in visited:
            directionTowards, guard_x, guard_y = movementsGuard[x]
            possibleObstaclesOnMap += 1
            break
        
        else:
            if checkForObstacleAhead(guard_x, guard_y) == False:
                guard_x, guard_y = walkStraight(guard_x, guard_y)
                visited.append([directionTowards, guard_x, guard_y])
                print(visited)
            else:
                directionTowards = turnRight()
    resetMap()
    
        
    
print("#6.2 Guard Patrol steps: ", possibleObstaclesOnMap)