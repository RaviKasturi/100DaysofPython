# https://replit.com/@appbrewery/tip-calculator-start?v=1

print('Welcome to the tip calculator!')
bill = float(input('What is the total bill? $'))
percentage = int(input('What percentage tip would you like to give? 10, 12 or 15? '))
people = int(input('How many people to split the bill? '))

amount = round((bill*(1+percentage/100))/people, 2)

print(f'Each person should pay: ${amount}')
