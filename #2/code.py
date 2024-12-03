file = open("./#2/data.txt", "r")
content = file.readlines()

amountOfLines = len(content)
amountOfSafeReportsPartOne = 0
amountOfSafeReportsPartTwo = 0

def checkSafeLevel(row):
    amountOfValuesInRow = len(row)

    isIncreaseCounter = 0 
    isDecreaseCounter = 0
    
    for column in range(amountOfValuesInRow-1):
    
        difference = abs(int(row[column]) - int(row[column + 1]))
        
        if difference > 3 or difference < 1: 
            return False
        
        if int(row[column]) < int(row[column + 1]):
            isIncreaseCounter = isIncreaseCounter + 1 
        
        if int(row[column]) > int(row[column + 1]):
            isDecreaseCounter = isDecreaseCounter + 1 
        
    return isIncreaseCounter == amountOfValuesInRow-1 or isDecreaseCounter == amountOfValuesInRow-1

def checkSafeLevel_problemDampening(row):
    amountOfValuesInRow = len(row)
    results = []
    results.append(checkSafeLevel(row))
    
    for column in range(amountOfValuesInRow):
        newrow = row[:] 
        del newrow[column]
        results.append(checkSafeLevel(newrow))
 
    return any(results)

for line in range(amountOfLines):
    row = content[line].split(' ')
    if checkSafeLevel(row): 
        amountOfSafeReportsPartOne = amountOfSafeReportsPartOne + 1
    if checkSafeLevel_problemDampening(row):
        amountOfSafeReportsPartTwo = amountOfSafeReportsPartTwo + 1

print("#2.1 Amount of safe reports: " , amountOfSafeReportsPartOne)
print("#2.2 Amount of safe reports: " , amountOfSafeReportsPartTwo)