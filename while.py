total = 0
count = 0

while True :
    val = input('Enter a number:\n')
    if val == 'done' :
        break
    try :
        num = float(val)
    except :
        print('invalid input')
        continue
    total = total + num
    count = count + 1

print('Total:', total)
print('Count:', count)
print('Average:', total/count)
