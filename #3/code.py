import re 

file = open("./#3/data.txt", "r")
content = file.read().strip()

mulList = re.findall('mul\(\d{1,3},\d{1,3}\)', content, re.M)
mullieTotal = 0

for mullie in range(len(mulList)):
    leftValue, rightValue = str(re.findall('\d*,\d*', mulList[mullie], re.M)[0]).split(',')
    mullieTotal = mullieTotal + (int(leftValue) * int(rightValue))

print("#3.1 Mullie total: ", mullieTotal)
