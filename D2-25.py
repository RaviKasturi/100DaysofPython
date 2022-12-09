# https://app.codingrooms.com/management/assignments/364911/overview

age = int(input("Enter your current age in years: "))
years_left = 90-age
days = years_left*365
weeks = years_left*52
months = years_left*12

print(f'You have {days} days, {weeks} weeks, and {months} months left.')