# https://app.codingrooms.com/management/assignments/364910/overview

height = float(input('Enter your height in meters: '))
weight = float(input('Enter your weight in kgs: '))

bmi = round(weight/height**2,1)

print(f'Your BMI is {bmi}')

