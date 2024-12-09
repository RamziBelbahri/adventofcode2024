
def solution():
    
    f = open("input.txt", "r")
    firstList, secondList = [], []
    for line in f.readlines():
        pair = line.split("   ")
        firstList.append(int(pair[0]))
        secondList.append(int(pair[1]))
    firstList.sort()
    secondList.sort()
    totalDistance = 0
    
    for i in range(len(firstList)):
       totalDistance += abs(firstList[i] - secondList[i])
    return totalDistance 
    
if __name__ == "__main__":
    solution()