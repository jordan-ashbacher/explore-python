newString = 'mineral water'
duplicates = []

def findDuplicate(string) :
    for letter in newString :
        if newString.count(letter) > 1 :
            duplicates.append(letter)
    
    if len(duplicates) == 0 :
        return -1
    else :
        return newString.find(duplicates[0])

print(findDuplicate(newString))

