array = ['a', 'b', 'c', 'd']

def shuffle(myArray):
    shuffles = []
    myArrayCopy = list(myArray)
    if len(myArray) == 1:
        return [myArray]
    for i in range(len(myArray)):
        myArrayCopy = list(myArray)
        myArrayCopy.insert(0, myArrayCopy.pop(i))
        newShuffle = shuffle(myArrayCopy[1:])
        for item in newShuffle:
            item.insert(0, myArrayCopy[0])
            shuffles.append(item)
    return shuffles

print(shuffle(array))