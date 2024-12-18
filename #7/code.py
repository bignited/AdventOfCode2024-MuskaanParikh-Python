from itertools import product

file = open("./#7/data.txt", "r")
CONTENT = file.readlines()

calculations = []
sum = 0
sumConcat = 0
remainingConcats = []

def calculate(result, numbers):
    calculation = result
    for i in range(len(numbers)):
        if calculation % int(numbers[len(numbers) - 1 - i]) == 0:
            if calculation == int(numbers[0]): return True
            calculation //= int(numbers[len(numbers) - 1 - i])
        else: 
            if calculation == int(numbers[0]): return True
            calculation -= int(numbers[len(numbers) - 1 - i])

def calculateCombination(result, numbers, combination):
    calculation = int(numbers[0])
    
    for i in range(len(combination)):        
        if combination[i] == "*": 
            calculation *= int(numbers[i+1])
        else:
            calculation += int(numbers[i+1])
    
    return result == calculation

def calculateCombinationConcatination(result, numbers, combination):
    calculation = int(numbers[0])
    
    for i in range(len(combination)):
        match combination[i]:
            case "||":
                calculation = int(str(calculation)+numbers[i+1])
            case "*":
                calculation *= int(numbers[i+1])
            case _:
                calculation += int(numbers[i+1])
    return result == calculation
            
      

for i in range(len(CONTENT)):
    result, numbers = CONTENT[i].split(":")
    calculations.append([result, numbers.split(" ")])
    
for i in range(len(calculations)):
    result, numbers = calculations[i]
    numbers.remove("")
    
    foundOne = 0
        
    if calculate(int(result), numbers): 
        sum += int(result)
        foundOne += 1
        
    else: 
        for comb in product(['*', '+'], repeat=len(numbers)-1):
            if calculateCombination(int(result), numbers, comb): 
                sum += int(result)
                foundOne += 1 
                break
    
    if foundOne == 0: remainingConcats.append([result, numbers])
                

for i in range(len(remainingConcats)):
    result, numbers = remainingConcats[i]
        
    for concat in product(['*', '+', '||'], repeat=len(numbers)-1):
        if calculateCombinationConcatination(int(result), numbers, concat): 
            sumConcat += int(result)
            break
                    

print("#7.1 calibration total: ", sum)
print("#7.2 calibration total: ", sum + sumConcat)
