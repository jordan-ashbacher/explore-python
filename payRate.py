hourPrompt = 'Enter hours:\n'
hours = int(input(hourPrompt))
ratePrompt = 'Enter pay rate:\n'
rate = float(input(ratePrompt))

totalPay = hours * rate

print('$',totalPay)