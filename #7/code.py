file = open("./#7/data.txt", "r")
CONTENT = file.readlines()

print(CONTENT)

calculations = []

for i in range(len(CONTENT)):
    result, numbers = CONTENT[i].split(":")
    print(result)
    print(numbers.strip())
    numbersList = []
    for ii in range(len(numbers.strip())):
        numbersList.append(numbers[ii])
        
    calculations.append([result, [numbersList]])

print(calculations)