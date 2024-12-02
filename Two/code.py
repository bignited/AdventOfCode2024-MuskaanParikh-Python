file = open("./Two/data.txt", "r")
content = file.readlines()

amountOfLines = len(content)
amountOfSafeReports = 0

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
        
    if isIncreaseCounter == amountOfValuesInRow-1 or isDecreaseCounter == amountOfValuesInRow-1:
        return True
    else: 
        return False

for line in range(amountOfLines):
    row = content[line].split(' ')
    if checkSafeLevel(row): 
        amountOfSafeReports = amountOfSafeReports + 1

print("#2.1 Amount of safe reports: " , amountOfSafeReports)
