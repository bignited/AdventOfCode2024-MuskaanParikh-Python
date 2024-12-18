from itertools import product

file = open("./#7/data.txt", "r")
CONTENT = file.readlines()

calculations = []
sum = 0

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
    
        
for i in range(len(CONTENT)):
    result, numbers = CONTENT[i].split(":")
    calculations.append([result, numbers.split(" ")])
    
for i in range(len(calculations)):
    result, numbers = calculations[i]
    numbers.remove("")
        
    if calculate(int(result), numbers): 
        sum += int(result)
        
    else: 
        for comb in product(['*', '+'], repeat=len(numbers)-1):
            if calculateCombination(int(result), numbers, comb): 
                sum += int(result)
                break

print("#7.1 calibration total: ", sum)