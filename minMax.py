numList = []
minNum = None
maxNum = None

while True :
    val = input('Enter a number:\n')
    if val == 'done' :
        break
    try : 
        num = float(val)
    except :
        print('invalid input')
        continue
    numList.append(num)

print(numList)

for num in numList :
    if maxNum is None or num > maxNum :
        maxNum = num

print('Max:', maxNum)

for num in numList :
    if minNum is None or num < minNum :
        minNum = num

print('Min:', minNum)