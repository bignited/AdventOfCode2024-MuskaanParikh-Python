import re 

file = open("./#3/data.txt", "r")
CONTENT = file.read().strip()

partOneRegex = 'mul\(\d{1,3},\d{1,3}\)'
mulListOne = re.findall(partOneRegex, CONTENT, re.M)

def calculateMullie(list):
    total = 0
    for mullie in range(len(list)):
        leftValue, rightValue = str(re.findall('\d*,\d*', list[mullie], re.M)[0]).split(',')
        total = total + (int(leftValue) * int(rightValue))
    return total


partTwoRegex = 'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)'
mulListTwo = re.findall(partTwoRegex, CONTENT, re.M)
mullieTotalTwo = 0
doMullie = True

for mullie in range(len(mulListTwo)):

    if mulListTwo[mullie] == 'do()':
        doMullie = True

    if mulListTwo[mullie] == 'don\'t()':
        doMullie = False 

    if doMullie and mulListTwo[mullie] != 'do()' and mulListTwo[mullie] != 'don\'t()':
        leftValue, rightValue = str(re.findall('\d*,\d*', mulListTwo[mullie], re.M)[0]).split(',')
        mullieTotalTwo = mullieTotalTwo + (int(leftValue) * int(rightValue))

print("#3.1 Mullie total: ", calculateMullie(mulListOne))
print("#3.2 Mullie total: ", mullieTotalTwo)
