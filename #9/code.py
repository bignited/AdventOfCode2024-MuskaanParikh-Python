file = open("./#9/data.txt")
CONTENT = file.read()

diskMap = list(CONTENT)

DOT="."
X=":"
diskSpaces = [] 

def getAmountOfValue(list, ids, space, doesItHaveToBeDot = False):
    for i in range(space): 
        if doesItHaveToBeDot:
            list.append(DOT) 
        else: 
            list.append(ids)

def createString():
    ids = 0
    for i in range(len(diskMap)):
        if i%2 != 0: 
            getAmountOfValue(diskSpaces,ids,int(diskMap[i]), doesItHaveToBeDot=True) 
            ids+=1
        else: 
            getAmountOfValue(diskSpaces,ids,int(diskMap[i]), doesItHaveToBeDot=False) 
            
def replaceDotWithBackNumber(list):
    counterYoinked = 0
    for i in range(len(list)):
        if all(item == '.' for item in list[list.index("."):]):
            break
        else:
            while list[len(list)-counterYoinked-1] == DOT:
                counterYoinked += 1
            
            if list[i] == DOT:
                list[i] = list[len(list)-counterYoinked-1]
                list[len(list)-counterYoinked-1] = DOT

                counterYoinked += 1

def calculateFilesystemChecksum(list):
    checksum = 0
    for i in range(len(list)):
        if list[i] != DOT:
            checksum += (i * int(list[i]))
    return checksum

createString()
replaceDotWithBackNumber(diskSpaces)
print("#9.1 Calculate Filesystem checksum: ", calculateFilesystemChecksum(diskSpaces))