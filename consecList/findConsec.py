#l = [2,3,8,9,10,11,12] #min straight
#l = [2,3,4,5,6,11,12] #max straight
l = [2,7,8,9,10,11,13] #mid straight


def getStraight(mylist = l,maxHandSize = 5):
    counter = 0
    tempIndex = []
    for i in range(0,len(mylist)-1):
        if len(tempIndex) == maxHandSize - 1:
            return mylist[min(tempIndex):max(tempIndex)+2]
        if mylist[i+1] - mylist[i] == 1:
            counter+=1
            tempIndex.append(i)
        else:
            counter = 0
            del tempIndex[:]
    return mylist[min(tempIndex):]

print(getStraight())