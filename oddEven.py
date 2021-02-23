list = [1, 2, 3, 4, 5, 6, 7]
sort = 'odd'


def oddEven(list, sort) :
    evenList = []
    oddList = []
    for num in list :
        if num % 2 == 0 :
            evenList.append(num)
        else:
            oddList.append(num)
    if sort == 'even' :
        oddList.extend(evenList)
        return oddList
    else :
        evenList.extend(oddList)
        return evenList

print(oddEven(list, sort))

        

