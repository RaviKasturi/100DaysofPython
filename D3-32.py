# https://app.codingrooms.com/management/assignments/364916/overview

height = float(input('Enter your height in meters: '))
weight = float(input('Enter your weight in kgs: '))

BMI = round(weight/height**2,1)

if BMI <= 18.5:
    print(f'Your BMI is {BMI}. You are underweight.')
elif BMI <= 25:
    print(f'Your BMI is {BMI}. You have a normal weight.')
elif BMI <= 30:
    print(f'Your BMI is {BMI}. You are slightly overweight.')
elif BMI <= 35:
    print(f'Your BMI is {BMI}. You are obese.')
else:
    print(f'Your BMI is {BMI}. You are clinically obese.')

