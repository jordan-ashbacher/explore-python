hourPrompt = 'Enter hours:\n'
ratePrompt = 'Enter pay rate:\n'
try : 
    hours = float(input(hourPrompt))
    rate = float(input(ratePrompt))
    if hours > 40 :
        overtimeHours = hours - 40
        overtimeRate = rate * 1.5
        totalPay = (rate * 40) + (overtimeRate * overtimeHours)
        print('Pay:', totalPay)
    else :
        totalPay = hours * rate
        print('Pay:', totalPay)
except :
    print('Please enter a number')


